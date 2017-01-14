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
        if 'student' in session:
            return render_template('home.html', loggedIn="Logout", teach = False)
        return render_template('home.html', loggedIn="Logout", teach = True)
    return redirect(url_for('login'))

@app.route('/auth/', methods = ["GET","POST"])
def auth():
    print 'start'
    ## register
    #print request.form
    if 'register' in request.form:
        if (request.form['user'] == '' or request.form['pass'] == ''):
            return render_template('login.html', msg = 'please fill in all forms of info', register = False)
        elif (database.logincheck(request.form['user'], True) or (database.logincheck(request.form['user'], False))):
            return render_template('login.html', msg = 'username taken, please choose a new one', register = False)
        else:
            name = request.form['name']
            user0 = request.form['user']
            pass0 = hashp(request.form['pass'])
            if (request.form['person']  == 'teacher'):
                database.addteacher(user0,pass0,name,database.gettid())
            else:
                database.addstudent(user0,pass0,name,database.getsid())
            return render_template('login.html', msg = 'new account created', register = True)
    ## login
    else:
        if not database.logincheck(request.form['user'], True) or database.logincheck(request.form['user'], False):
            return render_template('login.html', msg = 'username does not exist', register = False)
        elif (database.gethash(request.form['user']) == hashp(request.form['pass'])):
            user1 = request.form['user']
            session['user'] = user1
            if request.form['person']  == 'teacher':
                session['teach'] = True;
            else:
                session['teach'] = False;
            return redirect(url_for('home'))
        else:
            return render_template('login.html', msg = 'incorrect username and password combination', register = False)

def hashp(password):
    return hashlib.sha512(password).hexdigest()

#dev only
@app.route('/seating/')
def seating():
    htmlString = seat.seatHtml(3,5)
    return render_template('seat.html', seats=htmlString)

if __name__ == '__main__':
    app.debug = True
    app.run()
