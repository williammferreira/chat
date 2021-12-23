const searchSocket = new WebSocket('ws://' + window.location.host + '/ws/search');

searchSocket.onopen = function () {
  sendNotification("connected!");
}

searchSocket.onmessage = function (rawData) {
  var data = JSON.parse(rawData.data);
  var chats = ``;
  if ((data.output).length == 0) {
    chats = `<p class='no-chats-search' style='font-size: 15px;'><i>No chats match your search.</i></p>`;
  } else {
    // 0=chatCreator 1=chatUsers 2=chatDescription 3=chatDateCreated 4=locationUrl 5=token
    for (var i = 0; i < (data.output).length; i++) {
      chats += `
      <div class="chat" onclick="replace('/~/chats/` + data.output[i][4] + `')">
          <div class="title"><b>` + data.output[i][0] + `, </b>` + data.output[i][1] + `</div><br>
          <div>` + data.output[i][2] + `</div><br>
          <div>` + data.output[i][3] + `</div><br><hr>
      </div>
    `;
    }
  }
  $('#chat-messages').innerHTML = chats;
}