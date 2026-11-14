FROM python:3.11-slim

WORKDIR /app

RUN groupadd -g 10001 raguser && \
    useradd -u 10001 -g raguser -s /bin/false raguser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

RUN chown -R raguser:raguser /app
USER 10001:10001

ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/healthz')" || exit 1

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
