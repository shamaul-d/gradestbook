console.log('aosduhsad');

var login = document.getElementById('loginL');
var reg = document.getElementById('loginR');
var glasses = document.getElementById('glassesCheck');
var stud = document.getElementById('studentChosen');
var notstud = document.getElementById('teacherChosen');
console.log(stud);
console.log(notstud);


var displayLogin = function(event){
    document.getElementById('loginElements').style.display = 'block';
    document.getElementById('registerElements').style.display = 'none';
    login.classList.add('active');
    reg.classList.remove('active');
}

var displayReg = function(event){
    document.getElementById('loginElements').style.display = 'none';
    document.getElementById('registerElements').style.display = 'block';
    reg.classList.add('active');
    login.classList.remove('active');
}

var studentView = function(event){
    console.log('student');
    glasses.style.display = 'block';
}

var teacherView = function(event){
    console.log('teach');
    glasses.style.display = 'none';
}

login.addEventListener('click',displayLogin);
reg.addEventListener('click',displayReg);

stud.addEventListener('click',studentView);
notstud.addEventListener('click',teacherView);
