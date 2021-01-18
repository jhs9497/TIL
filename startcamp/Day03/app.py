from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#http://127.0.0.1:5000/name     #127.0.0.1 = local host = 내 컴퓨터, 즉 나만 볼 수 있는 서버 (개발서버)

@app.route('/name')
def name():
    return '안녕하세요, 조현식입니다!'