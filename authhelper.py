import dbhelper

def getAuth(db, usr, key):

    db_connect = dbhelper.serverconn(db)
    cursor = db_connect.cursor()
    cursor.execute(f"""CALL `WWC_Admin`.`site_auth`('{usr}', '{key}');""")

    for row in cursor.fetchall():
        data = row

    dbhelper.db_close(db_connect)    
    return data

#getAuth(db, usr, key)