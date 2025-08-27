import requests

API_KEY = 'AIzaSyD6cZy1_J5N-O97bhcX6aqqKbP3_wqfk58'
SEARCH_ENGINE_ID = '30854cad23c464de8'
query = 'Pedido de asilo à Argentina de Milei? A repercussão do indiciamento'.replace(" ", '+')

url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}'

response = requests.get(url)
data = response.json()

for item in data.get('items', []):
    print(item['link'])