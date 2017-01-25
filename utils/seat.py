from . import database

def getRowCol(classid, seatNumber):
    l = database.getdims(classid)
    rows = l[0]
    y = (seat - 1)/rows
    x = (seat - 1) % rows
    return [x,y]

def removeSeat(classid, studentid):
    # changeseat(classid,studentid,seatid,row,col)
    d = database.getStudents(classid)
    seatid = d[studentid]

    l = database.getdims(classid)

    database.changeseat(classid,studentid,0,l[0] + 1, l[1] + 1)

def switchSeats(classid, id1, id2):

    # getstudents(classid) -- returns dict of {studentid: seatid} in given class
    d = database.getStudents(classid)

    seat1 = d[id1]
    seat2 = d[id2]

    # changeseat(classid,studentid,seatid,row,col)
    #change seat id of student w/newid to oldid
    xy = getRowCol(classid, seat1)
    database.changeseat(classid,id1,seat2,xy[0],xy[1])
    #change seat id of student w/oldid to newid
    xy = getRowCol(seat2)
    database.changeseat(classid,id2,seat1,xy[0],xy[1])

def setSeat(cid, sid, seatid):
    l = database.getdims(cid)
    row = l[0]
    col = l[1]
    database.changeseat(cid,sid,seatid,row,col)
    return 'done'

#actual; when we deal w/classes and students
def seatHtml(classid):

    l = database.getdims(classid)
    rows = l[0]
    cols = l[1]

    # getstudents(classid) -- returns dict of {studentid: seatid} in given class
    students = database.getstudents(classid)
    d = {}

    for i in students.keys():
        #seatid: name, sid
        d[students[i]] = [database.getstudentname(i), i]

    html = "";
    for x in range(rows):
        html += '<center>'
        for y in range(cols):

            #seatid
            id = (rows*y) + x + 1

            if id in d:

                name = d[id][0]
                sid = d[id][1]

                #open div; seat
                html += '<div class="filledseat seat" ondrop="drop(event)">'

                #p; student
                html +='<p class="student" ondragstart="dragStart(event)" ondragover="allowDrop(event)">'
                html += name
                #p; sid
                html += '<p class="sid">' + str(sid) + '</p>'
                html += '</p>'

                #p; seat
                html += '<p class="seatid">' + str(id) + '</p>'

                #attend; attendance box
                html += '<div class="attend">'
                html += '<input class="check" type="checkbox">'
                html += 'Absent?'
                html += '</input>'
                html += '</div>'

                #close div, add aesthetic spaces
                html += '</div>'
                html += '&emsp;&emsp;'

            else:
                #open div; seat
                html += '<div class="openseat seat" ondrop="drop(event)">'

                #p; seatid
                html += '<p class="sid">' + str(id) + '</p>'

                #p; student
                html +='<p class="student" ondragstart="dragStart(event)" ondragover="allowDrop(event)">'
                html += "&emsp;&emsp;"
                html += '</p>'

                #close div, add aesthetic spaces
                html += '</div>'
                html += '&emsp;&emsp;'

        html += "</center><br>"

    seatless = database.getseatless(classid)
    #name: id
    if seatless:
        html += "<center><p>The Unseated</p>"

        for i in seatless:

            sid = seatless[i]
            #open div; seat
            html += '<div class="filledseat seat" ondrop="drop(event)">'

            #p; student
            html +='<p class="student" ondragstart="dragStart(event)" ondragover="allowDrop(event)">'
            html += i
            #p; sid
            html += '<p class="sid">' + str(sid) + '</p>'
            html += '</p>'


            #close div, add aesthetic spaces
            html += '</div>'
            html += '&emsp;&emsp;'

        html +="</center>"

    return html;
