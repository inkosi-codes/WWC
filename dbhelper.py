import pymysql
from pathlib import Path

def serverconn(db_conn):
    conn = pymysql.connect(
    host= 'dsba.ccp7whzua9lm.us-east-2.rds.amazonaws.com', 
    port = 3306,
    user = '', 
    password = '',
    db = db_conn,
        
    )

    return (conn)

def db_close(conn):
    conn.close

    return ('Connection Closed')
    
