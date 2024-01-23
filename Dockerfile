FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG DATABASE_NAME
ARG DATABASE_USER
ARG DATABASE_PASSWORD
ARG DATABASE_HOST
ARG DATABASE_PORT
ARG SECRET_KEY

ENV DATABASE_NAME $DATABASE_NAME
ENV DATABASE_USER $DATABASE_USER
ENV DATABASE_PASSWORD $DATABASE_PASSWORD
ENV DATABASE_HOST $DATABASE_HOST
ENV DATABASE_PORT $DATABASE_PORT
ENV SECRET_KEY $SECRET_KEY

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
