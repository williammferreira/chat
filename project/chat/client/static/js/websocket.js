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
  if (data.username == document.getElementById('user_username').textContent.slice(1,-1)) {
    document.getElementById('message-area').innerHTML += `
      <div class='message mymessage'>
        <div class='message-info'>
          <em>Me</em><br>
          <em>date</em>
        </div>
        <p>myMessage</p>
      </div>
    `.replace('date', data.datetime).replace('myMessage', data.message);
  } else {
    document.getElementById('message-area').innerHTML += `
      <div class='message othermessage'>
        <div class='message-info'>
          <em>user</em><br>
          <em>date</em>
        </div>
        <p>otherMessage</p>
      </div>
    `.replace('user', data.username).replace('date', data.datetime).replace('otherMessage', data.message);
  }
}

chatSocket.onclose = function(closeCode) {
  document.getElementById('message-area').innerHTML = 'The chat socket closed unexpectedly.';
}
