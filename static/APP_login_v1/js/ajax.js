/*

by tayir 
email:arnoldincredible@126.com
*/
$('#submit').click(function(e){
    var e = e || window.event
    e.preventDefault();
    if(window.event){
        e.cancelBubble = true;
    }else{
        e.stopPropagation();
    }

    
    var action = "login",
        ischecked = $("#remember_me").is(":checked"),
        username = $("#name").val(),
        password = $("#pass").val(),
        datatype = "json";
        
    if(!ischecked){
        REMEMBER_ME = false;
    }
    var formdata = {"action":action,"username":username,"password":password,"remember_me":REMEMBER_ME,"redirect":REDIRECT};
    if(METHOD == "GET"){
        SIGNIN_URL = SIGNIN_URL + "?action=" + action + "$username=" + username + "$password=" + password  + "$remember_me=" + REMEMBER_ME + "$redirect=" + REDIRECT;
        formdata = undefined;
        datatype = undefined;
    }

    var options = {
                    type:METHOD,
                    url:SIGNIN_URL,
                    data:formdata,
                    datatype:datatype,
                    success:function(data){
                        if(data.success){
                            $("#login-alert").addClass("alert alert-success").html(data.msg);
                        }else if(!data.success){
                            $("#login-alert").addClass("alert alert-danger").html(data.msg);
                        }
                        var redirect = data.redirect || REDIRECT;
                        window.location.href(redirect);
                    }
                }

    fun_signin(options);
});

function fun_signin(options){ 
    $.ajax(options);
}
