import requests
import time

while True:

    user_input = input("User: ")

    inputs = f"""
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user questions. 
USER: {user_input} 
ASSISTANT: 
"""

    start_time = time.time()

    response = requests.post(
        "http://127.0.0.1:8080/generate",
        json={"inputs": inputs, "parameters": {"max_new_tokens": 4096}},
        headers={'Content-Type': 'application/json'}
    )

    print(response.json())

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"\nExecution time: {elapsed_time:.2f} seconds\n")
