import pymysql
from pathlib import Path

def serverconn(db_conn):
    conn = pymysql.connect(
    host= '13.58.92.155', 
    port = 3306,
    user = 'adminaws', 
    password = 'FMmZl9xfAHHrFwZifZgk',
    db = db_conn,
        
    )

    return (conn)

def db_close(conn):
    conn.close

    return ('Connection Closed')
    
