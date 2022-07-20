var chats = document.querySelectorAll(".chat");
var pin_buttons = document.querySelectorAll(".pin-button");

document.addEventListener("DOMContentLoaded", function () {
    var divs = document.querySelectorAll(".users");
    divs.forEach(function (div) {
        html = div.innerHTML;
        html = html.replace(/ /g, "");
        html = html.replace(/\r?\n|\r/g, "");
        html = html.replace(new RegExp(",", "g"), ", ");
        div.innerHTML = html;
    });
});

chats.forEach(function (chat) {
    chat.addEventListener("click", function (evt) {
        if (!evt.target.classList.contains("no-redirect")) {
            location.href = chat.getAttribute("data-url");
        }
    });
});

pin_buttons.forEach((btn) =>
    btn.addEventListener("click", function (evt) {
        url = btn.getAttribute("data-url");
        chat = btn.getAttribute("data-chat");
        csrf = btn.getAttribute("data-csrf");

        var xhr = new XMLHttpRequest();
        xhr.open("GET", url + "?location=" + chat, true);
        xhr.send();

        var img = btn.getElementsByTagName("img")[0];

        console.log(
            img.src +
                "\n" +
                window.location.origin +
                img.getAttribute("data-pinned")
        );

        if (
            img.src ==
            window.location.origin + img.getAttribute("data-pinned")
        ) {
            img.src = img.getAttribute("data-pin");
        } else {
            img.src = img.getAttribute("data-pinned");
        }
    })
);
