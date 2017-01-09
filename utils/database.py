import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

#f="data/database.db"

#################################################################################################
def users():
    f = "data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, teacher BOOLEAN, name TEXT, id INTEGER)"
    c.execute(q)    #run SQL query
    db.commit()
    

##################################################################################################
def classes():
    f = "data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS classes (classid INTEGER, teacherid INTEGER, studentid INTEGER, period INTEGER, seatid INTEGER, glasses BOOLEAN)"
    c.execute(q)
    db.commit()

    
##################################################################################################
def grades():
    f = "data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS grades (classid INTEGER, studentid INTEGER, grade INTEGER, assignmentid INTEGER, assignmentname TEXT)"
    c.execute(q)
    db.commit()
    

##################################################################################################


def go():
    users()
    classes()
    grades()

#go()

def close():
    f = "data/database.db"
    db = sqlite3.connect(f)
    db.commit() #save changes
    db.close()  #close database

    
close()

