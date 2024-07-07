import vllm_qa

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type, Qs-PageCode, Cache-Control'

@app.route("/")
def index():
    """Server 是否正常的確認頁面.
    """
    return "server is ready v1.1.0"

@app.route('/llama2qa', methods=['POST', 'GET'])
def llama2qa():
    if request.method == 'POST':
        data = request.json
    
        question = data.get("question")
        max_length = data.get("max_length")
        temperature = data.get("temperature")
        top_p = data.get("top_p")
        repetition_penalty = data.get("repetition_penalty")

        if not question:
            response = "無問題 (無內容_llama)"
        else:
            try:
                response = vllm_qa.chat(question, max_length, temperature, top_p, repetition_penalty)
            except Exception as e:
                print(f"get error (llama): {e}")
                response = f"Error (llama): {e}"

        return returnMsg(response)

    else:
        return "無問題 (GET_llama)"

def returnMsg(response):
    print(response)
    return response

# print("server is ready.")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9639, threaded=True)
