FROM python:3.9-slim

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY vagas_monitor.py .
COPY config.py .

# Create the cron job and install it
RUN echo "*/5 * * * * . /etc/environment; cd /app && /usr/local/bin/python /app/vagas_monitor.py >> /var/log/cron.log 2>&1" > /etc/cron.d/vagas-monitor
RUN chmod 0644 /etc/cron.d/vagas-monitor
RUN crontab /etc/cron.d/vagas-monitor

# Create the log file and set permissions
RUN touch /var/log/cron.log && chmod 0666 /var/log/cron.log

ENV PYTHONUNBUFFERED=1

# Create a startup script
RUN echo '#!/bin/sh\n\
# Store environment variables for cron\n\
printenv | grep -v "no_proxy" > /etc/environment\n\
echo "Starting cron service..."\n\
service cron restart\n\
echo "Cron service restarted"\n\
echo "Printing logs"\n\
tail -f /var/log/cron.log' > /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
