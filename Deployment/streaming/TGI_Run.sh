# vRam 消耗 20 GiB (指定 GPU 1) 左右
# jMeter: 100 人併發 (十秒內) + 10 loops 回應速度問題 (能否再量化模型 + 多 GPU + 多台 GPU Server)
# quantize 嘗試其他方式 (如：gptq, 原 bitsandbytes ...)

model=yentinglin/Taiwan-LLaMa-v1.0 # MiuLab 微調的 LLama2 (13b)
volume=$PWD/data # /home/ap02/test_docker/data

docker run -d --rm \
        --name tgi \
        --runtime=nvidia \
        --gpus '"device=1"' \
        --shm-size 1g \
        -p 9639:9639 \
        -v $volume:/data \
        ghcr.io/huggingface/text-generation-inference:1.0.3 \
        --model-id $model \
        --hostname 0.0.0.0 \
        --port 9639 \
        --quantize bitsandbytes-fp4 \
        --cuda-memory-fraction 0.3 \
        --sharded false
