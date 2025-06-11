FROM python:3.10-slim

WORKDIR /app

COPY ai_client.py .
COPY ai_model.py .

RUN pip install transformers torch

CMD ["python", "ai_client.py"]