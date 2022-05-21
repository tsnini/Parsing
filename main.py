import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('wines.csv', 'w', newline = '\n', encoding='utf-8_sig')
f_obj = csv.writer(file)
f_obj.writerow(['Title', 'Brand', 'Category', 'Year', 'Price'])

page = 1

while page<6:
    url = "https://winegallery.ge/ka/production?ca=115&page="+str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    sub_soup = soup.find('div', class_="col-md-9")
    all_wines = sub_soup.find_all('div', class_="shop-product-item")

    for wine in all_wines:
        title = wine.h4.a.text
        brand = wine.find('p', class_='product-manufacturer-newd').text
        category = wine.find('p', class_='product-category-newd').text.strip()
        year = wine.find('span', class_='product-year-newd').text
        price = wine.find('div', class_='price').text.strip()
        price = price.replace('b', '')
        print(title)
        f_obj.writerow([title, brand, category, year, price])
    page = page+1
    sleep(randint(15, 20))