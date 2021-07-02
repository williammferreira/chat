// document.addEventListener("DOMContentLoaded", function () {
//   if (this.location.pathname == '~/' || this.location.pathname == '~/newchat') {
//     searchWebsocket();
//   } else {
//     messageWebsocket();
//   }
// });

// function searchWebsocket() {
//   window.searchSocket = new WebSocket('ws://127.0.0.1:8000/ws/search');

//   searchSocket.onopen = function () {
//     sendNotification("connected!");
//     document.getElementById('searchInput').innerHTML = '';
//     window.searchSocket.send('fdhgh');
//   }

//   searchSocket.onmessage = function (rawData) {
//     var data = JSON.parse(rawData.data);
//     var chats = ``;
//     for (i in data.output) {
//       chats += `
//       <input type="text" name="" value="" class="search-input" placeholder="search by description" id="searchInput" onkeypress="searchChats()"><hr>
//       <div class="chat" onclick="replace(` + data.output.locationUrl + `)">
//           <div class="title"><b>` + data.output.chatCreator + `, </b>` + data.output.chatUsers + `</div><br>
//           <div>` + data.output.chatDescription + `</div><br>
//           <div>` + data.output.chatDateCreated + `</div><br><hr>
//       </div>
//     `;
//     }
//     document.getElementById('chats').innerHTML = chats;
//   }
// }

// function messageWebsocket() {
//   searchWebsocket();
//   const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/' + document.getElementById('token').textContent.substring(1, (document.getElementById('token').textContent.length - 1)));
//   username = document.getElementById('username').textContent.slice(1, -1);
//   chatSocket.onopen = function () {
//     document.getElementById("message-area").scrollTop = document.getElementById("message-area").scrollHeight;
//     sendNotification("connected!");
//   }

//   chatSocket.onmessage = function (rawData) {
//     var data = JSON.parse(rawData.data);
//     if (data.number == 0) {
//       document.getElementById('message-area').innerHTML = '';
//     }


//     if (data.creator == username) {
//       var creator = 'Me';
//       document.getElementById('message-area').innerHTML += `
//     <div class='message mymessage'>
//       <div class='message-info'>
//         <em>` + creator + `</em><br>
//         <em>` + data.date + `</em>
//       </div>
//       <p>` + data.message + `</p>
//     </div>
//   `;
//       document.getElementById("message-area").scrollTop = document.getElementById("message-area").scrollHeight;
//     } else {
//       var creator = data.creator;
//       document.getElementById('message-area').innerHTML += `
//     <div class='message othermessage'>
//       <div class='message-info-other'>
//         <em>` + creator + `</em><br>
//         <em>` + data.date + `</em>
//       </div>
//       <p>` + data.message + `</p>
//     </div>
//   `;
//       document.getElementById("message-area").scrollTop = document.getElementById("message-area").scrollHeight;
//     }

//   }

//   chatSocket.onclose = function (closeCode) {
//     if (closeCode.code == 1000) {
//       sendNotification("connecting...");
//     } else {
//       sendNotification("The chat socket closed unexpectedly.", "red", "400px");
//       document.getElementById("message-area").innerHTML = "";
//       console.log(closeCode.code, closeCode.reason);
//     }
//   }
// }

const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/' + document.getElementById('token').textContent.substring(1, (document.getElementById('token').textContent.length - 1)));
username = document.getElementById('username').textContent.slice(1, -1);
chatSocket.onopen = function () {
  document.getElementById("message-area").scrollTop = document.getElementById("message-area").scrollHeight;
  sendNotification("connected!");
}

chatSocket.onmessage = function (rawData) {
  var data = JSON.parse(rawData.data);
  if (data.number == 0) {
    document.getElementById('message-area').innerHTML = '';
  }


  if (data.creator == username) {
    var creator = 'Me';
    document.getElementById('message-area').innerHTML += `
      <div class='message mymessage'>
        <div class='message-info'>
          <em>` + creator + `</em><br>
          <em>` + data.date + `</em>
        </div>
        <p>` + data.message + `</p>
      </div>
    `;
    document.getElementById("message-area").scrollTop = document.getElementById("message-area").scrollHeight;
  } else {
    var creator = data.creator;
    document.getElementById('message-area').innerHTML += `
      <div class='message othermessage'>
        <div class='message-info-other'>
          <em>` + creator + `</em><br>
          <em>` + data.date + `</em>
        </div>
        <p>` + data.message + `</p>
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