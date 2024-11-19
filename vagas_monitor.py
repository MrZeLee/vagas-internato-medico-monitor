import json
import requests
from twilio.rest import Client
from pathlib import Path
from config import *

class VagasMonitor:
    def __init__(self):
        self.cache_file = Path('vagas_cache.json')
        self.cached_data = self.load_cache()
        self.twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def load_cache(self):
        if self.cache_file.exists():
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_cache(self, data):
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def send_notification(self, institution, old_value, new_value):
        message = (
            f"Changes detected for {institution}!\n"
            f"Previous vacancies: {old_value}\n"
            f"Current vacancies: {new_value}"
        )
        self.twilio_client.messages.create(
            body=message,
            messaging_service_sid=TWILIO_MESSAGING_SERVICE_SID,
            to=TWILIO_TO_NUMBER
        )

    def fetch_vagas(self):
        payload = {
            "pData": ["Norte", "MEDICINA GERAL E FAMILIAR"]
        }
        
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()

    def check_vagas(self):
        try:
            data = self.fetch_vagas()
            
            for vaga in data['d']:
                if 'Unidade Local de Saúde Braga, E.P.E.' in vaga['Instituicao']:
                    institution = vaga['Instituicao']
                    current_vagas = vaga['VagasCurrent']
                    
                    # Check if we have cached data for this institution
                    if institution in self.cached_data:
                        cached_vagas = self.cached_data[institution]
                        if cached_vagas != current_vagas:
                            self.send_notification(institution, cached_vagas, current_vagas)
                    
                    # Update cache
                    self.cached_data[institution] = current_vagas
            
            self.save_cache(self.cached_data)
            
        except Exception as e:
            print(f"Error occurred: {str(e)}")

def main():
    import sys
    monitor = VagasMonitor()
    
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        print("Sending test notification...")
        monitor.send_notification("test", "test", "test")
        print("Test notification sent!")
    else:
        monitor.check_vagas()

if __name__ == "__main__":
    main()
