const accept = document.querySelectorAll(".accept");
const reject = document.querySelectorAll(".reject");

accept.forEach(function (btn) {
    btn.addEventListener("click", function () {
        url = btn.getAttribute("data-url");
        chat = btn.getAttribute("data-chat");

        var xhr = new XMLHttpRequest();
        xhr.open("GET", `${url}?location=${chat}`, true);
        xhr.send();

        btn.parentElement.parentElement.remove();
    });
});

reject.forEach(function (btn) {
    btn.addEventListener("click", function () {
        url = btn.getAttribute("data-url");
        chat = btn.getAttribute("data-chat");

        var xhr = new XMLHttpRequest();
        xhr.open("GET", `${url}?location=${chat}`, true);
        xhr.send();

        btn.parentElement.parentElement.remove();
    });
});
