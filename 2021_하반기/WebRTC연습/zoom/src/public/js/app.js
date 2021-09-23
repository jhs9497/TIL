//socket.io를 실행하고 있는 백서버를 자동으로 찾아 연결해주는 함수 io()
const socket = io();

const welcome = document.getElementById("welcome")
const room = document.getElementById("room");
const form = welcome.querySelector("form")

room.hidden = true;

function addMessage(msg) {
  const ul = room.querySelector("ul");
  const li = document.createElement("li");
  li.innerText = msg;
  ul.appendChild(li);
}

function handleMessageSubmit(event) {
  event.preventDefault();
  const input = room.querySelector("#msg input");
  const value = input.value
  socket.emit("new_message", input.value, room, () => {
    addMessage(`You: ${value}`);
  });
  input.value = ""
}

function handleNicknameSubmit(event) {
  event.preventDefault();
  const input = room.querySelector("#nickname input");
  socket.emit("nickname", input.value)
}

function showRoom(msg) {
  const roomMsg = room.querySelector("h2")
  roomMsg.innerText = `${msg}방에 입장하신 것을 환영합니다!`;
  welcome.hidden = true;
  room.hidden = false;
  const msgForm = room.querySelector("#msg");
  const nameForm = room.querySelector("#nickname");
  msgForm.addEventListener("submit", handleMessageSubmit);
  nameForm.addEventListener("submit", handleNicknameSubmit);
}


const handleRoomSubmit = (event) => {
  event.preventDefault();
  const input = form.querySelector("input");
  // JSON화 할 필요없이 object형태로 바로 보낼 수 있음 (모든type전송 가능 심지어 여러개도 가능!)
  // 심지어 마지막 인자에는 서버에서 호출하는 fn 들어갈 수 있음!!, FE에서 실행됨
  socket.emit("enter_room", input.value, showRoom);
  input.value = ""
}

form.addEventListener("submit", handleRoomSubmit);

socket.on("welcome", (user, newCount) => {
  const roomMsg = room.querySelector("h2");
  roomMsg.innerText = `${user}방 현재인원: ${newCount}명`;
  addMessage(`${user} 들어왔음!`);
})

socket.on("bye", (user, newCount) => {
  const roomMsg = room.querySelector("h2");
  roomMsg.innerText = `${user}방 현재인원: ${newCount}명`;
  addMessage(`${user} 떠났음ㅜㅜ`);
})

socket.on("new_message", (msg) => {
  addMessage(msg);
});

socket.on("room_change", (roomList) => {
  const rooms = welcome.querySelector('ul')
  rooms.innerHTML = "";
  if (roomList.length === 0) {
    return;
  }
  roomList.forEach((room) => {
    const li = document.createElement("li");
    li.innerText = room;
    rooms.append(li);
  });
});