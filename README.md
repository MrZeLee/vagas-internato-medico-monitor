# Vagas Monitor

A Python application that monitors healthcare job vacancies in Braga, Portugal, and sends SMS notifications when changes are detected using Twilio.

## Description

This application periodically checks for changes in medical job vacancies at "Unidade Local de Saúde Braga, E.P.E." through the official healthcare API. When changes are detected, it sends SMS notifications via Twilio to keep you informed of new opportunities.

## Features

- Monitors healthcare job vacancies in real-time
- Caches results to detect changes
- Sends SMS notifications via Twilio
- Can be run locally or deployed to Kubernetes
- Supports environment-based configuration

## Prerequisites

- Python 3.9+
- Twilio account with:
  - Account SID
  - Auth Token
  - Messaging Service SID
  - Verified phone number

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd vagas-monitor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Twilio credentials:
```env
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_MESSAGING_SERVICE_SID=your_messaging_service_sid_here
TWILIO_TO_NUMBER=your_phone_number_here
```

## Usage

### Local Development

Run the monitor:
```bash
python vagas_monitor.py
```

Test SMS notification:
```bash
python vagas_monitor.py test
```

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t your-registry/vagas-monitor:latest .
```

2. Push to your registry:
```bash
docker push your-registry/vagas-monitor:latest
```

3. Run with docker:

```bash
docker run \
-e TWILIO_ACCOUNT_SID="$TWILIO_ACCOUNT_SID" \
-e TWILIO_AUTH_TOKEN="$TWILIO_AUTH_TOKEN" \
-e TWILIO_MESSAGING_SERVICE_SID="$TWILIO_MESSAGING_SERVICE_SID" \
-e TWILIO_TO_NUMBER="$TWILIO_TO_NUMBER" \
-v $(pwd)/data:/app/data
your-registry/vagas-monitor
```

or

```bash
docker run --env-file=.env -v $(pwd)/data:/app/data vagas-monitor
```

### Kubernetes Deployment

1. Update the secrets in `k8s-cronjob.yaml` with your Twilio credentials

2. Apply the Kubernetes manifests:
```bash
kubectl apply -f k8s-cronjob.yaml
kubectl apply -f k8s-persistence.yaml  # If using persistence
```

## Configuration

The application can be configured using environment variables:

- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
- `TWILIO_MESSAGING_SERVICE_SID`: Your Twilio Messaging Service SID
- `TWILIO_TO_NUMBER`: The phone number to receive notifications

## Cache

The application maintains a JSON cache file to track changes in vacancies. In Kubernetes, this can be persisted using a PersistentVolumeClaim.

