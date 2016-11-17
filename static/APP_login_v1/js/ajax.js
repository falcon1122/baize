/*

by tayir 
email:arnoldincredible@126.com
*/

$('#submit').on("click",fun_user_login_check);

function fun_user_login_check(e){
	e.preventDefault(); 
    var action = "login",
        isChecked = $("#remember_me").is(":checked"),
        username = $("#name").val(),
        password = $("#pass").val(),
        datatype = "json";
        REMEMBER_ME = isChecked?true:false;

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
                            $("#login-alert").removeClass("alert alert-danger").addClass("alert alert-success").html(data.msg);
                        }else if(!data.success){
                            $("#login-alert").removeClass("alert alert-success").addClass("alert alert-danger").html(data.msg);
                            fun_web_redirect(data.redirect);
                        }
                    }
                }

    $.ajax(options);
}

function fun_web_redirect(redirect){
	var url = redirect || REDIRECT;
    window.location.href = url;
}