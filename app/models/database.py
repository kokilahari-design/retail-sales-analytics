# pymysql - load the MySQL connector library so Python program can talk to MySQL database.
import pymysql
from app.config import DB_CONFIG

def get_connection():

    connection = pymysql.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        cursorclass=pymysql.cursors.DictCursor )

    return connection
