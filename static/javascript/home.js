var addToClass = function(event){
    var secretKey = document.getElementById('secretKey').value;
    if (secretKey){
        $.ajax({
            url: '/checkClass',
            type: 'GET',
            data: {'secretkey':secretKey},
            success: function(data){
                location.reload();
            }

        });
    }
    else{

    }
}


var sub = document.getElementById('searchClass');
if (sub){
    sub.addEventListener('click', addToClass);
}
