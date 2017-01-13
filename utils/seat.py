import sqlite3   #enable control of an sqlite database

#gets list of students in class classId
def students(classId):
    f = "utils/data/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT name"

def seatHtml(x, y):
    html = "";
    for i in range(y):
        html += "<center>"
        for j in range(x):
            me = (x*i) + j
            html += '<div class="seat" ondrop="drop(event)"><p draggable="true" ondragstart="dragStart(event)" ondragover="allowDrop(event)">Student ' + str(me) + '</p></div>'
        html += "</center><br>"
    return html;
