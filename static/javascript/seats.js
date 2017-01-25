//The #1 Global Variable
var seat = document.getElementsByClassName('seat');


//--------drag and drop-------
var oldEvent;

function allowDrop(event) {
    event.preventDefault();
}

function dragStart(event) {
    oldEvent = event.target;
    event.dataTransfer.setData("student", event.target.innerHTML);
}

function drop(event){

    event.preventDefault();
    var data = event.dataTransfer.getData("student");
    var data2 = event.target.innerHTML;
    if (data2 && data){
        if (!(data === 'undefined' || data2 === 'undefined')){

            div1 = event.target.parentElement;
            div2 = oldEvent.parentElement;

            event.target.innerHTML = data;
            oldEvent.innerHTML = data2;

            console.log(data);
            console.log(data2);
            console.log(event.target);
            console.log(oldEvent);

            class1 = div1.className;
            class2 = div2.className;

            div1.className = class2;
            div2.className = class1;
        }
    }
}


//------editing seat mode v class mode----------

var butt = document.getElementById('butt');
var edit = false;


//TODO: edit db w/new seat ids
var save = function(event){
    butt.innerHTML = "Edit"
    butt.removeEventListener('click', save);
    butt.addEventListener('click', editSeats);
    var student = document.getElementsByClassName('student');
    for (var i = 0; i < student.length; i++){
        student[i].setAttribute('draggable',false);
        student[i].style.cursor = 'default';
        edit = false;
    }

    var cid = document.getElementById('cid').innerHTML;

    for (var i = 0; i < seat.length; ++i){
        if (seat[i].className.includes('filled')){
            console.log(i);
            try{
                var thisSid = seat[i].getElementsByClassName('student')[0].getElementsByClassName('sid')[0].innerHTML;
                console.log('cid: ' + cid + ' sid: ' + thisSid + ' seat: ' + i);
                $.ajax({
                    url: '/changeseat/',
                    type: 'GET',
                    data: {'cid':cid, 'sid':thisSid, 'seatid':i},
                    success: function(data){
                        console.log(data);
                    }

                });
            }
            catch(TypeError){
                console.log(seat[i]);
            }

        }

    }
}

var editSeats = function(event){
    butt.innerHTML = "Save";
    butt.removeEventListener('click', editSeats);
    butt.addEventListener('click',save);
    var student = document.getElementsByClassName('student');
    for (var i = 0; i < student.length; i++){
        student[i].setAttribute('draggable',true);
        edit = true;
    }
}

//--------attendance stuff-------------

var showAttendance = function(event){
    if (!edit){
        try{
            var attend = event.target.getElementsByClassName('attend')[0];
            attend.style.display = 'block';
        }
        catch(TypeError){}
    }
}

var hideAttendance = function(event){
    try{
        var attend = event.target.getElementsByClassName('attend')[0];
        attend.style.display = 'none';
    }
    catch(TypeError){}
}

//Todo: actually change attendance of student
var attendance = function(event){
    student = event.target.parentNode.parentNode.getElementsByClassName('student')[0].innerHTML;
    if (event.target.checked){
        console.log(student + ' absent');
    }
    else{
        console.log(student + ' not absent')
    }
}

//-----------set up stuff------------

butt.addEventListener('click',editSeats);

for (i = 0; i < seat.length; i++){
    seat[i].addEventListener('mouseenter',showAttendance);
    seat[i].addEventListener('mouseleave',hideAttendance);
    var attend = document.getElementsByClassName('attend')[i];
    attend.style.display = 'none';
    attend.getElementsByClassName('check')[0].addEventListener('change',attendance);
}
