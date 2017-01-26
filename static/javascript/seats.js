//The #1 Global Variable
var seat = document.getElementsByClassName('seat');
var filledseat = document.getElementsByClassName('filledseat');
var cid = document.getElementById('cid').innerHTML;
var rand = document.getElementById('rand');

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

    for (var i = 0; i < seat.length; ++i){
        if (seat[i].className.includes('filled')){
            try{
                var thisSid = seat[i].getElementsByClassName('student')[0].getElementsByClassName('sid')[0].innerHTML;
                seatNum = seat[i].getElementsByClassName('seatid')[0].innerHTML;
                $.ajax({
                    url: '/changeseat/',
                    type: 'GET',
                    data: {'cid':cid, 'sid':thisSid, 'seatid':seatNum},

                });
            }
            catch(TypeError){
            }

        }

    }

    location.reload();
}

var editSeats = function(event){
    butt.innerHTML = "Save";
    butt.removeEventListener('click', editSeats);
    butt.addEventListener('click',save);

    rand.style.display = 'block';

    var student = document.getElementsByClassName('student');
    for (var i = 0; i < student.length; i++){
        student[i].setAttribute('draggable',true);
        edit = true;
    }
}

//--------random seating-------------

var seatGen = function(event){

    $.ajax({
        url: '/glassesSeatGen/',
        type: 'GET',
        data: {'cid':cid},
        success: function(data){
            //console.log(data);
            location.reload();
        }

    });

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
    var absentSid = event.target.parentNode.parentNode.getElementsByClassName('sid')[0].innerHTML;
    var date = new Date();
    var timestamp = date.getMonth() + 1;
    timestamp += "/";
    timestamp += date.getDate();
    timestamp += "/"
    timestamp += date.getFullYear();
    if (event.target.checked){
        $.ajax({
            url: '/absent/',
            type: 'GET',
            data: {'sid':absentSid, 'cid':cid,'time':timestamp},
            success: function(data){
                console.log('absent');
            }

        });
    }
    else{
        $.ajax({
            url: '/notAbsent/',
            type: 'GET',
            data: {'sid':absentSid, 'cid':cid,'time':timestamp},
            success: function(data){
                console.log('not absent');
            }

        });
    }
}

//-----------set up stuff------------

butt.addEventListener('click',editSeats);


for (i = 0; i < filledseat.length; i++){
    filledseat[i].addEventListener('click',showAttendance);
    filledseat[i].addEventListener('mouseleave',hideAttendance);
    var attend = document.getElementsByClassName('attend')[i];
    attend.style.display = 'none';
    attend.getElementsByClassName('check')[0].addEventListener('change',attendance);
}

rand.style.display = 'none';
rand.addEventListener('click',seatGen);
