function HTMLDecode(input) {
    var doc = new DOMParser().parseFromString(input, "text/html");
    return doc.documentElement.textContent;
}

function sendMessage() {
    if ($('#chat-input').value != '') {
        chatSocket.send(JSON.stringify(
            {
                'message': $('#chat-input').value,
                'token': $('#token').textContent.substring(1, ($('#token').textContent.length - 1)),
            }
        ));
        $('#chat-input').value = '';
    }
}

function searchChat() {
    searchSocket.send(JSON.stringify(
        {
            "input": $('#searchInput').value,
        }
    ));
}

function executeAsync(func) {
    setTimeout(func, 0);
}

function fitText(element, space) {
    var parent = element.parentNode;

    element.style.fontSize = parseInt(parent.offsetHeight - space) + "px";
}

function $(name) {
    return document.querySelector(name);
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}