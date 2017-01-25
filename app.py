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
    return render_template('login.html',register='blank',loggedIn=False)

@app.route('/logoutJ/')
def logoutJ():
    if 'user' in session:
        session.pop('user')
        session.pop('teach')
        return 'Success! Logged out'
    return 'Not logged in'


@app.route('/home/')
def home():
    if 'user' in session:
        classHTML = ""
        cL = ""
        if session['teach']:
            tid = database.getteacherid(session['user'])
            l = database.getclassest(tid)
            for i in l:
                classHTML += '<a type="button" class="btn btn-default btn-lg btn-block" href="/seating/'+str(i)+'">'+str(i)+'</a><br>'
                cL += "<p> Period " + str(i) + "</p>"
            return render_template('home.html', teach = session['teach'], classes=classHTML, classList = cL, loggedIn=True,teacher=True)
        else:
            sid = database.getstudentid(session['user'])
            l = database.getclassess(sid)
            for i in l:
                cL += str(i) + '<br>'
            return render_template('home.html', teach = session['teach'], classes=classHTML, classList = cL, loggedIn=True,teacher=False)
    return redirect(url_for('login'))

@app.route('/auth/', methods = ["GET","POST"])
def auth():
    ## register
    #print request.form
    if 'register' in request.form:
        if (request.form['user'] == '' or request.form['pass'] == '' or request.form['name'] == '' or request.form['pass2'] == '' or (not "person" in request.form)):
            return render_template('login.html', msg = 'please fill in all forms of info', register = False, loggedIn=False)
        elif (database.logincheck(request.form['user'].lower(), True) or (database.logincheck(request.form['user'].lower(), False))):
           return render_template('login.html', msg = 'username taken, please choose a new one', register = False, loggedIn=False)
        elif (request.form['pass'] != request.form['pass2']):
            return render_template('login.html', msg = 'passwords do not match',register = False, loggedIn=False)
        else:
            name = request.form['name']
            user0 = request.form['user'].lower()
            pass0 = hashp(request.form['pass'])
            if (request.form['person']  == 'teacher'):
                database.addteacher(user0,pass0,name,database.gettid())
            else:
                if 'glasses' in request.form:
                    database.addstudent(user0,pass0,name,database.getsid(),1)
                else:
                    database.addstudent(user0,pass0,name,database.getsid(),0)
            return render_template('login.html', msg = 'new account created', register = True, loggedIn=False)
                    ## login
    else:
        user1 = request.form['userl'].lower()
        passw = request.form['passl']
        #print request.form

        if (user1 == '' or passw == '' or len(request.form) == 7): #looking for person1 gave messed up results, kind of a copout here
            return render_template('login.html', msg = 'please fill in all forms of info', register = False, loggedIn=False)
        
        if request.form['personl']  == 'teacher':
            session['teach'] = True
        else:
            session['teach'] = False
        teacher = session['teach']

        if (teacher):
            if not database.logincheck(user1, True):
                return render_template('login.html', msg = 'username does not exist', register = False, loggedIn=False)
            elif database.gethash(user1, True) == hashp(passw):
                session['user'] = user1
                return redirect(url_for('home'))
        else:
            if not database.logincheck(user1, False):
                return render_template('login.html', msg = 'username does not exist', register = False, loggedIn=False)
            elif database.gethash(user1, False) == hashp(passw):
                session['user'] = user1
                return redirect(url_for('home'))
        return render_template('login.html', msg = 'incorrect username and password combination', register = False, loggedIn=False)

def hashp(password):
    return hashlib.sha512(password).hexdigest()

@app.route('/seating/<int:cid>')
def seating(cid):
    if 'teach' in session:
        htmlString = seat.seatHtml(cid);
        return render_template('seat.html', seats=htmlString, loggedIn = True, cid = cid)
    else:
        return redirect(url_for('home'))

@app.route('/changeseat/')
def changeseat():
    print "start"
    cid = request.args.get('cid')
    sid = request.args.get('sid')
    seatid = request.args.get('seatid')
    return seat.setSeat(cid,sid,seatid)

@app.route('/checkClass/', methods = ["GET"])
def check():
    if 'user' not in session:
        return redirect(url_for('home'))
    cid = request.args.get("secretkey")
    if not intCheck(cid) or not database.periodcheck(cid):
        return 'Class does not exist'
    return adds(cid)

def adds(cid):
    if 'user' in session:
        sid = database.getstudentid(session['user'])
        if database.addtoclass(cid,sid):
            #return redirect(url_for('home'))
            return 'success'
        return 'something went wrong'
    print 'error'
    return "error"

def intCheck(s):
    try:
        int(s)
        return True
    except:
        return False


@app.route('/addt/', methods = ["GET"])
def addt():
    if (not 'user' in session):
        return redirect(url_for('home'))
    else:
        cid = classauth()
        if (cid != 0):
            cn = request.args['name']
            tid = database.getteacherid(session['user'])
            pd = request.args['pd']
            r = request.args['rows']
            c = request.args['cols']
            if database.addperiod(cid,tid,pd,r,c,cn):
                return redirect(url_for('home'))
            return render_template('newClass.html', msg="failure", loggedIn=True)
        return render_template('newClass.html', msg="failure", loggedIn=True)

@app.route('/classauth/', methods =["GET"])
def classauth():
    key = request.args.get("secretkey")
    cid = int(database.classauth(key))        
    return cid

@app.route('/absence/')
def absence():
    if 'user' in session:
        if (session['teach']):
            return render_template('absence.html',loggedIn=True,teacher=True)
        return render_template('absence.html',loggedIn=True,teacher=False)
    return redirect(url_for('home'))

@app.route('/createClass/')
def createClass():
    if (session['teach']):
        return render_template('newClass.html',loggedIn=True)
    return redirect(url_for('home'))

@app.route('/grade/')
def grade():
    if 'user' in session:
        if (session['teach']):
            return render_template('grade.html', loggedIn=True, teacher=True)
        return render_template('grade.html', loggedIn=True, teacher=False)
    return redirect(url_for('home'))
        
if __name__ == '__main__':
    app.debug = True
    app.run()
