// JavaScript source code
function validate() {
    var name = document.getElementById("name");
    var username = document.getElementById("uname");
    var telephone = document.getElementById("tele");
    var email = document.getElementById("em");
    var password = document.getElementById("pass");
    var password1 = document.getElementById("pass1");
    var fgender = document.getElementById("female");
    var mgender = document.getElementById("male");

    if (name.value == "" || username.value == "" || telephone.value == "" || email.value == "" || password.value == "" || fgender.value == "" || mgender.value == "" || password1.value == "") {
        alert("No blank values allowed")
    }
    else if (password.value != password1.value) {
        alert("two passwords dont match.")
    }
    else if (telephone.value.length > 10) {
        alert("enter a valid phone number")
    }
    else {
        alert("Your account has been successfully created!!")
    }

}
function fun() {
    document.getElementById("name").value='';
    document.getElementById('uname').value = '';
    document.getElementById('tele').value = '';
    document.getElementById("em").value = '';
    document.getElementById("pass").value = '';
    document.getElementById("pass1").value = '';
    document.getElementById("fgender").value = '';
    document.getElementById("mname").value = '';
} 

