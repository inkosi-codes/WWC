import dbhelper

def getPayData(db, usr):

    db_connect = dbhelper.serverconn(db)
    cursor = db_connect.cursor()
    cursor.execute(f"""<here>""")

    for row in cursor.fetchall():
        rdata = row

    dbhelper.db_close(db_connect)    
    return rdata