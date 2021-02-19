import json
import os

from bs4 import BeautifulSoup
from scraper.settings import PROJECT_DIR

# сохраняем категории в json

if not os.path.isdir(PROJECT_DIR + '/tmp'):
    os.mkdir(PROJECT_DIR + '/tmp')
    with open(f'{PROJECT_DIR}/tmp/index.html') as file:
        src = file.read()
else:
    with open(f'{PROJECT_DIR}/tmp/index.html') as file:
        src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_products_href = soup.find_all(class_='mzr-tc-group-item-href')

all_categories_dict = {}
for i in all_products_href:
    text = i.text
    href = 'https://health-diet.ru' + i.get('href')
    all_categories_dict[text] = href

with open(f'{PROJECT_DIR}/tmp/all_categories.json', 'w') as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
