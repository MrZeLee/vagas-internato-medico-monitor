from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_MESSAGING_SERVICE_SID = os.getenv('TWILIO_MESSAGING_SERVICE_SID')
TWILIO_TO_NUMBER = os.getenv('TWILIO_TO_NUMBER')

# API configuration
API_URL = 'https://vagasconcursoim-acss.min-saude.pt/WCF/VagasService.asmx/GetCurrentVagasByRegion'
HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://vagasconcursoim-acss.min-saude.pt',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

