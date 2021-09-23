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

socketIO.on("connection", socket => {
  socket.on("join_room", (roomName) => {
    socket.join(roomName);
    socket.to(roomName).emit("welcome");
  })
  socket.on("offer", (offer, roomName) => {
    socket.to(roomName).emit("offer", offer);
  });
  socket.on("answer", (answer, roomName) => {
    socket.to(roomName).emit("answer", answer)
  })
  socket.on("ice", (ice, roomName) => {
    socket.to(roomName).emit("ice", ice);
  })
})

httpserver.listen(3000, handleListen);