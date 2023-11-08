model=yentinglin/Taiwan-LLaMa-v1.0
volume=$PWD/data
docker run --rm \
  --name tgi \
  --runtime=nvidia \
  --gpus all \
  --shm-size 1g \
  -p 8080:8080 \
  -v $volume:/data \
  ghcr.io/huggingface/text-generation-inference:1.0.3 \
  --model-id $model \
  --hostname 0.0.0.0 \
  --port 8080 \
  --dtype bfloat16 \
  --sharded true \
  --num-shard 2 \
  --max-total-tokens 4000 \
  --max-input-length 2500
