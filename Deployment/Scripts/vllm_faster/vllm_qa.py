from transformers import AutoTokenizer
import time
from vllm import LLM, SamplingParams

model_name = "yentinglin/Taiwan-LLaMa-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

sampling_params = SamplingParams(max_tokens=4096, temperature=0, top_p=1)

llm = LLM(
    model=model_name,
    trust_remote_code=True,
    dtype = "float16",
)

def chat(text, max_length, temperature, top_p, repetition_penalty):
    prompt_f = f"""
    A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.
    USER: {text}
    ASSISTANT:
    """
    outputs = llm.generate([prompt_f], sampling_params)
    response = outputs[0].outputs[0].text
    response = response.replace(prompt_f, "")
    return response

if __name__ == "__main__":
    while True:
        user_input = input("User: ")

        user_input_tokens = len(tokenizer.tokenize(user_input))

        start_time = time.time()
        response = chat(user_input)

        response_tokens = len(tokenizer.tokenize(response))

        total_tokens = user_input_tokens + response_tokens

        end_time = time.time()
        elapsed_time = end_time - start_time

        tokens_per_second = total_tokens / elapsed_time

        print("LLama: " + response)
        print(f"執行時間: {elapsed_time} 秒")
        print(f"每秒處理的tokens: {tokens_per_second}")