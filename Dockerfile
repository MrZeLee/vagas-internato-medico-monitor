FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY vagas_monitor.py .
COPY config.py .

CMD ["python", "vagas_monitor.py"]
