// tensorflow.js
let video = document.getElementById("myFace")
let canvas = document.getElementById("canvas")
let ctx = canvas.getContext("2d");
let model;


const socket = io();

const myFace = document.getElementById("myFace");
const muteBtn = document.getElementById("mute");
const cameraBtn = document.getElementById("camera");
const cameraSelect = document.getElementById("cameras");

const call = document.getElementById("call");

call.hidden = true;

let myStream;
let muted = false;
let cameraOff = false;
let roomName;
let myPeerConnection;

async function getCameras() {
  try {
    const devices = await navigator.mediaDevices.enumerateDevices();
    const cameras = devices.filter(device => device.kind ==="videoinput");
    const currentCamera = myStream.getVideoTracks()[0];
    cameras.forEach(camera => {
      const option = document.createElement("option");
      option.value = camera.deviceId;
      option.innerText = camera.label;
      if (currentCamera.label === camera.label) {
        option.selected = true;
      }
      cameraSelect.appendChild(option);
    })
  } catch (e) {
    console.log(e);
  }
}

async function getMedia(deviceId) {
  const initialConstraints = {
    audio: true,
    video: { facingMode: "user" },
    // video : { facingMode : "user" } -> 자동으로 셀카 선택
  };
  const cameraConstraints = {
    audio: true,
    video: { deviceId: { exact: deviceId } },
  };
  try {
    myStream = await navigator.mediaDevices.getUserMedia(
      deviceId ? cameraConstraints : initialConstraints
    );
    myFace.srcObject = myStream;
    if (!deviceId) {
      await getCameras();
    }
  } catch (e) {
    console.log(e);
  }
}

// getMedia();

function handleMuteClick() {
  myStream.getAudioTracks().forEach((track) => (track.enabled = !track.enabled));
  if(!muted){
    muteBtn.innerText = "Unmute"
    muted = true;
  } else {
    muteBtn.innerText = "Mute";
    muted = false;
  }
}
function handleCameraClick() {
  myStream
    .getVideoTracks()
    .forEach((track) => (track.enabled = !track.enabled));
  if (cameraOff) {
    cameraBtn.innerText = "Turn Camera Off";
    cameraOff = false;
  } else {
    cameraBtn.innerText = "Turn Camera On";
    cameraOff = true;
  }
}

async function handleCameraChange() {
  await getMedia(cameraSelect.value);
  // 카메라를 바꿀 땐 새로운 스트림을 만들어서 재연결을 한다!
  if(myPeerConnection){
    const videoTrack = myStream.getVideoTracks()[0];
    const videoSender = myPeerConnection.getSenders().find(sender => sender.track === "video");
    videoSender.replaceTrack(videoTrack);
  }
}

muteBtn.addEventListener("click", handleMuteClick);
cameraBtn.addEventListener("click", handleCameraClick);
cameraSelect.addEventListener("input", handleCameraChange);


// welcomeForm (join a room)

const welcome = document.getElementById("welcome");
const welcomeForm = welcome.querySelector("form");

async function startMedia() {
  welcome.hidden = true;
  call.hidden = false;
  await getMedia();
  makeConnection();
  // main();
}

async function handleWelcomeSubmit(event) {
  event.preventDefault();
  const input = welcomeForm.querySelector("input");
  await startMedia();
  socket.emit("join_room", input.value);
  roomName = input.value;
  input.value = ""
}

welcomeForm.addEventListener("submit", handleWelcomeSubmit)

// Socket Code

// Peer A에서 실행됨
socket.on("welcome", async () => {
  // 주소 들어있음
  const offer = await myPeerConnection.createOffer();
  myPeerConnection.setLocalDescription(offer);
  socket.emit("offer", offer, roomName);
  console.log("sent the offer");
})

// Peer B에서 실행에서 Peer A가 보낸 offer에 의해 실행됨
socket.on('offer', async (offer) => {
  console.log("received the offer");
  myPeerConnection.setRemoteDescription(offer);
  const answer = await myPeerConnection.createAnswer();
  myPeerConnection.setLocalDescription(answer);
  socket.emit("answer", answer, roomName);
  console.log("sent the answer");
})

// Peer A에서 Peer B가 보낸 answer에 의해 실행됨
socket.on("answer", answer => {
  console.log("received the answer");
  myPeerConnection.setRemoteDescription(answer);
})

socket.on("ice", (ice) => {
  console.log("received candidate");
  myPeerConnection.addIceCandidate(ice);
})

// RTC Code

function makeConnection() {
  myPeerConnection = new RTCPeerConnection({
    iceServers: [
      {
        urls: [
          "stun:stun.l.google.com:19302",
          "stun:stun1.l.google.com:19302",
          "stun:stun2.l.google.com:19302",
          "stun:stun3.l.google.com:19302",
          "stun:stun4.l.google.com:19302",
        ],
      },
    ],
  });
  myPeerConnection.addEventListener("icecandidate", handleIce)
  myPeerConnection.addEventListener("addstream", handleAddstream);
  myStream.getTracks().forEach((track) => myPeerConnection.addTrack(track, myStream));
}

function handleIce(data) {
  console.log("sent candidate")
  socket.emit("ice", data.candidate, roomName);
}

function handleAddstream(data) {
  const peerStream = document.getElementById("peerStream");
  peerStream.srcObject = data.stream;
  console.log("got an event from my peer")
  console.log("남에꺼", data.stream)
  console.log("내꺼", myStream)
}


// tensorflow.js

let flag = true;

const detectFaces = async () => {
  const prediction = await model.estimateFaces(video, false);

  ctx.drawImage(video, 0, 0, 600, 400)

  const img = new Image();
  img.src =
    "data:image/jpeg;base64,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";

  if (flag === true) {  
    prediction.forEach((pred) => {
      ctx.beginPath();
      ctx.lineWidth = "2";
      ctx.strokeStyle = "blue";
      ctx.rect(
        pred.topLeft[0],
        pred.topLeft[1]-50,
        pred.bottomRight[0] - pred.topLeft[0],
        pred.bottomRight[1] - pred.topLeft[1]+50
      );
      ctx.stroke();
      ctx.drawImage(
        img,
        pred.topLeft[0],
        pred.topLeft[1]-50,
        pred.bottomRight[0] - pred.topLeft[0],
        pred.bottomRight[1] - pred.topLeft[1]+50
      );
      })
  }};
  video.addEventListener("loadeddata", async () => {
    model = await blazeface.load();
    setInterval(detectFaces, 200);
});