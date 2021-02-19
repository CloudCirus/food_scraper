import os
import scraper

PROJECT_DIR = os.path.dirname(scraper.__file__)

headers = {
    'authority': 'www.yeezysupply.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
        '/573.31 (KHTML, like Gecko) Chrome/80.0.3547.106 Safari/573.31',
    'sec-fetch-dest': 'document',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

url = 'https://health-diet.ru/table_calorie/'
