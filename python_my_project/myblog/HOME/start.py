from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")  #도메인
def index() : 
  return send_from_directory('THEME', "index.html") # 127.0.0.1/html/css/b.css

@app.route('/<path:name>')  #도메인/css/b.css
def start(name) : 
  return send_from_directory('THEME', name) #도메인/THEME/css/b.css