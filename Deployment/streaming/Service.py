# 同一 Session 隊列問題 未解決 (可嘗試用 for 迴圈中判斷再暫停的機制試試)
# 多人併發已可呈現, 百人併發 (10秒內, 10 loops) 速度問題 Streaming 還未測試

from flask import Flask, request
from flask_socketio import SocketIO
import LLama_Run as LR
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type, Qs-PageCode, Cache-Control'

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    """Server 是否正常的確認頁面.
    """
    return "server is ready v1.1.0"

@socketio.on('connect')
def on_connect():
    LR.on_connect(request)

@socketio.on('disconnect')
def on_disconnect():
    LR.on_disconnect(request)

@socketio.on('generate')
def handle_generate(data):
    LR.chat(data, request, socketio)

def returnMsg(response):
    print(response)
    return response

if __name__ == '__main__':
    # 加入 allow_unsafe_werkzeug=True
    socketio.run(app, host="0.0.0.0", allow_unsafe_werkzeug=True, port=9640, debug=True)
