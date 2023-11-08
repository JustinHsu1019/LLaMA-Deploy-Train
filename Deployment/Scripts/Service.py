import LLaMA_QA

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type, Qs-PageCode, Cache-Control'

@app.route("/")
def index():
    """Server 是否正常的確認頁面.
    """
    return "server is ready"

@app.route('/llama2qa', methods=['POST', 'GET'])
def llama2qa():
    if request.method == 'POST':
        data = request.json
    
        question = data.get("question")

        if not question:
            response = "無內容"
        else:
            try:
                response = LLaMA_QA.chat(question)
            except Exception as e:
                print(f"get error: {e}")
                response = f"Error: {e}"

        return returnMsg(response)

    else:
        return "無問題"

def returnMsg(response):
    print(response)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, threaded=True)
