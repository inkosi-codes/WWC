import dbhelper


def getAuth(db, usr, key):
    db_connect = dbhelper.serverconn(db)
    cursor = db_connect.cursor()
    cursor.execute("""SELECT * FROM WWC_Admin.user_login_data""")

    rows = cursor.fetchall()
    #print(f'{rows}')
    return (rows)
    dbhelper.db_close(db_connect)

#getAuth()
