var addToClass = function(event){
    var secretKey = document.getElementById('secretKey').value;
    if (secretKey){
        $.ajax({
            url: '/checkClass',
            type: 'GET',
            data: {'secretkey':secretKey},
            success: function(data){
                var msg = document.getElementById('joinMsg');
                msg.innerHTML = data;
            }

        });
    }
    else{

    }
}


var sub = document.getElementById('searchClass');
sub.addEventListener('click', addToClass);
