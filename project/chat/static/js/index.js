// function setCookie(cname,cvalue,exdays) {
//   var d = new Date();
//   d.setTime(d.getTime() + (exdays*24*60*60*1000));
//   var expires = "expires=" + d.toGMTString();
//   document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
// 	location.reload;
// }

// function getCookie(cname) {
//   var name = cname + "=";
//   var decodedCookie = decodeURIComponent(document.cookie);
//   var ca = decodedCookie.split(';');
//   for(var i = 0; i < ca.length; i++) {
//     var c = ca[i];
//     while (c.charAt(0) == ' ') {
//       c = c.substring(1);
//     }
//     if (c.indexOf(name) == 0) {
//       return c.substring(name.length, c.length);
//     }
//   }
//   return "";
// }

// function checkCookie() {
//   var user=getCookie("username");
//   if (user != "") {
//     document.getElementById("name").innerHTML = user;
//   } else {
//      user = prompt("What do you want people to call you?","William Ferreira");
//      if (user != "" && user != null) {
//        setCookie("username", user, 30);
//      }
//   }
// }
alert("wow")

var input = document.getElementById("myInput");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
   event.preventDefault();
   document.getElementById("myBtn").click();
	 document.getElementById("myInput").innerHTML = "";
  }
});

function mess(){
  if (delay && messageInput.value.replace(/\s/g, "") != ""){
    delay = false;
    setTimeout(delayReset, 1000);
    socket.emit("send", messageInput.value);
    messageInput.value = "";
  }
}

document.cookie = "user=index; path=/;";


function openTab(tabName) {
  var i, x;
  x = document.getElementsByClassName("containerTab");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  document.getElementById(tabName).style.display = "block";
}



//const input2 = document.getElementById("input043");
const input2 = document.getElementById("myInput");
const button = document.querySelector(`button[data-post]`);
const textarea = document.getElementById("messageareabox");

function checkInput(event) {
	button.disabled = (input2.value.length == 0);
}

function post() {
	if(input2.value.length > 0) {
		const inputValue = input2.value;
		/*const message = {
			id : socket.id,
			value : inputValue,
		};*/
		const message = {
			id : getCookie("username"),
			value : inputValue,
		};
		socket.emit('message-room', {room, message});
		appendPost(message);
		input2.value = '';
	}
}

function appendPost({id, value}) {
	appendText(`${id == getCookie("username")? "<div id='my-message'>":'<div id="other-message">'}<p style="opacity: 0.5;">${id}</p><br> ${value}`);
	value.className = "container";
}

function appendText(text) {
	textarea.innerHTML += `${text}\n</div>`;
	textarea.scrollTop = textarea.mainHeight;
}

const socket = io("https://socketio-server.codeisamazing.repl.co");
const random = Math.round(Math.random() * 99999999999999999999);
const room = "room";
socket.on('connect', () => {
	socket.emit("join", {room});/*
	//appendText(`user ${socket.id} (YOU) entered the chat`);
	appendText(`user ${socket.id} (YOU) entered the chat`);*/
	socket.on('user-connect', message => {
		console.log('user-connect', message);
	});
	socket.on('message', message => {
		console.log("message", message);
	});

	socket.on('direct-message', message => {
		console.log("direct-message", message);
	});

	socket.on('user-join', message => {
		console.log('user-join', message);

		const {id} = message;
		//appendText(`user ${id} entered the chat`);
			});

	socket.on('message-room', message => {
		appendPost(message);
	});
			
	socket.on('user-leave', message => {
		console.log('user-leave', message);

		const {id} = message;
		//appendText(`user ${id} left the chat`);
	});

	socket.on('user-disconnect', message => {
		console.log('user-disconnect', message);
	});
});

window.onbeforeunload = function(event) {
  event.returnValue = "Write something clever here..";
};