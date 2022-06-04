var chats = document.querySelectorAll('.chat')

document.addEventListener('DOMContentLoaded', function () {
    var divs = document.querySelectorAll('.users');
    divs.forEach(function (div) {
        html = div.innerHTML;
        html = html.replace(/ /g, '');
        html = html.replace(/\r?\n|\r/g, '');
        html = html.replace(new RegExp(',', 'g'), ', ');
        console.log(html);
        div.innerHTML = html;
    });
});

chats.forEach(function (chat) {
    chat.addEventListener('click', function (evt) {
        location.href = chat.getAttribute('data-url');
    })
})