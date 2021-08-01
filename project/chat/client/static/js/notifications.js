window.requestAnimFrame = (function () {
    return window.requestAnimationFrame ||
        window.webkitRequestAnimationFrame ||
        window.mozRequestAnimationFrame ||
        function (callback) {
            window.setTimeout(callback, 1000 / 60);
        };
})();

window.cancelAnimFrame = (function () {
    return window.cancelAnimationFrame ||
        window.webkitCancelAnimationFrame ||
        window.mozCancelAnimationFrame ||
        function (callback) {
            window.setTimeout(callback, 1000 / 60);
        };
})();



var interval;

function sendNotification(text, color = "#39FF14", width = "150px", interval = 1) {
    var element = document.createElement("SPAN");
    var div = document.createElement("div");
    div.appendChild(element);
    document.getElementById("notifacations-container").appendChild(div);
    div.style.width = width;
    div.style.height = "40px";
    div.style.color = "white";
    div.style.right = "5%";
    div.style.background = color;
    div.style.zIndex = "2";
    div.style.position = "fixed";
    div.style.borderRadius = "5%";
    div.style.textAlign = "center";
    div.style.border = "2px solid gray";
    div.style.fontFamily = "sans-seirf";
    div.style.lineHeight = "40px";
    div.style.fontSize = "20px";
    div.style.textAlign = "center";
    element.style.height = "20px";
    element.style.marginRight = "auto";
    element.style.marginLeft = "auto";
    element.innerHTML = text;
    moveNotification(div, interval);
}

function moveNotification(div, intervalTime) {
    var pos = 0;
    var animationId;
    function animate() {
        if (pos > 10) {
            cancelAnimFrame(animationId);
            return;
        }
        pos++;
        div.style.marginTop = pos * 10 + "px";
        animationId = requestAnimFrame(animate);
    }

    animate();

    setTimeout(function () {
        div.remove();
    }, 2000);
}