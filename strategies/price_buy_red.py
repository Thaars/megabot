import json
import zlib
import pandas as pd
import definitions

# todo: add description
"""
 
"""

STATE_RUNNING = 'running'
STATE_HOLD = 'hold'
STATE_DEAD = 'dead'


# these classes will hold all the required information for their part of the strategy
# it defines all possibilities and will generate random values based on that
# possible values and analyze the data for each tick
class PRICE_BUY_RED:
    def __init__(self, df, pf):
        self.indicator = self.__class__.__name__
        self.df = df
        self.pf = pf
        self.config = definitions.PRICE_BUY_RED_CONFIG
        self.cycles = list()
        # the maximum percentage part of the start cash in the portfolio to invest in this cycle
        self.cycle_max_invest_of_cash_in_percent = self.config['cycle_max_invest_of_cash_in_percent']
        # the number of dollars which will be invested for each order
        self.order_invest = self.config['order_invest']
        # the multiplier to append more cash to a buy when the next red candle is much longer
        # the lower the price, the more the invest
        self.order_invest_factor = self.config['order_invest_factor']
        # a factor to increase the sell price related to the buying price in percent
        self.sell_price_factor_in_percent = self.config['sell_price_factor_in_percent']
        # the number of candles from the last buy until the cycle goes on hold
        self.candle_limit_until_hold = self.config['candle_limit_until_hold']
        # the number of candles from the last buy and for cycles on hold until the sell price
        # will not be longer cycle start price, it will be changed to the cycle average buying price
        # to disable this, set it to None
        self.candle_limit_until_sell_for_average_price = self.config['candle_limit_until_sell_for_average_price']

    def prepare(self):
        pass

    def analyze(self):
        for (line, (index, row)) in enumerate(self.df.iterrows()):
            if line == 0:
                self.pf.market_start_amount = row.close
            # remember the last price at the very end of the back testing for calculating stats
            if line + 1 == len(self.df):
                self.pf.market_end_amount = row.close
            # create cycle
            if len(self.cycles) == 0:
                self.create_cycle(line)

            cycles_running = 0
            for cycle in self.cycles:
                # sell
                self.sell(line, index, row, cycle)
                # buy
                self.buy(line, index, row, cycle)
                # todo: on hold phase
                #   in dieser phase könnte ein weiterer zyklus gestartet werden,
                #   der sich grundsätzlich auf einem niedrigeren niveau bewegt aber dennoch profitabel sein kann
                #   evtl. defensiver arbeiten, also statt 5% des portfolios nur 1% als startgeld für den zyklus nehmen
                # check on hold
                if cycle['state'] == STATE_RUNNING \
                        and cycle['latest_bought_on_candle'] is not None \
                        and cycle['latest_bought_on_candle'] + self.candle_limit_until_hold < line:
                    cycle['state'] = STATE_HOLD
                # if on hold, check for setting the average buying price as sell price
                if cycle['state'] == STATE_HOLD \
                        and self.candle_limit_until_sell_for_average_price is not None \
                        and cycle['latest_bought_on_candle'] + self.candle_limit_until_sell_for_average_price < line \
                        and cycle['sell_price_changed'] is False:
                    cycle_stats = self.calc_cycle_stats(line, index, row, cycle)
                    cycle['sell_price'] = cycle_stats['average_buying_price']
                    # this is needed to prevent infinity loops while checking this on each candle after the first hit
                    cycle['sell_price_changed'] = True
                # check how much cycles are still running
                if cycle['state'] == STATE_RUNNING:
                    cycles_running += 1

            # create a new cycle if all existing cycles are on a different state
            if cycles_running == 0:
                self.create_cycle(line)

        self.pf.cycles_for_stats = self.cycles
        return self.df, self.pf, self.config

    def create_cycle(self, line):
        cycle = dict(cycle_id=len(self.cycles),
                     start_price=0,
                     sell_price=0,
                     start_cash=0,
                     start_candle=line,
                     orders=list(),
                     state=STATE_RUNNING,
                     stats=list(),
                     latest_bought_on_candle=None,
                     sell_price_changed=False)
        self.cycles.append(cycle)

    def buy(self, line, index, row, cycle):
        # todo: position öffnen wenn die kerze rot ist
        #   und noch nicht 10x nachgekauft wurde
        #   bzw. das muss ein prozentualer anteil des portfolios sein
        #   - bspw. 1000 € im topf - davon maximal 50% einsetzen - hard cap
        #   - feste summen investieren - 5% des startpreises zzgl. prozentual zur roten kerze
        #   -- wenn die kerze um 40% gegenüber dem startpreis (1. order in diesem zyklus) gefallen ist, dann 40% von 5%des startpreises on top
        #   - so lange bei roten kerzen nachkaufen, bis der hard cap von 500 € (50%) überschritten wäre - nicht überschreiten
        # red candle
        if cycle['state'] == STATE_HOLD or cycle['state'] == STATE_DEAD:
            return False
        if row['close'] < row['open']:
            # buy only, if the close price is lower than the cycle start price or if no order exists yet
            if len(cycle['orders']) == 0 or cycle['start_price'] > row['close']:
                # no open orders - set cycle start values
                if len(cycle['orders']) == 0:
                    cycle['start_price'] = row['close']
                    cycle['sell_price'] = row['close']
                    cycle['start_cash'] = self.pf.cash
                # calc buy amount of cash
                # calc the percentage loss of the current candle relative to the cycle start price
                # the lower the price, the higher the invest
                current_candle_percentage_loss = 100 - row['close'] * 100 / cycle['start_price']
                # take the percentage and add it to the buy price with the defined factor
                # without the factor the invest increment could be too low
                buy_amount_of_cash = self.order_invest + self.order_invest / 100 * (
                            current_candle_percentage_loss * self.order_invest_factor)
                # max invest of the portfolio cash in percent
                # the cash shouldn't be less than this
                if self.pf.cash - buy_amount_of_cash > \
                        cycle['start_cash'] - cycle['start_cash'] / 100 * self.cycle_max_invest_of_cash_in_percent:
                    # create order
                    order = self.pf.create_order(
                        df=self.df,
                        index=index,
                        current_price=row['close'],
                        target=None,
                        stop_loss=None,
                        units=buy_amount_of_cash / row['close']
                    )
                    # add order to cycle
                    cycle['orders'].append(order)
                    # remember the line to determine if the cycle goes on hold
                    cycle['latest_bought_on_candle'] = line
                    return cycle

        return False

    def sell(self, line, index, row, cycle):
        # todo: verkaufen bei grüner kerze und close preis über dem startpreis des zyklus
        #   - wenn nach n kerzen immer noch nicht verkauft wurde, als target den durchschnittspreis ermitteln und leicht drüber bleiben
        #   -- so wird wenig bis gar kein gewinn gemacht, aber ein neiuer zyklus kann eher starten
        #   -- wenn dieser preis nicht erreicht wird - halten
        # green candle
        if cycle['state'] == STATE_DEAD:
            return False
        if row['close'] > row['open']:
            # the close price must be greater than the cycle start price
            if row['close'] > cycle['sell_price'] + cycle['sell_price'] / 100 * self.sell_price_factor_in_percent:
                # calc cycle stats
                if len(cycle['orders']) > 0:
                    cycle['stats'].append(self.calc_cycle_stats(line, index, row, cycle))
                # close all orders
                for order in cycle['orders']:
                    self.pf.close_order(order, row['close'], index)
                # remove all orders from cycle
                cycle['orders'] = list()
                if cycle['state'] == STATE_HOLD:
                    cycle['state'] = STATE_DEAD
                return True
        return False

    def calc_cycle_stats(self, line, index, row, cycle):
        buys = list()
        sum_orders = 0
        sum_units = 0
        average_buying_price = 0
        average_buying_costs = 0
        if len(cycle['orders']) > 0:
            for order in cycle['orders']:
                sum_units += order['units']
                sum_orders += order['units'] * order['buying_price']
                buys.append({
                    'time': str(order['index'].day) + '.' + str(order['index'].month) + '. ' + str(order['index'].hour) + 'h',
                    'price': order['buying_price']
                })
            average_buying_price = sum_orders / sum_units
            average_buying_costs = sum_orders / len(cycle['orders'])
        return {
            'cycle_start_price': cycle['start_price'],
            'average_buying_price': round(average_buying_price, self.calc_round_precision(average_buying_price)),
            'sell_price': row['close'],
            'average_buying_costs': round(average_buying_costs, self.calc_round_precision(average_buying_costs)),
            'number_of_buys': len(cycle['orders']),
            'sell_time': str(index.day) + '.' + str(index.month) + '. ' + str(index.hour) + 'h',
            'buys': json.dumps(buys),
        }

    def calc_round_precision(self, value):
        if value >= 1:
            return 2

        # get number of leading zeros after decimal point
        decimal_index = str(value).find('.')
        number_of_leading_zeros = 0
        for char in str(value)[decimal_index + 1:]:
            if char == '0':
                number_of_leading_zeros += 1
            else:
                break
        # round for 3 numbers which are not a zero
        return number_of_leading_zeros + 3

    def get_preparation_values(self):
        return {
            'name': self.get_name(),
            'indicator': self.indicator,
            'hash': hash(self)
        }

    def get_name(self):
        return self.indicator

    def __hash__(self):
        return zlib.adler32(self.get_name().encode('UTF-8')) & 0xffffffff
