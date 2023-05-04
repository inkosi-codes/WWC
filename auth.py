import authhelper

def init_login(usr,key):
    db = 'WWC_Admin'
    l_info = authhelper.getAuth(db,usr,key)

    return l_info

#def logout():
