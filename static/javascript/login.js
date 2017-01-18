var login = document.getElementById('loginL');
var reg = document.getElementById('loginR');
1
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

login.addEventListener('click',displayLogin);
reg.addEventListener('click',displayReg);
