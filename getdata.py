import dbhelper


db = 'WorldWideCompany'

def getPayData(usr):
    db_connect = dbhelper.serverconn(db)
    cursor = db_connect.cursor()
    cursor.execute(f"""CALL `WorldWideCompany`.`getEmployeePay`('{usr}');""")

    for row in cursor.fetchall():
        data = row

    dbhelper.db_close(db_connect)    
    return data

def getBenefitsData(usr):
    db_connect = dbhelper.serverconn(db)
    cursor = db_connect.cursor()
    cursor.execute(f"""CALL `WorldWideCompany`.`getEmployeeBenefits`('{usr}');""")

    for row in cursor.fetchall():
        data = row

    dbhelper.db_close(db_connect)    
    return data

def getProfileData(usr):
    db_connect = dbhelper.serverconn(db)
    cursor = db_connect.cursor()
    cursor.execute(f"""CALL `WorldWideCompany`.`getEmployeeProfile`('{usr}');""")

    for row in cursor.fetchall():
        data = row

    dbhelper.db_close(db_connect)    
    return data     