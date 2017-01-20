var addToClass = function(event){
    var cid = document.getElementById('cid').value;
    if (cid){
        $.ajax({
            url: '/checkClass',
            type: 'GET',
            data: {'cid':cid},
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
