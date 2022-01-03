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

function searchChats() {
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