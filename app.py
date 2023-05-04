import auth
import getdata
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
#auth_data = [] 

@app.route("/")
def default():
    return redirect(url_for('usrlogin'))

@app.route("/login")
def usrlogin():
    return render_template("login.html")

@app.route("/home")
def homepage():
    benefits = getdata.getBenefitsData(session['username'])
    plan = benefits[0]
    plan_amt = benefits[1]

    pay = getdata.getPayData(session['username'])

    index_to_remove = 0
    pay = pay[:index_to_remove] + pay[index_to_remove+1:]

    return render_template("index.html", data = session['username'],pdata=pay,plan=plan,bamt=plan_amt)

@app.route("/EmployeeProfile")
def profile():
    edata = getdata.getProfileData(session['username'])

    empid = edata[0]
    fname = edata[1]
    lname = edata[2]
    dob = edata[3]
    streetadd = edata[4]
    city_state = edata[5]
    country = edata[6]
    s_date = edata[7]
    office = edata[8]
    dept = edata[9]
    comp = edata[10]

    return render_template("profile.html", empid=empid, fname=fname, lname=lname, dob=dob, streetadd=streetadd, city_state=city_state, country=country, s_date=s_date, office=office, dept=dept, comp=comp)

@app.route("/logout")
def usrlogout():
    session.clear()

    return redirect(url_for('usrlogin'))

@app.route("/authentication", methods=("GET", "POST"))
def usrauth():
    username = request.form['InputUser']
    key = request.form['InputPassword']
    login_info = auth.init_login(username,key)
    token = login_info[0]
    usrname = login_info[1]

    if token == 0:
        return redirect(url_for('default'))
    elif token == 1:
        session['username'] = usrname
        return redirect(url_for('homepage'))
        
if __name__ == '__main__':
    app.run(debug=True)