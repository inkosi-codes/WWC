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
auth_data = [] 

@app.route("/")
def default():
    return render_template('login.html')


@app.route("/authentication", methods=['POST'])
def getauth():
    db = 'WWC_Admin'
    if request.method == 'POST':
        username = request.form['InputUser']
        key = request.form['InputPassword']
   
    auth_data.append(appauth.getAuth(db,username,key))

    return redirect('home', code=302)

@app.route("/home")
def index():
    if auth_data[0][0] == 1:
        return render_template('index.html',data=auth_data[0][1])
    else:
        return redirect('/',code=302)
        
    
        
if __name__ == '__main__':
    app.run(debug=True)