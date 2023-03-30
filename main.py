import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict

# Отправляем GET-запрос на страницу с лучшими фильмами imdb.com
def parse():
    k = 1
    d = dict()
    while k <= 5:
        if k == 1:
            url = "https://www.chitai-gorod.ru/search?phrase=python"
        else:
            url = 'https://www.chitai-gorod.ru/search?phrase=python&page=' + str(k)

        page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную

        # Создаем объект BeautifulSoup для парсинга HTML-страницы
        soup = BeautifulSoup(page.text, 'html.parser') # передаем страницу в bs4
        book = soup.findAll(class_='product-title__head')
        author = soup.findAll(class_='product-title__author')
        price = soup.findAll(class_='product-price__value')
        for el in range(len(book)):
            temp = price_temp[el].find(class_='product-price__value').text if price_temp[el].find(class_='product-price__value') != None else " "
            d['Name'] = d.get('Name', []) + [book[el].text]
            d['Author'] = d.get('Author', []) + [author[el].text]
            d['Price'] = d.get('Price', []) + [temp.replace('\xa0', ' ')]

        k += 1
    df = pd.DataFrame(d)
    df.to_excel('./teams.xlsx')
