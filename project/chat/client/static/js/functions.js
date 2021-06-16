function HTMLDecode(input) {
	var doc = new DOMParser().parseFromString(input, "text/html");
	return doc.documentElement.textContent;
}

function sendMessage() {
	if (document.getElementById('chat-input').value != '') {
		chatSocket.send(JSON.stringify(
			{
				'message': document.getElementById('chat-input').value,
				'token': document.getElementById('token').textContent.substring(1, (document.getElementById('token').textContent.length - 1)),
			}
		));
		document.getElementById('chat-input').value = '';
	}
}