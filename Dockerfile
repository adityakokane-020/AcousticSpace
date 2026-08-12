FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN grep -vE '^(torch|torchvision)([<=>].*)?$' requirements.txt > requirements-docker.txt && \
    pip install --no-cache-dir -r requirements-docker.txt && \
    pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu torch torchvision

COPY backend ./backend
COPY ml ./ml

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]