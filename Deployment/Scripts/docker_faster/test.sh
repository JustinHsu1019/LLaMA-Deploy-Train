#!/bin/bash

# run.sh

while true; do
    # 提示使用者輸入問題
    echo "User: "
    read user_input

    # 將問題格式化為JSON格式的inputs
    inputs="A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user questions. USER: $user_input ASSISTANT: "

    start_time=$(date +%s.%N)

    # 使用curl命令發送請求
    curl 127.0.0.1:8080/generate \
        -X POST \
        -d "{\"inputs\":\"$inputs\",\"parameters\":{\"max_new_tokens\":1024}}" \
        -H 'Content-Type: application/json'

    # 記錄結束時間
    end_time=$(date +%s.%N)

    # 計算並輸出執行時間
    elapsed_time=$(echo "$end_time - $start_time" | bc)
    echo -e "\nExecution time: $elapsed_time seconds"

    echo ""  # 空行分隔回答和下一次的提示
done

