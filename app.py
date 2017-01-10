from flask import Flask, redirect, request, render_template, session, url_for
import os
#from utils import database
import hashlib


app = Flask(__name__)

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
        return render_template('home.html')
    return redirect(url_for('login'))

@app.route('/auth/')
def auth():
## register
    #print request.form
    if 'register' in request.form:
        if (request.form['user'] == '' or request.form['pass'] == ''):
            return render_template('login.html', msg = 'please fill in all forms of info')
        elif (db_builder.check(request.form['user'])):
            return render_template('login.html', msg = 'username taken, please choose a new one')
        else:
            user0 = request.form["username"]
            pass0 = hashp(request.form["password"])
            db_builder.add_user(user0,pass0)
            flash("new account created")
            return redirect(url_for("login"))
    ## login
    else:
        if (not (db_builder.check(request.form['username']))):
            flash("username does not exist")
            return redirect(url_for("login"))
        elif (db_builder.get_hash(request.form['username']) == hashp(request.form['password'])):
            user1 = request.form['username']
            session['username'] = user1
            print '!SESSION_STATUS: ' + session['username']
            return redirect(url_for("home"))
        else:
            flash("incorrect username and password combination")
    return redirect(url_for("login"))

#dev only
@app.route('/seat')
def seat():
    return render_template('seat.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
