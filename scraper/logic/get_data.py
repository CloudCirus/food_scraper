import random
import requests
import os
import json
from time import sleep
from scraper.settings import PROJECT_DIR, headers
from bs4 import BeautifulSoup


def get_data():
    # забираем JSON с категориями
    with open(f'{PROJECT_DIR}/tmp/all_categories.json') as file:
        all_categories = json.load(file)
    # проверяем наличие директории /data/ или создаем ее
    if os.path.isdir(f'{PROJECT_DIR}/data'):
        pass
    else:
        os.mkdir(f'{PROJECT_DIR}/data')
    # счетчик для вывода в консоль итераций парсинга
    iteration_count = int(len(all_categories)) - 1
    print(f'Всего итераций: {iteration_count}')
    count = 0
    # главный цикл, для сохранения каждой категории в /data/
    for name, href in all_categories.items():
        # убираем левые символы из названий файлов
        rep = [",", " ", "-", "'"]
        rep1 = ["(", ")"]
        for i in rep:
            if i in name:
                name = name.replace(i, '_')
                for j in rep1:
                    if j in name:
                        name = name.replace(j, '')
        #  делаем запрос
        req = requests.get(url=href, headers=headers)
        src = req.text
        #  сохраняем страницу в свой HTML файл
        with open(f'{PROJECT_DIR}/data/{name}.html', 'w') as file:
            file.write(src)
        #  открываем
        with open(f'{PROJECT_DIR}/data/{name}.html') as file:
            src = file.read()
        #  отбъект супа
        soup = BeautifulSoup(src, 'lxml')
        # профевка на наличие данных
        alert_block = soup.find(class_='uk-alert-danger')
        if alert_block is not None:
            continue
        #  разбираем дом тегов
        products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
        products_list_for_json = []
        for i in products_data:
            product_tds = i.find_all('td')

            title = product_tds[0].find('a').text
            calories = product_tds[1].text
            proteins = product_tds[2].text
            fats = product_tds[3].text
            carbohydrates = product_tds[4].text

            products_list_for_json.append(
                {
                    'title': title,
                    'calories': calories,
                    'proteins': proteins,
                    'fats': fats,
                    'carbohydrates': carbohydrates,
                }
            )
        #  сохраняем JSON с нужными данными
        with open(f'{PROJECT_DIR}/data/{name}.json', 'a', encoding="utf-8") as file:
            json.dump(products_list_for_json, file, indent=4, ensure_ascii=False)
        #  подпинываем счетчик
        count += 1
        #  итерации парсинга
        print(f'{count} итерация, файл {name} записан...')
        iteration_count -= 1
        if iteration_count == 0:
            print('Сбор данных закончен!')
            break
        print(f'Осталось итераций: {iteration_count}')
        #  тормозим запросы
        sleep(random.randrange(1, 2))
