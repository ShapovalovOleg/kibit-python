"""
Завдання 2. «Котячий паспорт» — MongoDB + pandas
Мета: попрактикувати конвертацію DataFrame → JSON і зворотно при роботі з MongoDB.


1. Запуск MongoDB
docker run --name cats_mongo -p 27017:27017 -d mongo

2. Встановіть pymongo та pandas (якщо ще не встановлено).
3. Підключіться через MongoClient('localhost', 27017); створіть БД "cafe", колекцію coffe_ratings.
4. Аналогічно завданню 1, завантажте csv-файл coffe_ratings.csv з смаками котів (використовуючи функцію read_csv) у DataFrame.
5. Отриманий DataFrame збережіть у колекцію MongoDB (використовуючи метод insert_many).
6. Отримайте всі записи з значенням total_cup_points більше 89 і виведіть в консоль. Використовуйте collection.find({'total_cup_points': {'$gt': 89}}

"""

import pandas as pd
from pymongo import MongoClient

