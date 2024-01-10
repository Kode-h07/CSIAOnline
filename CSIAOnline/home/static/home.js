document.addEventListener('DOMContentLoaded', function() {
    var apiURL = "http://127.0.0.1:8000";
    console.log(document.getElementById('counsel'))

    document.getElementById('counsel').addEventListener('click', function() {
        window.location.href = apiURL + "/counsel";
        console.log("Counsel button clicked");
    });

    document.getElementById('bus').addEventListener('click', function() {
        window.location.href = apiURL;
        console.log("Bus button clicked");
    });

    document.getElementById('study').addEventListener('click', function() {
        window.location.href = apiURL;
        console.log("Study button clicked");
    });

    document.getElementById('logout').addEventListener('click', function() {
        window.location.href = apiURL;
        console.log("Logout button clicked");
    });
});
