from huggingface_hub import InferenceClient
from queue import Queue, Empty
import uuid

# Call TGI Docker
client = InferenceClient("http://127.0.0.1:9639")

# 1. 處理多人併發問題 2. 處理單人連發問題
session_queues = {}
latest_request_ids = {}

def on_connect(request):
    session_queues[request.sid] = Queue()

def on_disconnect(request):
    if request.sid in session_queues:
        del session_queues[request.sid]

def chat(data, request, socketio):
    user_input = data.get('user_input')

    if not user_input:
        socketio.emit('response', {'error': '輸出不可為空'}, room=request.sid)
        return

    new_request_id = str(uuid.uuid4())
    latest_request_ids[request.sid] = new_request_id

    session_queues[request.sid].put((user_input, new_request_id))
    process_queue(request.sid, socketio)

def process_queue(session_id, socketio):
    try:
        user_input, request_id = session_queues[session_id].get_nowait()
    except Empty:
        return

    inputs = f"""
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user questions.
USER: {user_input}
ASSISTANT:
"""

    try:
        # TGI Streaming 呈現 (參數: stream=True)
        # 嘗試在 for 迴圈內加入判斷機制確認同一 User 是否有下一請求進入，若有，就跳出迴圈
        for token in client.text_generation(inputs, max_new_tokens=1024, temperature=0.1, stream=True):
            if request_id != latest_request_ids.get(session_id):
                return
            socketio.emit('response', {'data': token}, room=session_id)
    except:
        socketio.emit('response', {'error': '無法連線'}, room=session_id)

    process_queue(session_id, socketio)
