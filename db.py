import mysql.connector
import db_credentials


# https://www.edureka.co/blog/python-database-connection/#MySQL
class DB:
    def __init__(self):
        self.db = self.connect_db()

    def connect_db(self):
        db = mysql.connector.connect(
            host=db_credentials.MYSQL_HOST,
            user=db_credentials.MYSQL_USER,
            passwd=db_credentials.MYSQL_PASS
        )
        db_cursor = db.cursor()
        db_cursor.execute(f"create database if not exists `{db_credentials.MYSQL_DB}`")

        db = mysql.connector.connect(
            host=db_credentials.MYSQL_HOST,
            user=db_credentials.MYSQL_USER,
            passwd=db_credentials.MYSQL_PASS,
            database=db_credentials.MYSQL_DB
        )
        db_cursor = db.cursor()
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

        return db
