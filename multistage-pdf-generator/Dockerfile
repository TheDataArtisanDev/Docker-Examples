# Stage 1 - Builder
FROM python:3.11-slim AS builder

WORKDIR /install

COPY app/requirements.txt .
RUN pip install --prefix=/install/python-packages -r requirements.txt

# Stage 2 - Runtime
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install/python-packages /usr/local
COPY app /app

EXPOSE 5000

CMD ["python", "app.py"]
