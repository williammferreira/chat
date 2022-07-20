var pin_buttons = document.querySelectorAll(".pin-button");
var chats = document.querySelectorAll(".chat");

pin_buttons.forEach((btn) =>
    btn.addEventListener("click", function (evt) {
        btn.parentElement.parentElement.parentElement.remove();
    })
);
