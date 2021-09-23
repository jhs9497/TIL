import express from "express";
import { WebSocketServer } from "ws";
import { Server } from "socket.io";
import path from "path";
import http from "http";

const __dirname = path.resolve();
const app = express();

app.set("view engine", "pug");
app.set("views", __dirname + "/src/views");
app.use("/public", express.static(__dirname + "/src/public"));
app.get("/", (req, res) => res.render("home"));
app.get("/*", (req, res) => res.redirect("/"));

const handleListen = () => console.log(`Listening on http:localhost:3000`)

// http, ws 서버 둘다 돌리기 (필수는 아님)
const httpserver = http.createServer(app);
const socketIO = new Server(httpserver);

function publicRooms(){
  const sids = socketIO.sockets.adapter.sids;
  const rooms = socketIO.sockets.adapter.rooms;
  const publicRooms = [];
  rooms.forEach((_, key) => {
    if(sids.get(key) === undefined){
      publicRooms.push(key)
    }
  })
  return publicRooms;
}

function countRoom(roomName) {
  return socketIO.sockets.adapter.rooms.get(roomName)?.size;
}

socketIO.on("connection", (socket) => {
  socket["nickname"] = "Anon"
  // 어떤 이벤트가 일어났는지 체크 가능
  socket.onAny((event) => {
    console.log(socketIO.sockets.adapter)
    console.log(`Socket Event: ${event}`)
  })
  // switch문 필요 없이 분기처리 가능
  // done이란 인자는 BE에서 호출하지만 FE에서 실행됨
  socket.on("enter_room", (roomName, done) => {
    console.log('join전', socket.rooms);
    socket.join(roomName);
    console.log('join후', socket.rooms);
    done(roomName);
    socket.to(roomName).emit("welcome", socket.nickname, countRoom(roomName));

    // 서버에 들어와있는 모든 사람에게 방 생겼다고 말해주기
    socketIO.sockets.emit("room_change", publicRooms());
  });

  // 누군가 나갔을때!
  socket.on("disconnecting", () => {
    socket.rooms.forEach(room => socket.to(room).emit("bye", socket.nickname, countRoom(room)));
    socketIO.sockets.emit("room_change", publicRooms());
  })

  socket.on("new_message", (msg, room, done) => {
    socket.rooms.forEach((room) => socket.to(room).emit("new_message", `${socket.nickname} : ${msg}`));
    done();
  });

  // 닉네임 정하기
  socket.on("nickname", (nickname) => (socket["nickname"]= nickname));
})





// const wss = new WebSocketServer({server});

// const sockets = []; // 브라우저 종류 넣는 곳

// wss.on("connection", (socket) => {
//   sockets.push(socket)
//   socket["nickname"] = "Anon"
//   console.log("서버 연결 성공!");
//   socket.on("message", (message) => {
//     const messageJSON = JSON.parse(message)
//     switch (messageJSON.type) {
//       case "new_message":
//         sockets.forEach((aSocket) => aSocket.send(`${socket.nickname}: ${messageJSON.payload}`));
//         break;
//       case "nickname":
//         socket["nickname"] = messageJSON.payload;
//         break;
//     }
//   })
//   socket.on("close", () => {
//     console.log("브라우저로부터 연결 끊김!")
//   })
// });

httpserver.listen(3000, handleListen);