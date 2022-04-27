"""
    Reconnect / Refresh Access Token: https://community.tradovate.com/t/sequence-numbers/4102/4
    Contract Month Codes: https://www.cmegroup.com/month-codes.html
    Automated Orders: https://api.tradovate.com/#section/Automated-Orders
"""
import hashlib
import json

import pandas as pd
import math
import os.path
import time

import asyncio
import websockets
from binance.client import Client
from datetime import timedelta, datetime, date
from dateutil import parser
import yfinance as yf
from pandas_finance import Equity

# API
import definitions
from api_key import *
from db import DB

from tradovate.tradovate_api_client import Client as TradovateClient
from tradovate.tradovate_api_client import AuthenticatedClient
from tradovate.tradovate_api_client.api.accounting import account_list
from tradovate.tradovate_api_client.api.authentication import access_token_request
from tradovate.tradovate_api_client.api.users import user_list, sync_request
from tradovate.tradovate_api_client.models import AccessTokenRequest


INITIAL_BODY = {
    "symbol": definitions.SYMBOL,
    "chartDescription": {
        "underlyingType": "Tick",
        "elementSize": 1,
        "elementSizeUnit": "UnderlyingUnits",
        "withHistogram": False,
    },
    "timeRange": {
        # keep the added timedelta of 3 days in mind - asFarAsTimestamp must be more than 3 days ago
        "asFarAsTimestamp": "2022-04-23T00:00Z",
        "closestTimestamp": "2022-04-26T15:00Z",
        # "closestTickId": 123,
        # "asMuchAsElements": 66
    }
}
REQUESTS = []
HISTORICAL_ID = None
REALTIME_ID = None
OLDEST_TICK_TIMESTAMP = None


async def get_tradovate_data():

    tradovate_client = TradovateClient(base_url=definitions.TRADOVATE_URL)

    access_token_response = access_token_request.sync(
        client=tradovate_client,
        json_body=AccessTokenRequest(
            name=TRADOVATE_NAME,
            password=TRADOVATE_API_PW,
            app_id=TRADOVATE_APP_ID,
            app_version=definitions.APP_VERSION,
            device_id=TRADOVATE_API_DEVICE_ID,
            cid=TRADOVATE_API_CID,
            sec=TRADOVATE_API_SECRET
        )
    )
    access_token = access_token_response.access_token
    authenticated_client = AuthenticatedClient(
        base_url=definitions.TRADOVATE_URL,
        token=access_token
    )

    account_list_response = account_list.sync(client=authenticated_client)
    #
    # user_list_response = user_list.sync(client=authenticated_client)

    await open_ws(access_token)


async def heartbeat(websocket):
    while True:
        await asyncio.sleep(2.5)
        await websocket.send('[]')


async def get_ticks(websocket, body=None):
    global REQUESTS
    global INITIAL_BODY
    REQUESTS.append('get_ticks')
    if body is None:
        body = INITIAL_BODY
    await asyncio.sleep(1)
    print(f"md/getChart\n{len(REQUESTS)}\n\n{json.dumps(body)}")
    await websocket.send(f"md/getChart\n{len(REQUESTS)}\n\n{json.dumps(body)}")
    while True:
        await asyncio.sleep(30)


async def receive(websocket):
    while True:
        response = await websocket.recv()
        print(f"receive: {response}")

        if response:
            response_type = response[0]
            if response_type == "h":
                print("\tws -- MD -- heartbeat -- ")
            elif response_type == "c":
                print("ws -- close message -- [{0}]".format(response))
            elif response_type == "a":
                asyncio.create_task(handle_data(websocket, response))


