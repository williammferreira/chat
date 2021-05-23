const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/room/' + document.getElementById('token').textContent);

function sendMessage() {
  chatSocket.send(JSON.stringify(
    {
      'message': document.getElementById('chat-input').value
    }
  ));
  document.getElementById('chat-input').value = '';
}

chatSocket.onmessage = function(rawData) {
  var data = JSON.parse(rawData.data);
  if (data.user == document.getElementById('user_username').textContent.slice(1,-1)) {
    document.getElementById('message-area').innerHTML += `
      <div class='message mymessage'>
        <p>name</p>
        <p>date</p>
        <p>message</p>
      </div>
    `.replace('name', data.user).replace('date', data.datetime).replace('message', data.message);//data.message;
  }
}

chatSocket.onclose = function(closeCode) {
  document.getElementById('message-area').innerHTML = 'The chat socket closed unexpectedly.';
}
