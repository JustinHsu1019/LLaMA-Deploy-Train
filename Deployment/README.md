# LLaMA 模型部署環境安裝 (Linux)

## 安裝 Docker
1. sudo apt update
2. sudo apt install apt-transport-https ca-certificates curl software-properties-common
3. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
4. sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
5. apt-cache policy docker-ce
6. sudo apt install docker-ce
7. sudo usermod -aG docker ${USER}
8. sudo systemctl start docker
9. sudo systemctl enable docker

## 安裝 GPU Driver
1. sudo apt update
2. sudo apt upgrade
3. ubuntu-drivers devices
4. sudo ubuntu-drivers autoinstall
5. sudo reboot

## 安裝 Nvidia-Docker
1. curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
2. distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
3. curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
4. sudo apt-get install -y nvidia-docker2
5. sudo systemctl restart docker
6. vim /etc/docker/daemon.json
```json
{
  "default-runtime": "nvidia",
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  }
}
```
7. sudo systemctl restart docker

## [運行 TGI 部署腳本](/Deployment/Scripts/run.sh)
1. vim run.sh
```bash
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
```
2. sh run.sh

## [測試模型](/Deployment/Scripts/LLaMA_QA.py)
1. python Scripts/LLaMA_QA.py
2. Input something ...

## [運行 Python 部署腳本](/Deployment/Scripts/Service.py)
1. python Scripts/Service.py
2. 使用 PostMan 測試 API
3. 撰寫前端網頁來實際體驗!