async def handle_data(websocket, response):
    global HISTORICAL_ID
    global REALTIME_ID
    global REQUESTS
    global OLDEST_TICK_TIMESTAMP

    jmsg = json.loads(response[2:-1])
    event_msg = jmsg.get('e')
    response_status = jmsg.get('s')
    if response_status is not None:
        if response_status == 200:
            response_id = jmsg['i']
            request_type = REQUESTS[int(response_id) - 1]
            HISTORICAL_ID = jmsg.get('historicalId')
            REALTIME_ID = jmsg.get('realtimeId')
        else:
            print("got response ERROR --\n{0}\n".format(jmsg))

    if event_msg is not None:
        charts = jmsg.get('d', {}).get('charts', {})

        if charts is not None:
            for chart in charts:

                if chart.get('eoh'):
                    as_far_as_timestamp = pd.to_datetime(INITIAL_BODY['timeRange']['asFarAsTimestamp']).to_pydatetime()
                    # timedelta is needed because the datetime has milliseconds and could be outside the trading hours
                    # so we have to add simply some days to the farthest datetime
                    if (as_far_as_timestamp + timedelta(days=3)).timestamp() < OLDEST_TICK_TIMESTAMP.timestamp():
                        body = INITIAL_BODY
                        body['timeRange']['closestTimestamp'] = \
                            (OLDEST_TICK_TIMESTAMP + timedelta(seconds=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
                        asyncio.create_task(get_ticks(websocket, body))
                    else:
                        print('************* finished *************')
                        return
                else:

                    # todo: testing
                    # Writing to file
                    with open("tmp/tick_data.txt", "a") as file1:
                        # Writing data to a file
                        file1.write(response)
                        file1.write("\n")

                    base_price = chart.get('bp')
                    base_timestamp = chart.get('bt')
                    tick_size = chart.get('ts')
                    ticks = chart.get('tks')

                    if ticks is not None:
                        for ix, tick in enumerate(ticks):

                            timestamp = pd.to_datetime(base_timestamp + tick['t'], unit='ms').to_pydatetime()
                            if OLDEST_TICK_TIMESTAMP is None or OLDEST_TICK_TIMESTAMP > timestamp:
                                OLDEST_TICK_TIMESTAMP = timestamp
                    #         price = base_price + tick['p']
                    #         bid_price = 0
                    #         ask_price = 0
                    #         if tick['bs']:
                    #             bid_price = (base_price + tick['b'])
                    #         if tick['as']:
                    #             ask_price = (base_price + tick['a'])
                    #
                    #         result_list = [
                    #             tick['id'],
                    #             definitions.SYMBOL,
                    #             str(timestamp),
                    #             float(price),
                    #             float(tick['s']),
                    #             float(bid_price),
                    #             float(ask_price),
                    #             float(tick['bs']),
                    #             float(tick['as']),
                    #         ]
                    #         result_hash = get_hash_from_list(result_list)
                    #         result_list += [result_hash]
                    #
                    #         db = DB().db
                    #         db_cursor = db.cursor(dictionary=True)
                    #         db_cursor.execute(
                    #             "select * from ticks where `hash` = %s",
                    #             [result_hash]
                    #         )
                    #         db_cursor.fetchone()
                    #         if db_cursor.rowcount == -1:
                    #             db_cursor = db.cursor()
                    #             db_cursor.execute(
                    #                 "insert into ticks ("
                    #                     "`tick_id`,"
                    #                     "`symbol`,"
                    #                     "`timestamp`,"
                    #                     "`tick_price`,"
                    #                     "`tick_volume`,"
                    #                     "`bid_price`,"
                    #                     "`ask_price`,"
                    #                     "`bid_size`,"
                    #                     "`ask_size`,"
                    #                     "`hash`"
                    #                 ") values ("
                    #                     "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s"
                    #                 ")", tuple(result_list))
                    #             db.commit()


async def open_ws(access_token):
    global REQUESTS
    async with websockets.connect(definitions.TRADOVATE_WEBSOCKET_URL) as websocket:

        receive_task = asyncio.create_task(receive(websocket), name='receive')

        REQUESTS.append('authorize')
        await websocket.send(f"authorize\n{len(REQUESTS)}\n\n{access_token}")

        asyncio.create_task(heartbeat(websocket), name='heartbeat')
        asyncio.create_task(get_ticks(websocket), name='ticks')
        # asyncio.create_task(get_chart(websocket), name='chart')
        # asyncio.create_task(subscribe_quote(websocket), name='subscribe_quote')

        await asyncio.Future()  # run forever


def get_hash_from_list(hashable_list):
    return hashlib.md5(b'' + json.dumps(hashable_list).encode('UTF-8')).hexdigest()


async def main():
    print('run ws')
    await get_tradovate_data()


asyncio.run(main())
