# TEACHERS
# teachers(): username|password|name|id
# addteacher(user,pass,name,id)
# getteacherid(username) -- returns tid of teacher w given username
# printteachers()

# STUDENTS/GLASSES
# students(): username|password|name|id|glasses
# addstudent(username,password,name,id,glasses)
# getstudents(classid) -- returns dict of {studentid: seatid} in given class
# getstudentname(studentid) -- returns name of student w given studentid
# getstudentid(username) -- returns sid of teacher w given username
# checkglasses(studentid) -- returns boolean of whether student wears glasses
# printstudents()

# changegrade(classid,studentid,grade)

# CLASSES/SEATS # more like "students and their classes"
# classes(): classid|teacherid|studentid|name|period|seatid|glasses|row|col|grade
# addtoclass(classid,studentid) # SHAMAUL THIS IS FOR YOU
# aaddtoclass(classid,teacherid,studentid,name,pd,seatid,glasses,row,col)
# getclassest(tid) -- returns list of classids that the teacher has
# getclassestt(tid) -- returns dict of classes by teacher {classid:classname}
# getclassess(sid) -- returns list of classids that the student has
# getclassess(sid) -- returns list of classes by student {classid:classname
# getseatless(classid) -- returns dict of {name:id} that do not have a seat yet
# changeseat(classid,studentid,seatid,row,col)
# getclassname(cid) -- returns the name of the class
# getstudentgrade(sid) -- returns {classname:grade}
# getgrades() -- master dict {classid: {studentid:grade, ... }, ... }
# printclass()

# PERIODS/DIMS
# periods(): classid|teacherid|period|rows|cols|classname|secretcode
# addperiod(classid,teacherid,pd,rows,cols,classname) # SHAMAUL USE THIS
# addpd(classid,teacherid,pd,rows,cols,classname,secretcode)
# getdims(classid) -- returns [rows,cols] of a class
# getsecretcode(classid) -- returns the secret code of a class
# getperiod(classid) returns pd number
# printperiods()

# ABSENCES
# absences(): classid|studentid|date
# addabsence(classid,studentid,date) -- date is a STRING
# getabsencesbystudent(classid,studentid) -- list of dates student was absent
# getabsencesbydate(classid,date) -- list of students absent on given date
# getabsences(studentid) -- {classid: date}
# getabsencec(classid) -- {studentid: date}
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
    q = "CREATE TABLE IF NOT EXISTS classes (classid INTEGER, teacherid INTEGER, studentid INTEGER, name TEXT, period INTEGER, seatid INTEGER, glasses BOOLEAN, row INTEGER, col INTEGER, grade INTEGER)"
    c.execute(q)
    db.commit()

def periods():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS periods (classid INTEGER, teacherid INTEGER, period INTEGER, rows INTEGER, cols INTEGER, classname TEXT, secretcode TEXT)"
    c.execute(q)
    db.commit()

def absences():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS absences (classid INTEGER, studentid INTEGER, date TEXT)" # date is a STRING and must be formatted 'mmddyyyy'
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


