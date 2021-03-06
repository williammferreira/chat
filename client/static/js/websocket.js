const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/room/' + document.getElementById('token').textContent.substring(1, (document.getElementById('token').textContent.length - 1)));
username = document.getElementById('username').textContent.slice(1, -1);
chatSocket.onopen = function () {
    document.getElementById("message-area").scrollTop = document.getElementById("message-area").scrollHeight;
    sendNotification("connected!");
}

chatSocket.onmessage = function (rawData) {
    var data = JSON.parse(rawData.data);
    console.log(data.number);
    if (data.number == 0) {
        document.getElementById('message-area').innerHTML = '';
    }


    if (data.creator == username) {
        var creator = 'Me';
        document.getElementById('message-area').innerHTML += `
        <div class="message-wrapper message-wrapper-self">
      <div class='message mymessage'>
        <div class='message-info'>
          <em>` + creator + `</em><br>
          <em>` + data.date + `</em>
        </div>
        <p>` + data.message + `</p>
      </div>
      </div>
    `;
        document.getElementById("message-area").scrollTop = document.getElementById("message-area").scrollHeight;
    } else {
        var creator = data.creator;
        document.getElementById('message-area').innerHTML += `
        <div class="message-wrapper message-wrapper-other">
      <div class='message othermessage'>
        <div class='message-info-other'>
          <em>` + creator + `</em><br>
          <em>` + data.date + `</em>
        </div>
        <p>` + data.message + `</p>
      </div>
      </div>
    `;
        document.getElementById("message-area").scrollTop = document.getElementById("message-area").scrollHeight;
    }

}

chatSocket.onclose = function (closeCode) {
    if (closeCode.code == 1000) {
        sendNotification("connecting...");
    }

    else {
        sendNotification("The chat socket closed unexpectedly.", "red", "400px");
        document.getElementById("message-area").innerHTML = "";
        console.log(closeCode.code, closeCode.reason);
    }
}