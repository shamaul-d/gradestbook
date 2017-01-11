from flask import Flask, redirect, request, render_template, session, url_for
import os
from utils import database
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
    return render_template('login.html')

@app.route('/home/')
def home():
    if 'user' in session:
        if 'student' in session:
            return render_template('home.html', teach = False)
        return render_template('home.html', teach = True)
    return redirect(url_for('login'))

@app.route('/auth/', methods = ["GET","POST"])
def auth():
    print 'start'
    ## register
    #print request.form
    if 'register' in request.form:
        if (request.form['user'] == '' or request.form['pass'] == ''):
            return render_template('login.html', msg = 'please fill in all forms of info')
        elif (database.logincheck(request.form['user'])):
            return render_template('login.html', msg = 'username taken, please choose a new one')
        else:
            user0 = request.form['user']
            pass0 = hashp(request.form['pass'])
            database.adduser(user0,pass0, "placeholder", "placeholder", 0)
            ## what are we doing here?
            return render_template('login.html', msg = 'new account created')
    ## login
    else:
        if (not (database.logincheck(request.form['user']))):
            return render_template('login.html', msg = 'username does not exist')
        elif (database.gethash(request.form['user']) == hashp(request.form['pass'])):
            user1 = request.form['user']
            session['user'] = user1
            return redirect(url_for('home'))
        else:
            return render_template('login.html', msg = 'incorrect username and password combination')

def hashp(password):
    return hashlib.sha512(password).hexdigest()

#dev only
@app.route('/seat/')
def seat():
    return render_template('seat.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
