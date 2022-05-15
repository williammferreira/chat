var searchSocket;

if (window.location.protocol === "https") {
    searchSocket = new WebSocket('wss://' + window.location.host + '/ws/search');
} else {
    searchSocket = new WebSocket('ws://' + window.location.host + '/ws/search');
}

searchSocket.onopen = function () {
    sendNotification("connected!");
}

searchSocket.onmessage = function (rawData) {
    var data = JSON.parse(rawData.data);
    var chats = ``;
    if ((data.output).length == 0) {
        chats = `<p class='no-chats-search' style='font-size: 15px;'><i>No chats match your search.</i></p>`;
    } else {
        // 0=creator 1=users 2=description 3=created 4=location 5=token
        for (var i = 0; i < (data.output).length; i++) {
            chats += `
      <div class="chat" onclick="replace('/~/chats/` + data.output[i][4] + `')">
          <span class="title"><b>` + data.output[i][0] + `, </b>` + data.output[i][1] + `</span><br>
          <span>` + data.output[i][2] + `</span><br>
          <span>` + data.output[i][3] + `</span><br>
      </div>
    `;
        }
    }
    $('#chat-messages').innerHTML = chats;
}