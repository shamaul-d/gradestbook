def getRowCol(classid, seatNumber):
    l = database.getDims(classid)
    rows = l[0]
    y = (seat - 1)/rows
    x = (seat - 1) % rows
    return [x,y]

def removeSeat(classid, studentid):
    # changeseat(classid,studentid,seatid,row,col)
    d = database.getStudents(classid)
    seatid = d[studentid]

    l = database.getDims(classid)

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

#actual; when we deal w/classes and students
def seatHtml(classid):

    l = database.getDims(classid)
    rows = l[0]
    cols = l[1]

    # getstudents(classid) -- returns dict of {studentid: seatid} in given class
    students = database.getstudents(cid)
    d = {}

    for i in students:
        #seatid
        d[students[i]] = database.getstudentname(i)

    html = "";
    for x in range(rows):
        html += '<center>'
        for y in range(cols):

            id = (rows*y) + x + 1
            name = d[id]

            if (name):

                #open div; seat
                html += '<div class="seat" ondrop="drop(event)">'

                #p; student
                html +='<p class="student" ondragstart="dragStart(event)" ondragover="allowDrop(event)">'
                html += 'Student ' + name
                html += '</p>'

                #attend; attendance box
                html += '<div class="attend">'
                html += '<input class="check" type="checkbox">'
                html += 'Absent?'
                html += '</input>'
                html += '</div>'

                #close div, add aesthetic spaces
                html += '</div>'
                html += '&emsp;&emsp;'

        html += "</center><br>"
    return html;
