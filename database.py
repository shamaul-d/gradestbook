import sqlite3   #enable control of an sqlite database

#f="utils/data/database.db"

#################################################################################################
def users():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, teacher BOOLEAN, name TEXT, id INTEGER)"
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
def logincheck(username):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT username FROM users"
    d = c.execute(q)
    for n in d:
        if(n[0] == username):
            return True
    db.close()
    return False

# ret True if successfully added, False if username already exists
def adduser(username,password,teacher,name,id):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    if(not logincheck(username)):
        c = db.cursor()
        q = "INSERT INTO users VALUES ('"+username+"','"+password+"','"+str(teacher)+"','"+name+"',"+str(id)+");"
        c.execute(q)
        db.commit()
        db.close()
        return True
    else:
        return False

#adduser("nicole","nicole","nicole","nicole",0)
#adduser("b","a",True,"a",2)

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

def printusers():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    m = c.execute("SELECT * FROM users")
    for a in m:
        print a

#printusers()

def go():
    users()
    classes()
    grades()

#go()

def close():
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    db.commit() #save changes
    db.close()  #close database

close()
