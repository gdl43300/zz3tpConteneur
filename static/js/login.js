var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == "zz3" && password == "zz3") {
        alert("Login successfully");
        //window.location = ""; // Redirecting to other page.
        return false;
    } else {
        alert("Wrong Username or Password")
    }
}