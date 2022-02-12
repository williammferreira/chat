window.onload = function() {
    if (getCookie('logorun') !== '0') {
        setTimeout(function() {
            document.body.style.overflow = "auto";
        }, 2200)
        var style = document.createElement("link");
        style.href = importAnimationUrl;
        style.type = "text/css";
        style.rel = "stylesheet";
        document.head.appendChild(style);
        document.cookie = "logorun=0;"
    }
}