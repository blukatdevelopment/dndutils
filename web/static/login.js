// JQuery required.
// Login page scripts
var login = {};

login.login = function(){
    var username = $("#login_username_input").val();
    var password = $("#login_password_input").val();
    
    var data = {
        username: username,
        password: password
    };

    $.ajax({
        type: 'POST',
        url: "/login",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function(resp) {
            console.log("Succes");
            $("#response_div").text(resp.msg);
            $("#login_div").css("display: none");
            console.log("success! Redirecting to " + resp.redirect);
            window.location.href = resp.redirect;
        },
        error: function(error){
          console.log("Error" + JSON.stringify(error));
          if(error.responseJSON){
            var responseJSON = error.responseJSON;
            console.log(error);
            var msg = responseJSON.msg;
            $("#response_div").text(msg);
          }
          else{
            $("#response_div").text("Unexpected error. Please try again later."); 
          }
        }
    });
}

login.register = function(){
    var email = $("#reg_email_input").val();
    var username = $("#reg_username_input").val();
    var password = $("#reg_password_input").val();
    
    var data = {
        username: username,
        email: email,
        password: password
    };

    $.ajax({
        type: 'POST',
        url: "/register",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function(resp) {
            $("#response_div").text("Registration successful!");
            $("#login_div").css("display: none");
            window.location.href = resp.redirect;
        },
        error: function(error){
          if(error.responseJSON){
            var responseJSON = error.responseJSON;
            console.log(error);
            var msg = responseJSON.msg;
            $("#response_div").text(msg);
          }
          else{
            $("#response_div").text("Unexpected error. Please try again later."); 
          }
        }
    });
}

$(document).ready(function(){

    $("#login_button").click(function(){
        login.login();
    });

    $("#register_button").click(function(){
        login.register();
    });

    $("#show_reg_button").click(function(){
        $("#login_div").css("display", "none");
        $("#reg_div").css("display", "block");
    });

    $("#show_login_button").click(function(){
        $("#login_div").css("display", "block");
        $("#reg_div").css("display", "none");
    });

});