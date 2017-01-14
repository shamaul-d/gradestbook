def seatHtml(x, y):
    html = "";
    for i in range(y):
        html += '<center>'
        for j in range(x):

            me = (x*i) + j

            #open div; seat
            html += '<div class="seat" ondrop="drop(event)">'

            #p; student
            html +='<p class="student" ondragstart="dragStart(event)" ondragover="allowDrop(event)">'
            html += 'Student ' + str(me)
            #html += '<p class="student"> Student ' + str(me) + "</p>"
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


'<font class="attend"><input type="checkbox">Absent?</input></font>'
