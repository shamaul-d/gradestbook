# PSA: new database!!! absence(classid,studentid,date) -- date=='mmddyy'

# TEACHERS
# teachers(): username|password|name|id
# addteacher(user,pass,name,id)
# getteacherid(username) -- returns tid of teacher w given username
# printteachers()

# STUDENTS/GLASSES
# students(): username|password|name|id|glasses
# getstudents(classid) -- returns dict of {studentid: seatid} in given class
# getstudentname(studentid) -- returns name of student w given studentid
# getstudentid(username) -- returns sid of teacher w given username
# checkglasses(studentid) -- returns boolean of whether student wears glasses
# printstudents()

# CLASSES/SEATS # more like "students and their classes"
# classes(): classid|teacherid|studentid|name|period|seatid|glasses|row|col
# addtoclass(classid,studentid) # SHAMAUL THIS IS FOR YOU
# aaddtoclass(classid,teacherid,studentid,name,pd,seatid,glasses,row,col)
# getclassest(tid) -- returns list of classids that the teacher has
# getclassess(sid) -- returns list of classids that the student has
# getseatless(classid) -- returns dict of {name:id} that do not have a seat yet
# changeseat(classid,studentid,seatid,row,col)
# printclass()

# PERIODS/DIMS
# periods(): classid|teacherid|period|rows|cols|classname|secretcode
# addperiod(classid,teacherid,pd,rows,cols,classname) # SHAMAUL USE THIS
# addpd(classid,teacherid,pd,rows,cols,classname,secretcode)
# getdims(classid) -- returns [rows,cols] of a class
# getsecretcode(classid) -- returns the secret code of a class
# printperiods()

# GRADES
# grades(): classid|studentid|grade|assignmentid|assignmentname
# addgrade(classid,studentid,grade,assignmentid,asignmentname)
# getgrades(sid) -- returns dictionary of {assignmentname: grade}
# getscores(assignmentid) -- returns dict of {studentid: grade} for assignment
# changegrade(classid,studentid,assignmentid,grade)
# printgrades()

# ABSENCES
# absences(): classid|studentid|date
# addabsence(classid,studentid,date) -- date is a STRING
# getabsences(classid,studentid) -- list of dates student was absent
# getabsences(classid,date) -- list of students absent on given date
# printabsences()

# MISC
# gethash(username,isteacher?) returns hashed pass
# gettid(),getsid(),getcid() -- gets next id to use
# getcode() -- gets next id to use
# go() sets up database from scratch if database has been deleted
# close() commits changes and closes db

import sqlite3, string, random

#f="utils/data/database.db"

#################################################################################################
def teachers():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS teachers (username TEXT, password TEXT, name TEXT, id INTEGER)"
    c.execute(q)    #run SQL query
    db.commit()

def students():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS students (username TEXT, password TEXT, name TEXT, id INTEGER, glasses BOOLEAN)"
    c.execute(q)    #run SQL query
    db.commit()

def classes():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS classes (classid INTEGER, teacherid INTEGER, studentid INTEGER, name TEXT, period INTEGER, seatid INTEGER, glasses BOOLEAN, row INTEGER, col INTEGER)"
    c.execute(q)
    db.commit()

def periods():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS periods (classid INTEGER, teacherid INTEGER, period INTEGER, rows INTEGER, cols INTEGER, classname TEXT, secretcode TEXT)"
    c.execute(q)
    db.commit()

def grades():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS grades (classid INTEGER, studentid INTEGER, grade INTEGER, assignmentid INTEGER, assignmentname TEXT)"
    c.execute(q)
    db.commit()

def absences():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS absences (classid INTEGER, studentid INTEGER, date TEXT)" # date is a STRING and must be formatted 'mmddyy'
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

# returns True if student is NOT in the class
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

#print classcheck(1,2)

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

##################################################################################################

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
def addstudent(username,password,name,id,glasses):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(not logincheck(username,False)):
        c = db.cursor()
        q = "INSERT INTO students VALUES ('"+str(username)+"','"+str(password)+"','"+str(name)+"',"+str(id)+","+str(glasses)+");"
        print q
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False

# add student to class
def addtoclass2(classid, teacherid, studentid, name, period, seatid, glasses, row, col):
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

