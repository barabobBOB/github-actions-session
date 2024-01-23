FROM python:3.10

WORKDIR /app

# requirements.txt 파일 먼저 복사
COPY requirements.txt /app

# pip 업그레이드 및 필요한 패키지 설치
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 애플리케이션 파일 복사
COPY . /app/

# 필요한 시스템 패키지 설치 및 정리
RUN apt-get update && \
    apt-get install --no-install-recommends -y libgl1-mesa-glx build-essential && \
    rm -rf /var/lib/apt/lists/*
