import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.getenv('GOOGLE_SEARCH_ENGINE_ID')

if not API_KEY or not SEARCH_ENGINE_ID:
    raise RuntimeError('Configure GOOGLE_API_KEY e GOOGLE_SEARCH_ENGINE_ID para testar a busca.')
query = 'Pedido de asilo à Argentina de Milei? A repercussão do indiciamento'.replace(" ", '+')

url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}'

response = requests.get(url)
data = response.json()

for item in data.get('items', []):
    print(item['link'])
