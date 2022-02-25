import mysql.connector
import definitions


# https://www.edureka.co/blog/python-database-connection/#MySQL
class DB:
    def __init__(self):
        self.db = self.connect_db()

    def connect_db(self):
        db = mysql.connector.connect(
            host=definitions.MYSQL_HOST,
            user=definitions.MYSQL_USER,
            passwd=definitions.MYSQL_PASS
        )
        db_cursor = db.cursor()
        db_cursor.execute(f"create database if not exists `{definitions.MYSQL_DB}`")

        db = mysql.connector.connect(
            host=definitions.MYSQL_HOST,
            user=definitions.MYSQL_USER,
            passwd=definitions.MYSQL_PASS,
            database=definitions.MYSQL_DB
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
                          "`starts_at` timestamp,"
                          "`ends_at` timestamp,"
                          "`ticks` decimal(15,6),"
                          "`winning_ticks` decimal(15,6),"
                          "`losing_ticks` decimal(15,6),"
                          "`tick_cash` decimal(15,6),"
                          "`lowest_tick_cash` decimal(15,6),"
                          "`tick_size` decimal(8,4),"
                          "`tick_value` decimal(8,4),"
                          "`trading_breaks` text,"
                          "`commission` decimal(8,6),"
                          "`start_cash` decimal(10,2),"
                          "`end_cash` decimal(10,2),"
                          "`created_at` timestamp default CURRENT_TIMESTAMP,"
                          "INDEX performance_index(`performance`),"
                          "INDEX market_performance_index(`market_performance`)"
                          ");")

        return db
