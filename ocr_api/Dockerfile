FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-devel

RUN apt-get update && apt-get install --no-install-recommends -y wget gnupg curl && apt-get install --no-install-recommends -y \
    libgl1 \
    libgomp1 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY ./src /app/src

ENV APP_DIR=/app

CMD ["python3", "./src/main.py"]