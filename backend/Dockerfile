# ---------- Stage 1: Build ----------
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.12-slim

RUN useradd -m appuser
WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY app.py .

USER appuser
EXPOSE 5000

CMD ["python", "app.py"]