# True if class already exists
def periodcheck(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT * FROM periods WHERE classid = "+str(classid)
    d = c.execute(q)
    for a in d:
        return True
    return False

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
        #print q
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False

# add student to class
def aaddtoclass(classid, teacherid, studentid, name, period, seatid, glasses, row, col, grade):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(classcheck(classid,studentid)):
        c = db.cursor()
        q = "INSERT INTO classes VALUES ('"+str(classid)+"','"+str(teacherid)+"','"+str(studentid)+"','"+name+"','"+str(period)+"','"+str(seatid)+"','"+str(glasses)+"','"+str(row)+"','"+str(col)+"','"+str(grade)+"');"
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
        grade = 0
        aaddtoclass(classid,teacherid,studentid,name,period,seatid,glasses,row,col,grade)
        db.commit()
        db.close()
        return True
    else:
        return False

def getclassname(cid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods WHERE classid = "+str(cid))
    for a in m:
        return a[5]

# given student id, get dict of {classname: grade}
def getstudentgrade(sid):
    d = {}
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM classes WHERE studentid = "+str(sid))
    for a in m:
        name = getclassname(a[0])
        d[name] = a[9]
    return d

# return True if not already marked absent
def absencecheck(classid,studentid,date):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM absences WHERE classid = "+str(classid))
    for a in m:
        if(a[1]==studentid and a[2]==date):
            return False
    return True

def addabsence(classid,studentid,date):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(not classcheck(classid,studentid)): # if student is in class
        if(absencecheck(classid,studentid,date)):
            c = db.cursor()
            q = "INSERT INTO absences VALUES ('"+str(classid)+"','"+str(studentid)+"','"+str(date)+"');"
            c.execute(q)
            db.commit()
            db.close()
            return True
    return False

# returns False if code already in use
def codecheck(code):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods")
    for a in m:
        if(a[6]==code):
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
    if(not periodcheck(classid)):
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

#addperiod(9,-3,9,5,7,"chorus")
    
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

def changegrade(classid,studentid,grade):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    a = "UPDATE classes SET grade = '"+str(grade)+"' WHERE classid = '"+str(classid)+"' AND studentid = '"+str(studentid)+"';"
    m = c.execute(a)
    db.commit()
    return True

# returns {classid: {studentid:grade, studentid:grade}, ... }
def getgrades():
    d = {}
    g = {}
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT classid FROM classes")
    for a in m:
        q = db.cursor()
        n = q.execute("SELECT studentid,grade FROM classes WHERE classid = "+str(a[0]))
        for w in n:
            g[w[0]] = w[1]
        d[a[0]] = g
    return d

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

# given teacher id, returns dict of classids that the teacher has {classid:classname}
def getclassestt(tid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods WHERE teacherid = "+str(tid))
    d = {}
    for a in m:
        d[str(a[0])] = a[5]
    return d

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

# given student id, returns a dict of classes that the student has {classid:classname}
def getclassesss(sid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM periods WHERE studentid = "+str(sid))
    d = {}
    for a in m:
        d[str(a[0])] = a[5]
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
            d[a[2]] = a[3]
    return d

def getabsencesbystudent(classid,studentid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM absences WHERE classid = "+str(classid))
    g = []
    for a in m:
        if(a[1]==studentid):
            g.append(str(a[2]))
    return g

def getabsencesbydate(classid,date): # mmddyy
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM absences WHERE classid = "+str(classid))
    g = []
    for a in m:
        if(a[2]==date):
            g.append(str(a[1]))
    return g

# returns {classid: date}
def getabsences(studentid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM absences WHERE studentid = "+str(studentid))
    d = {}
    for a in m:
        d[str(a[0])]=a[2]
    return d

# {studentid:date}
def getallabsencec(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM absences WHERE classid = "+str(classid))
    d = {}
    for a in m:
        d[str(a[1])]=a[2]
    return d

def getperiod(classid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT period FROM periods WHERE classid = "+str(classid))
    for a in m:
        return a[0]

#print getperiod(12)
    
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
    print "absences:"
    printabsences()

##################################################################################################

#addabsence(4,5,'04/12/17')

#print absences()

#check()

def go():
    teachers()
    students()
    periods()
    classes()
#    grades()
    absences()

go()

'''
#id=3,classid=12,tid=-1,pd=8,5x5,grade=90
addstudent("nicole","nicole","nIcole",3,1)
addperiod(12,-3,8,5,5,"trig")
addtoclass(12,3)
changegrade(12,3,90)
#print getgrades()

# id=4,cid=14,tid=-1,pd=8,5x5,grade=95
addstudent("u","pw","nm",4,0)
addperiod(14,-4,10,5,5,"anotherclass")
addtoclass(14,4)
changegrade(14,4,95)

# id=2,cid=10,tid=-2,pd9,5x5,grade=0
addperiod(10,-4,9,5,5,"antclass")
addtoclass(10,4)
#print getgrades()
#print getstudentgrade(1)
#print getstudentgrade(2)
'''

#check()

#print getclassname(10)

def close():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    db.commit() #save changes
    db.close()  #close database

close()

##################################################################################################

# GRADES
# grades(): classid|studentid|grade|assignmentid|assignmentname
# addgrade(classid,studentid,grade,assignmentid,asignmentname)
# getgradesbystudent(sid) -- returns dictionary of {assignmentname: grade}
# getgradesbyassignment(aid) -- return dict {studentname: grade}
# getscores(assignmentid) -- returns dict of {studentid: grade} for assignment
# changegrade(classid,studentid,assignmentid,grade)
# printgrades()

'''

def grades():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS grades (classid INTEGER, studentid INTEGER, grade INTEGER, assignmentid INTEGER, assignmentname TEXT)"
    c.execute(q)
    db.commit()

# return True if not already graded
def gradecheck(classid,studentid,assignmentid):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM grades WHERE classid = "+str(classid)+" AND assignmentid = "+str(assignmentid))
    for a in m:
        if(a[1]==studentid):
            return False
    return True

def addgrade(classid, studentid, grade, assignmentid, assignmentname):
    if(gradecheck(classid,studentid,assignmentid)):
        f = "utils/data/database.db"
        db = sqlite3.connect(f)
        if(isinstance(grade,int)):
            c = db.cursor()
            q = "INSERT INTO grades VALUES ('"+str(classid)+"','"+str(studentid)+"','"+str(grade)+"','"+str(assignmentid)+"','"+str(assignmentname)+"');"
            c.execute(q)
            db.commit()
            db.close()
            return True
    return False

# given student id, get dict of {assignmentname: grade}
def getgradesbystudents(sid):
    d = {}
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM grades WHERE studentid = "+str(sid))
    for a in m:
        d[a[3]] = a[2]
    return d

# given assignment id, get dict of {studentname: grade}
def getgradesbyassignment(aid):
    d = {}
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM grades WHERE assignmentid = "+str(aid))
    q = db.cursor()
    for a in m:
        studentid = a[1]
        n = q.execute("SELECT name FROM students WHERE id = "+str(studentid))
        for b in n:
            name = b[0]
        d[name] = a[2]
    return d

# {assignmentname:assignmentid}
def getassignments(classid):
    d = {}
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM grades WHERE classid = "+str(classid))
    for a in m:
        d[a[4]] = a[3]
    return d

# given assignment id, returns {studentid: grade} for that assignment
def getscores(assignmentid):
    d = {}
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM grades WHERE assignmentid = "+str(assignmentid))
    for a in m:
        d[a[1]] = a[2]
    return d

def changegrade(classid,studentid,assignmentid,grade):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    a = "UPDATE grades SET grade = '"+str(grade)+"' WHERE classid = '"+str(classid)+"' AND studentid = '"+str(studentid)+"' AND assignmentid = '"+str(assignmentid)+"';"
    m = c.execute(a)
    db.commit()
    return True

def printgrades():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM grades")
    for a in m:
        print a
'''
