from flask import Flask, redirect, request, render_template, session, url_for
import os
from utils import database, seat
import hashlib


app = Flask(__name__)
app.secret_key="fakeSecretKey"

@app.route('/')
def root():
    if 'user' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/login/')
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('login.html',register='blank')

@app.route('/logoutJ/')
def logoutJ():
    print 'out'
    if 'user' in session:
        session.pop('user')
        session.pop('teach')
        return 'Success! Logged out'
    return 'Not logged in'


@app.route('/home/')
def home():
    if 'user' in session:
        return render_template('home.html', loggedIn=True, teach = session['teach'])
    return redirect(url_for('login'))

@app.route('/auth/', methods = ["GET","POST"])
def auth():
    ## register
    #print request.form
    if 'register' in request.form:
        if (request.form['user'] == '' or request.form['pass'] == ''):
            return render_template('login.html', msg = 'please fill in all forms of info', register = False)
        elif (database.logincheck(request.form['user'].lower(), True) or (database.logincheck(request.form['user'].lower(), False))):
           return render_template('login.html', msg = 'username taken, please choose a new one', register = False)
        elif (request.form['pass'] != request.form['pass2']):
            return render_template('login.html', msg = 'passwords do not match')
        else:
            name = request.form['name']
            user0 = request.form['user'].lower()
            pass0 = hashp(request.form['pass'])
            if (request.form['person']  == 'teacher'):
                database.addteacher(user0,pass0,name,database.gettid())
            else:
                database.addstudent(user0,pass0,name,database.getsid())
            return render_template('login.html', msg = 'new account created', register = True)
    ## login
    else:
        user1 = request.form['userl'].lower()
        passw = request.form['passl']

        if request.form['personl']  == 'teacher':
            session['teach'] = True
        else:
            session['teach'] = False
        teacher = session['teach']

        if (teacher):
            if not database.logincheck(user1, True):
                return render_template('login.html', msg = 'username does not exist', register = False)
            elif database.gethash(user1, True) == hashp(passw):
                session['user'] = user1
                return redirect(url_for('home'))
        else:
            if not database.logincheck(user1, False):
                return render_template('login.html', msg = 'username does not exist', register = False)
            elif database.gethash(user1, False) == hashp(passw):
                session['user'] = user1
                return redirect(url_for('home'))
        return render_template('login.html', msg = 'incorrect username and password combination', register = False)

def hashp(password):
    return hashlib.sha512(password).hexdigest()

@app.route('/seating/')
def seating():
    if 'teach' in session:
        htmlString = seat.seatHtml(3,5)
        return render_template('seat.html', seats=htmlString, loggedIn = True)
    else:
        return redirect(url_for('home'))


@app.route('/checkClass' methods = ["GET"])
def check():
    cid = request.args.get("cid")
    if not isinstance(cid,int) or not database.periodCheck(cid):
        return 'Class does not exist'
    return adds(cid)


@app.route('/addt/' methods = ["GET"])
def addt():
    cid = database.getcid()
    cn = request.form['name']
    tid = database.getteacher(session['user'])
    pd = request.form['pd']
    r = request.form['rows']
    c = request.form['cols']
    if database.addperiod(cid,cn,tid,pd,r,c):
        return 'Added!'
    return "Error!"
    

@app.route('/adds/' methods = ["GET"])
def adds(cid):
    tid = 0
    sid = 0
    nm = 0
    pd = 0
    seid = 0
    glasses = 0
    r = 0
    c = 0
    return 'Joined!'

@app.route('/absence/')
def absence():
    return render_template('absence.html')

@app.route('/createClass/')
def createClass():
    return render_template('newClass.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
