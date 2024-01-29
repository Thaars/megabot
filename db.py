import json
from datetime import datetime

import mysql.connector
import db_credentials


# https://www.edureka.co/blog/python-database-connection/#MySQL
class DB:
    def __init__(self):
        self.connection = self.connect_db()
        self.create_tables()

    def disconnect(self):
        # Cursor und Verbindung schließen
        self.connection.cursor.close()
        self.connection.close()

    def connect_db(self):
        db = mysql.connector.connect(
            host=db_credentials.MYSQL_HOST,
            # port=tunnel.local_bind_port,
            user=db_credentials.MYSQL_USER,
            password=db_credentials.MYSQL_PASS,
            database=db_credentials.MYSQL_DB
        )

        return db

    def create_tables(self):
        self.connection.ping(reconnect=True)
        db_cursor = self.connection.cursor(buffered=True)
        db_cursor.execute(f"create database if not exists `{db_credentials.MYSQL_DB}`")

        db_cursor.execute("create table if not exists results("
                          "`id` int(10) auto_increment primary key,"
                          "`general_hash` varchar(250),"
                          "`exact_hash` varchar(250),"
                          "`symbol` varchar(250),"
                          "`strategy` varchar(250),"
                          "`strategy_config` text,"
                          "`timeframe` varchar(250),"
                          "`trade_type` varchar(250),"
                          "`days` varchar(250),"
                          "`performance` decimal(10,2),"
                          "`market_performance` decimal(10,2),"
                          "`winning` tinytext,"
                          "`losing` tinytext,"
                          "`winners` longtext,"
                          "`losers` longtext,"
                          "`largest_loser_series` longtext,"
                          "`starts_at` timestamp,"
                          "`ends_at` timestamp,"
                          "`ticks` decimal(15,6),"
                          "`winning_ticks` decimal(15,6),"
                          "`losing_ticks` decimal(15,6),"
                          "`tick_cash` decimal(15,6),"
                          "`lowest_tick_cash` decimal(15,6),"
                          "`max_stop_loss_amount` decimal(15,6),"
                          "`max_stop_loss_ticks` decimal(15,6),"
                          "`max_stop_loss_margin` decimal(15,6),"
                          "`tick_size` decimal(8,4),"
                          "`tick_value` decimal(8,4),"
                          "`trading_breaks` text,"
                          "`commission_factor` decimal(8,6),"
                          "`commission_value` decimal(8,6),"
                          "`start_cash` decimal(10,2),"
                          "`end_cash` decimal(10,2),"
                          "`created_at` timestamp default CURRENT_TIMESTAMP,"
                          "INDEX performance_index(`performance`),"
                          "INDEX market_performance_index(`market_performance`)"
                          ");")

        db_cursor.execute("create table if not exists minute_bars("
                          "`id` int(10) auto_increment primary key,"
                          "`symbol` varchar(250),"
                          "`timestamp` timestamp,"
                          "`open` decimal(12,4),"
                          "`high` decimal(12,4),"
                          "`low` decimal(12,4),"
                          "`close` decimal(12,4),"
                          "`up_volume` decimal(12,4),"
                          "`down_volume` decimal(12,4),"
                          "`up_ticks` decimal(12,4),"
                          "`down_ticks` decimal(12,4),"
                          "`bid_volume` decimal(12,4),"
                          "`offer_volume` decimal(12,4),"
                          "`hash` varchar(250),"
                          "INDEX hash_index(`hash`),"
                          "INDEX symbol_index(`symbol`),"
                          "INDEX timestamp_index(`timestamp`),"
                          "INDEX symbol_timestamp_index(`symbol`,`timestamp`)"
                          ");")

        db_cursor.execute("create table if not exists ticks("
                          "`id` int(10) auto_increment primary key,"
                          "`tick_id` int(10),"
                          "`symbol` varchar(250),"
                          "`timestamp` timestamp(3),"
                          "`tick_price` decimal(12,4),"
                          "`tick_volume` decimal(12,4),"
                          "`bid_price` decimal(12,4),"
                          "`ask_price` decimal(12,4),"
                          "`bid_size` decimal(12,4),"
                          "`ask_size` decimal(12,4),"
                          "`hash` varchar(250),"
                          "INDEX tick_id_index(`tick_id`),"
                          "INDEX hash_index(`hash`),"
                          "INDEX symbol_index(`symbol`),"
                          "INDEX timestamp_index(`timestamp`),"
                          "INDEX symbol_timestamp_index(`symbol`,`timestamp`)"
                          ");")

        db_cursor.execute("create table if not exists ai_models("
                          "`id` int(10) auto_increment primary key,"
                          "`symbol` varchar(250),"
                          "`timeframe` varchar(250),"
                          "`columns` text,"
                          "`layers` int,"
                          "`neurones` int,"
                          "`epochs` int,"
                          "`shap` text,"
                          "`early_stopped_epoch` int null,"
                          "`training_starts_at` timestamp(3),"
                          "`training_ends_at` timestamp(3),"
                          "`hash` varchar(250)"
                          ");")

        db_cursor.execute("create table if not exists ai_results("
                          "`id` int(10) auto_increment primary key,"
                          "`symbol` varchar(250),"
                          "`timeframe` varchar(250),"
                          "`model_id` int(10),"
                          "`model_data` longtext,"
                          "`starts_at` timestamp(3),"
                          "`ends_at` timestamp(3),"
                          "`total_predictions_count` int(10),"
                          "`true_predictions_count` int(10),"
                          "`true_predictions_percent` decimal(7,4),"
                          "`true_on_bullish_percent` decimal(7,4),"
                          "`true_on_bearish_percent` decimal(7,4)"
                          ");")
        db_cursor.close()

    def get_model_from_db(self, model_hash):
        self.connection.ping(reconnect=True)
        db_cursor = self.connection.cursor(buffered=True, dictionary=True)
        db_cursor.execute(
            "select * from ai_models where `hash` = %s;",
            [
                model_hash,
            ]
        )
        result = db_cursor.fetchone()
        db_cursor.close()
        if result:
            return result
        return None

    def save_model_to_db(self, config, train_start_time, train_end_time, model_hash, early_stopping_epoch=None,
                         average_shap_json=None):
        self.connection.ping(reconnect=True)
        db_cursor = self.connection.cursor(buffered=True)
        db_cursor.execute("insert into ai_models("
                                "`symbol`,"
                                "`timeframe`,"
                                "`columns`,"
                                "`layers`,"
                                "`neurones`,"
                                "`epochs`,"
                                "`early_stopped_epoch`,"
                                "`shap`,"
                                "`training_starts_at`,"
                                "`training_ends_at`,"
                                "`hash`"
                              ") values("
                                "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
                              ")", (
                                config['symbol'],
                                config['timeframe'],
                                json.dumps(config['columns']),
                                config['layers'],
                                config['neurones'],
                                config['epochs'],
                                early_stopping_epoch,
                                average_shap_json,
                                self.get_mysql_datetime_from_datetimeindex(train_start_time),
                                self.get_mysql_datetime_from_datetimeindex(train_end_time),
                                model_hash
                              ))
        self.connection.commit()
        last_id = db_cursor.lastrowid
        db_cursor.close()
        return last_id

    def save_predictions_to_db(self, config, test_start_time, test_end_time, model_hash, total_predictions_count,
                               true_predictions_count, true_predictions_percent, true_on_bullish_percent,
                               true_on_bearish_percent):
        self.connection.ping(reconnect=True)
        model_from_db = self.get_model_from_db(model_hash)
        db_cursor = self.connection.cursor(buffered=True)
        db_cursor.execute("insert into ai_results("
                                "`symbol`,"
                                "`timeframe`,"
                                "`model_id`,"
                                "`model_data`,"
                                "`starts_at`,"
                                "`ends_at`,"
                                "`total_predictions_count`,"
                                "`true_predictions_count`,"
                                "`true_predictions_percent`,"
                                "`true_on_bullish_percent`,"
                                "`true_on_bearish_percent`"
                              ") values("
                                "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
                              ")", (
                                config['symbol'],
                                config['timeframe'],
                                model_from_db['id'],
                                json.dumps(model_from_db, default=self.default_json_converter),
                                self.get_mysql_datetime_from_datetimeindex(test_start_time),
                                self.get_mysql_datetime_from_datetimeindex(test_end_time),
                                int(total_predictions_count),
                                int(true_predictions_count),
                                float(round(true_predictions_percent, 2)),
                                float(round(true_on_bullish_percent, 2)),
                                float(round(true_on_bearish_percent, 2))
                              ))
        self.connection.commit()
        db_cursor.close()

    def get_mysql_datetime_from_datetimeindex(self, datetimeindex):
        datetime_obj = datetime.strptime(str(datetimeindex), "%Y-%m-%d %H:%M:%S%z")
        return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

    # Funktion, die festlegt, wie nicht-serialisierbare Objekte behandelt werden sollen
    def default_json_converter(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        raise TypeError("Object of type '%s' is not JSON serializable" % type(o).__name__)

