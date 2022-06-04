var search = document.getElementById("app_search");

search.onkeydown = function(evt) {
    window.setTimeout(function() {
        var apps = document.querySelectorAll('.app');
        var text = search.value;
        apps.forEach(function(app) {
            var regex = new RegExp(text.toLowerCase(), 'g');
            var app_text = app.getElementsByClassName('app-label')[0].textContent.toLowerCase();
            if (app_text.match(regex) != null) {
                app.style.display = 'inline-block';
            } else {
                app.style.display = 'none';
            }
        });
    }, 1);
};