var login = document.getElementById('loginL');
var reg = document.getElementById('loginR');

var displayLogin = function(event){
    document.getElementById('loginElements').style.display = 'block';
    document.getElementById('registerElements').style.display = 'none';
    //login.style.backgroundColor = '#9F81F7';
    //reg.style.backgroundColor = '#D1D5DE';
}

var displayReg = function(event){
    document.getElementById('loginElements').style.display = 'none';
    document.getElementById('registerElements').style.display = 'block';
   // reg.style.backgroundColor = '#9F81F7';
    //login.style.backgroundColor = '#D1D5DE';
}

login.addEventListener('click',displayLogin);
reg.addEventListener('click',displayReg);
