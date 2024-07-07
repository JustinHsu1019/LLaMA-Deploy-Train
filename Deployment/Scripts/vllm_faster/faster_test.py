from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time

model_name = "E:\\model\\models--yentinglin--Taiwan-LLaMa-v1.0\\snapshots\\55d346ffb1ae7796bcb30c7562d4d10c8ce33463"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.bfloat16,
    device_map="auto",
    low_cpu_mem_usage=True,
    bnb_4bit_compute_dtype=torch.bfloat16
).half()

torch.no_grad()

torch.backends.cudnn.benchmark = True

model.gradient_checkpointing_enable()
model.eval()

tokenizer.pad_token = tokenizer.eos_token

device = "cuda"

def chat(text, max_new_tokens, temperature, top_p, top_k):
    prompt_f = f"""
    A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. 
    USER: {text} 
    ASSISTANT:
    """
    inputs = tokenizer(prompt_f, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, temperature=temperature, top_p=top_p, top_k=top_k)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.replace(prompt_f, "")
    return response

if __name__ == "__main__":
    max_new_tokens = 1024
    temperature = 0
    top_p = 0.9
    top_k = 50

    while True:
        user_input = input("User: ")
        start_time = time.time()
        print("LLama: " + chat(user_input, max_new_tokens, temperature, top_p, top_k))
        end_time = time.time()
        elapsed_time = end_time - start_time 
        print(f"執行時間: {elapsed_time} 秒")
