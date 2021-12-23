const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + $('#token').textContent.substring(1, ($('#token').textContent.length - 1)));
username = $('#username').textContent.slice(1, -1);
chatSocket.onopen = function () {
  $("#message-area").scrollTop = $("#message-area").scrollHeight;
  sendNotification("connected!");
}

chatSocket.onmessage = function (rawData) {
  var data = JSON.parse(rawData.data);
  if (data.number == 0) {
    $('#message-area').innerHTML = '';
  }


  if (data.creator == username) {
    var creator = 'Me';
    $('#message-area').innerHTML += `
      <div class='message mymessage'>
        <div class='message-info'>
          <em>` + creator + `</em><br>
          <em>` + data.date + `</em>
        </div>
        <p>` + data.message + `</p>
      </div>
    `;
    $("#message-area").scrollTop = $("#message-area").scrollHeight;
  } else {
    var creator = data.creator;
    $('#message-area').innerHTML += `
      <div class='message othermessage'>
        <div class='message-info-other'>
          <em>` + creator + `</em><br>
          <em>` + data.date + `</em>
        </div>
        <p>` + data.message + `</p>
      </div>
    `;
    $("#message-area").scrollTop = $("#message-area").scrollHeight;
  }

}

chatSocket.onclose = function (closeCode) {
  if (closeCode.code == 1000) {
    sendNotification("connecting...");
  }

  else {
    sendNotification("The chat socket closed unexpectedly.", "red", "400px");
    $("#message-area").innerHTML = "";
    console.log(closeCode.code, closeCode.reason);
  }
}