model=yentinglin/Taiwan-LLaMa-v1.0
volume=$PWD/data 

docker run --rm \
	--name tgi \
	--runtime=nvidia \
	--gpus all \
	--shm-size 1g \
	-p 8080:8080 \
	-v $volume:/data \
	ghcr.io/huggingface/text-generation-inference:1.0.2 \
	--model-id $model \
	--hostname 0.0.0.0 \
	--port 8080 \
	--dtype float16 \
	--quantize \
	--sharded false