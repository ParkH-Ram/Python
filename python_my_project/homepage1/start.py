from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")  # 127.0.0.1 
def index():
    return send_from_directory('html', 'index.html') #127.0.0.1:5000/html/index


@app.route("/hello")  # 127.0.0.1:500/hello
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<path:name>")  # 127.0.0.1 / path:name << 에 모든 내용이 들어감
def start(name):
    return send_from_directory('html', name) #127.0.0.1/html/css/b.css
