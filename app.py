import hashlib
import appauth
import dbhelper
from flask import Flask, request, render_template, session, redirect, url_for



#-----------------------------------------------#
#              Initialize the app               #
#-----------------------------------------------#
app = Flask(__name__, static_folder="templates/static")
app.secret_key = '*55ro8LThAD-po#i'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1


#-----------------------------------------------#
#                   Routes                      #
#-----------------------------------------------#


@app.route("/")
def default():
    return render_template('login.html')


@app.route("/authentication", methods=['POST'])
def getauth():
    db = 'WWC_Admin'
    if request.method == 'POST':
        username = request.form['InputUser']
        key = request.form['InputPassword']
        
    r_data = appauth.getAuth(db,username,key)

    return redirect('home', code=302)

@app.route("/home")
def index():
    phash = 'thisismypassword'
    hashlib.md5(phash.encode())
    return render_template('index.html',data=phash)
    
        

if __name__ == '__main__':
    app.run(debug=True)