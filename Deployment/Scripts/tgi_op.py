import requests
# import time

def chat(user_input):
    input_ = f"""
A chat between a curious user and an artificial intelligence assistant.
The assistant gives helpful, detailed, and polite answers to the user questions. 
USER: {user_input} 
ASSISTANT: 
"""
    # start_time = time.time()
    response = requests.post(
        "http://127.0.0.1:8080/generate",
        json={"inputs": input_, "parameters": {"max_new_tokens": 1024, "temperature": 0.1}},
        headers={'Content-Type': 'application/json'}
    )
    response = response.json()
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(f"\nExecution time: {elapsed_time:.2f} seconds\n")
    return str(response['generated_text'])

if __name__ == "__main__":
    quest = input(">> ")
    print(chat(quest))
