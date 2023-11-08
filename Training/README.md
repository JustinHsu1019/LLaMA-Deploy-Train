# LLaMA 模型訓練環境安裝

### [LLaMA 模型訓練框架 (點擊查看)](https://github.com/JustinHsu1019/LLaMA-Training.git)

#### My Cuda Version: 11.8

#### My Torch Version: 2.0.1

## 安裝 (Admin Anaconda Powershell)
1. git clone [https://github.com/JustinHsu1019/LLaMA-Training.git](https://github.com/JustinHsu1019/LLaMA-Training.git)
2. conda create -n llama-training python=3.10
3. conda activate llama-training
4. cd LLaMA-Training
5. pip install -r requirements.txt
6. pip uninstall torch
7. pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)

## 測試 Cuda, Torch Version
- nvidia-smi
- nvcc -V

- python
1. import torch
2. print(torch.version.cuda)
3. print(torch.cuda.is_available())

## 執行 (開始訓練模型)

### [可視化界面 (Gradio)](/Training/Scripts/run_web.sh)
1. .\shell.w32-ix86\sh.exe .\run_web.sh
2. run_web.sh:  
```bash
CUDA_VISIBLE_DEVICES=0 python src/train_web.py
```

### [指令介面](/Training/Scripts/run_bash.sh)
1. .\shell.w32-ix86\sh.exe .\run_bash.sh
2. run_bash.sh:  
```bash
CUDA_VISIBLE_DEVICES=1 python src/train_bash.py \
    --stage sft \
    --model_name_or_path "E:\models-Llama2-Chinese-7b-Chat" \
    --do_train \
    --dataset self_cognition \
    --template default \
    --lora_target '[q_proj,k_proj,v_proj,o_proj]' \
    --finetuning_type lora \
    --output_dir e50_1108 \
    --overwrite_cache \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_strategy epoch \
    --evaluation_strategy epoch \
    --save_strategy epoch \
    --val_size 0.1 \
    --learning_rate 5e-5 \
    --num_train_epochs 50.0 \
    --plot_loss True \
    --fp16
```
