import os
import requests

from scraper.settings import PROJECT_DIR, headers, url

# сохраняем index.html

url = url
headers = headers
req = requests.get(url, headers)
src = req.text


def get_index():
    if not os.path.isdir(PROJECT_DIR + '/tmp'):
        os.mkdir(PROJECT_DIR + '/tmp')
        with open(f'{PROJECT_DIR}/tmp/index.html', 'w') as file:
            file.write(src)
    else:
        with open(f'{PROJECT_DIR}/tmp/index.html', 'w') as file:
            file.write(src)
