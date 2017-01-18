# creating databases: teachers(), students(), classes(), grades()

import sqlite3   #enable control of an sqlite database

#f="utils/data/database.db"

#################################################################################################
def teachers():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS teachers (username TEXT, password TEXT, name TEXT, id INTEGER)"
    c.execute(q)    #run SQL query
    db.commit()


#################################################################################################
def students():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS students (username TEXT, password TEXT, name TEXT, id INTEGER)"
    c.execute(q)    #run SQL query
    db.commit()


##################################################################################################
def classes():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS classes (classid INTEGER, teacherid INTEGER, studentid INTEGER, name TEXT, period INTEGER, seatid INTEGER, glasses BOOLEAN, row INTEGER, col INTEGER)"
    c.execute(q)
    db.commit()


##################################################################################################
def periods():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS periods (classid INTEGER, teacherid INTEGER, period INTEGER, rows INTEGER, cols INTEGER)"
    c.execute(q)
    db.commit()


##################################################################################################
def grades():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS grades (classid INTEGER, studentid INTEGER, grade INTEGER, assignmentid INTEGER, assignmentname TEXT)"
    c.execute(q)
    db.commit()


##################################################################################################

# checks if account username is found
def logincheck(username, teacher):
    #print "called"
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    #print "connected"
    c = db.cursor()
    if(teacher):
        q = "SELECT username FROM teachers"
        d = c.execute(q)

        for n in d:
            if(n[0] == username):
                return True
    else:
        q = "SELECT username FROM students"
        d = c.execute(q)

        for n in d:
            if(n[0] == username):
                return True
    db.close()
    return False

# ret True if successfully added, False if username already exists
def addteacher(username,password,name,id):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(not logincheck(username,True)):
        c = db.cursor()
        q = "INSERT INTO teachers VALUES ('"+username+"','"+password+"','"+name+"',"+str(id)+");"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False

# ret True if successfully added, False if username already exists
def addstudent(username,password,name,id):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(not logincheck(username,False)):
        c = db.cursor()
        q = "INSERT INTO students VALUES ('"+username+"','"+password+"','"+name+"',"+str(id)+");"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False

#addstudent("nicole","nicole","nicole",0)

def classcheck(classid, studentid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT * FROM classes WHERE classid = "+str(classid)
    d = c.execute(q)
    for a in d:
        if (a[2]==studentid):
            return False
    return True


#"CREATE TABLE IF NOT EXISTS classes (classid INTEGER, teacherid INTEGER, studentid INTEGER, name TEXT, period INTEGER, seatid INTEGER, glasses BOOLEAN, row INTEGER, col INTEGER)"
# add student to class
def addtoclass(classid, teacherid, studentid, name, period, seatid, glasses, row, col):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(classcheck(classid,studentid)):
        c = db.cursor()
        q = "INSERT INTO classes VALUES ('"+str(classid)+"','"+str(teacherid)+"','"+str(studentid)+"','"+name+"','"+str(period)+"','"+str(seatid)+"','"+str(glasses)+"','"+str(row)+"','"+str(col)+"');"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False

def periodcheck(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT * FROM periods WHERE classid = "+str(classid)
    d = c.execute(q)
    for a in d:
        if (a[0]==classid):
            return False
    return True

# add a secret code!!!!
# "CREATE TABLE IF NOT EXISTS periods (classid INTEGER, teacherid INTEGER, period INTEGER, rows INTEGER, cols INTEGER)"
# add a class (period)
def addperiod(classid,teacherid,period,rows,cols):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(periodcheck(classid)):
        c = db.cursor()
        q = "INSERT INTO periods VALUES ('"+str(classid)+"','"+str(teacherid)+"','"+str(period)+"','"+str(rows)+"','"+str(cols)+"');"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False




# grades (classid INTEGER, studentid INTEGER, grade INTEGER, assignmentid INTEGER, assignmentname TEXT)"
def addgrade(classid, studentid, grade, assignmentid, assignmentname):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(isinstance(grade,int)):
        c = db.cursor()
        q = "INSERT INTO grades VALUES ('"+str(classid)+"','"+str(studentid)+"','"+str(grade)+"','"+str(assignmentid)+"',"+str(assignmentname)+");"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False


def gethash(username, teacher):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    if (teacher):
        m = c.execute("SELECT * FROM teachers")
        for a in m:
            if a[0]==username:
                db.close()
                return a[1]
    else:
        m = c.execute("SELECT * FROM students")
        for a in m:
            if a[0]==username:
                db.close()
                return a[1]
    db.close()
    return None

def printstudents():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM students")
    for a in m:
        print a

def printteachers():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM teachers")
    for a in m:
        print a

#printstudents()

#addperiod(00,-1,2,6,5)
#addtoclass(00, -1, 14, "nikkita", 2, 4, False, 3, 4)

def printclass():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM classes")
    for a in m:
        print a

def printperiods():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods")
    for a in m:
        print a

printclass()
printperiods()

# get next teacher id
def gettid():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM teachers")
    id = -1
    for a in m:
        id = a
    if(id==-1):
        return id
    else:
        return id[3]-1

# get next student id
def getsid():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM students")
    id = 1
    for a in m:
        id = a
    if(id==1):
        return id
    else:
        return id[3]+1

#print getsid()
#print gettid()

# returns {studentid: seatid}
def getstudents(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM classes WHERE classid = "+str(classid))
    j = {}
    for a in m:
        j[a[2]]=a[5]
    return j

# get rows and cols in a class
def getdims(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods WHERE classid = "+str(classid))
    j = []
    for a in m:
        j.append([a[3],a[4]])
    return j

def go():
    teachers()
    students()
    periods()
    classes()
    grades()

#go()

def close():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    db.commit() #save changes
    db.close()  #close database

close()

# TO DO
# add class name to periods table
# wipe out database and reset