def getstufffromclassid(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods WHERE classid = '"+str(classid)+"'")
    for a in m:
        return a
    
def getstufffromstudentid(studentid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM students WHERE id = '"+str(studentid)+"'")
    for a in m:
        return a    

def addtoclass(classid, studentid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(classcheck(classid,studentid)):
        c = db.cursor()
        n = getstufffromclassid(classid)
        teacherid = n[1]
        period = n[2]
        m = getstufffromstudentid(studentid)
        name = m[2]
        glasses = m[4]
        seatid = 0
        row = 0
        col = 0
        addtoclass2(classid,teacherid,studentid,name,period,seatid,glasses,row,col)
        db.commit()
        db.close()
        return True
    else:
        return False

def aaddgrade(classid, studentid, grade, assignmentid, assignmentname):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(isinstance(grade,int)):
        c = db.cursor()
        q = "INSERT INTO grades VALUES ('"+str(classid)+"','"+str(studentid)+"','"+str(grade)+"','"+str(assignmentid)+"','"+str(assignmentname)+"');"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False

def addabsence(classid,studentid,date):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(not classcheck(classid,studentid)): # if student is in class
        c = db.cursor()
        q = "INSERT INTO absences VALUES ('"+str(classid)+"','"+str(studentid)+"','"+str(assignmentname)+"');"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False

# returns False if code already in use
def codecheck(code):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods")
    for a in m:
        if(periods[6]==code):
            return False
    return True

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def getcode():
    check = False
    while(check==False):
        code = id_generator()
        if(codecheck(code)):
            check = True
            return code

def getsecretcode(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods WHERE classid = "+str(classid))
    for a in m:
        return a[6]
    
def addpd(classid,teacherid,period,rows,cols,classname,secretcode):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(periodcheck(classid)):
        c = db.cursor()
        q = "INSERT INTO periods VALUES ('"+str(classid)+"','"+str(teacherid)+"','"+str(period)+"','"+str(rows)+"','"+str(cols)+"','"+classname+"','"+str(secretcode)+"');"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False

# add a class (period)
def addperiod(classid,teacherid,period,rows,cols,classname):
    code = getcode()
    addpd(classid,teacherid,period,rows,cols,classname,code)

# return class id; 0 if nonexistent
def classauth(code):
    if(codecheck(code)):
       return 0
    else:
        f = "utils/data/database.db"
        db = sqlite3.connect(f)
        c = db.cursor()
        m = c.execute("SELECT * FROM periods")
        for a in m:
            if(a[6]==code):
                return a[0]
        return 0
            
##################################################################################################

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

# get next class id
def getcid():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods")
    id = 1
    for a in m:
        id = a
    if(id==1):
        return id
    else:
        return id[0]+1
    
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

# returns name of student w the given student id
def getstudentname(studentid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM students WHERE id = "+str(studentid))
    for a in m:
        return a[2]

# get rows and cols in a class
def getdims(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods WHERE classid = "+str(classid))
    j = []
    for a in m:
        j.append(a[3])
        j.append(a[4])
    return j
    
# given teacher id, returns list of classids that the teacher has
def getclassest(tid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods WHERE teacherid = "+str(tid))
    j = []
    for a in m:
        j.append(a[0])
    return j

# given student id, returns a list of classids that the student has
def getclassess(sid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM classes WHERE studentid = "+str(sid))
    j = []
    for a in m:
        j.append(a[0])
    return j

# given student id, get dict of {assignmentname: grade}
def getgrades(sid):
    d = {}
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM grades WHERE studentid = "+str(sid))
    for a in m:
        d[m[3]] = m[2]
    return d

# given assignment id, returns {studentid: grade} for that assignment
def getscores(assignmentid):
    d = {}
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM grades WHERE assignmentid = "+str(assignmentid))
    for a in m:
        d[m[1]] = m[2]
    return d

# given username, get teacherid
def getteacherid(username):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM teachers")
    for a in m:
        if(a[0]==username):
            return a[3] 
    return 0

# given username, get teacherid
def getstudentid(username):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM students")
    for a in m:
        if(a[0]==username):
            return a[3] 
    return 0

# returns seatid of student in class
def getseatid(classid,studentid):
    b = getstudents(classid)
    return b[studentid]

# returns list of student ids of kids who wear glasses
def getglasses(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM classes WHERE classid = "+str(classid))
    g = []
    for a in m:
        g.append(a[2])
    return g

# returns boolean of whether the student wears glasses
def checkglasses(studentid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM students")
    for a in m:
        if(a[3]==studentid):
            return a[4] 
    return 0

# returns dict
def getseatless(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM classes WHERE classid = "+str(classid))
    d = {}
    for a in m:
        if(a[5]==0):
            d[a[3]] = a[2]
    return d

def getabsences(classid,studentid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM absences WHERE classid = "+str(classid))
    g = []
    for a in m:
        if(a[1]==studentid):
            g.append(a[2])
    return g

def getabsences(classid,date): # mmddyy
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM absences WHERE classid = "+str(classid))
    g = []
    for a in m:
        if(a[2]==date):
            g.append(a[1])
    return g
    
##################################################################################################

# changes seat of student 
def changeseat(classid,studentid,seatid,row,col):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    a = "UPDATE classes SET seatid = '"+str(seatid)+"', row = '"+str(row)+"', col = '"+str(col)+"' WHERE classid = '"+str(classid)+"' AND studentid = '"+str(studentid)+"';"
    m = c.execute(a)
    db.commit()
    return True

def changegrade(classid,studentid,assignmentid,grade):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    a = "UPDATE grades SET grade = '"+str(grade)+"' WHERE classid = '"+str(classid)+"' AND studentid = '"+str(studentid)+"' AND assignmentid = '"+str(assignmentid)+"';"
    m = c.execute(a)
    db.commit()
    return True

##################################################################################################

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

def printgrades():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM grades")
    for a in m:
        print a

def printabsences():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM absences")
    for a in m:
        print a
    
def check():
    print "students:"
    printstudents()
    print "teachers:"
    printteachers()
    print "students in classes:"
    printclass()
    print "periods:"
    printperiods()
    print "grades:"
    printgrades()
    print "absences:"
    printabsences()
    #changegrade(00,1,12,80)
    #printgrades()

addtoclass(1,1)

##################################################################################################

def go():
    teachers()
    students()
    periods()
    classes()
    grades()
    absences()

#go()

check()

def close():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    db.commit() #save changes
    db.close()  #close database

close()

