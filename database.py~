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
    q = "CREATE TABLE IF NOT EXISTS classes (classid INTEGER, teacherid INTEGER, studentid INTEGER, period INTEGER, seatid INTEGER, glasses BOOLEAN)"
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
def logincheck(username,teacher):
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
    

def gethash(username):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM users")
    for a in m:
        if a[0]==username:
            db.close()
            return a[1]
    else:
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
        
printstudents()

# get next id

def go():
    teachers()
    students()
    classes()
    grades()

#go()

def close():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    db.commit() #save changes
    db.close()  #close database

close()
