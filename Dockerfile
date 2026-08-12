FROM python:3.11-slim

WORKDIR /app

COPY requirements-docker.txt .

RUN pip install --no-cache-dir -r requirements-docker.txt

RUN pip install --no-cache-dir \
    torch==2.12.1 \
    torchvision==0.27.1 \
    --index-url https://download.pytorch.org/whl/cpu

COPY backend ./backend
COPY ml ./ml

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]