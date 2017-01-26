from . import database
import random

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

    html = "<center>";
    for x in range(rows):
        for y in range(cols):

            #seatid
            id = (cols*x) + y + 1

            if id in d:

                name = d[id][0]
                sid = d[id][1]

                #open div; seat
                html += '<div class="filledseat seat" ondrop="drop(event)">'

                #p; student
                html +='<div class="student" ondragstart="dragStart(event)" ondragover="allowDrop(event)">'
                html += name
                if (database.checkglasses(sid)):
                    html += '<i class="fa fa-eye"></i>'
                #p; sid
                html += '<p class="sid" hidden>' + str(sid) + '</p>'
                #attend; attendance box
                html += '<div class="attend">'
                html += '<input class="check" type="checkbox">'
                html += 'Absent?'
                html += '</input>'
                html += '</div>'

                html += '</div>'

                #p; seat
                html += '<p class="seatid" hidden>' + str(id) + '</p>'

                #close div, add aesthetic spaces
                html += '</div>'

            else:
                #open div; seat
                html += '<div class="openseat seat" ondrop="drop(event)">'

                #p; seatid
                html += '<p class="seatid" hidden>' + str(id) + '</p>'

                #p; student
                html +='<div class="student" ondragstart="dragStart(event)" ondragover="allowDrop(event)">'
                html += "&emsp;&emsp;"
                html += '</div>'

                #close div, add aesthetic spaces
                html += '</div>'

        html += "<br>"

    html += "</center>"
    seatless = database.getseatless(classid)
    #name: id
    if seatless:
        html += "<center><p>The Unseated</p>"

        for i in seatless:

            sid = seatless[i]
            #open div; seat
            html += '<div class="filledseat seat" ondrop="drop(event)">'

            #p; student
            html +='<div class="student" ondragstart="dragStart(event)" ondragover="allowDrop(event)">'
            html += i
            #p; sid
            if (database.checkglasses(sid)):
                html += '<i class="fa fa-eye"></i>'
            html += '<p class="sid" hidden>' + str(sid) + '</p>'
            #attend; attendance box
            html += '<div class="attend">'
            html += '<input class="check" type="checkbox">'
            html += 'Absent?'
            html += '</input>'
            html += '</div>'
            html += '</div>'


            #close div, add aesthetic spaces
            html += '</div>'
            html += '&emsp;&emsp;'

        html +="</center>"

    return html;

def glassesSeatGen(classid):
    print "=============="
    students = database.getstudents(classid).keys()
    random.shuffle(students)

    withGlasses = []
    withoutGlasses = []

    for i in students:
        if (database.checkglasses(i)):
            withGlasses.append(i)
        else:
            withoutGlasses.append(i)

    l = database.getdims(classid)
    rows = l[0]
    cols = l[1]

    random.shuffle(withGlasses)
    random.shuffle(withoutGlasses)

    for x in range(rows):
        for y in range(cols):
            #seatid
            id = (cols*x) + y
            print "id:"+str(id)
            if (id < len(withGlasses)):
                print "personSiGlasses:"+str(withGlasses[id])
                setSeat(classid,withGlasses[id],id+1)
            elif (id < (len(withGlasses) + len(withoutGlasses))):
                print "personNoGlasses:" +str(withoutGlasses[id-len(withGlasses)])
                setSeat(classid,withoutGlasses[id-len(withGlasses)],id+1)

    return 'success'
