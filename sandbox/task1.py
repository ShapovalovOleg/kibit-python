"""
Завдання 1:
«Смаки кави» — PostgreSQL + pandas

Підготовка середовища
1. Завантажте й запустіть Docker-контейнер з PostgreSQL.

docker run --name cafe_pg -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass -p 5433:5432 -d postgres

2. Встановіть psycopg2-binary та sqlalchemy (якщо ще не встановлено).
3. Створіть engine і підключіться до бази даних що створили в попередньому пункті.
4. Використовуючи pandas, завантажте csv-файл coffe_ratings.csv з смаками кави (використовуючи функцію read_csv) у DataFrame.
5. Отриманий DataFrame збережіть у базу даних (таблицю назвіть 'coffee_flavors').
6. За допомогою pd.read_sql_query виведіть середні значення деяких колонок (наприклад, AVG(total_cup_points)).
7. Відсортуйте таблицю за grading date та виведіть перші 10 записів.

pd.read_csv()

'postgresql://user:pass@localhost:5433/postgres'
df.to_sql(назва таблиці, енжин)
pd.read_sql_query(sql запит, engine)

SELECT * FROM coffe_ratings ORDER BY grading_date LI
harvest_year
SELECT AVG(total_cup_points) FROM coffee_flavors
"""

import pandas as pd
from numpy.distutils.misc_util import green_text
from sqlalchemy import create_engine
coffe = pd.read_csv('coffe_ratings.csv')
print(coffe.head())

ce = create_engine("postgresql://user:pass@localhost:5433/postgres")

gradingDate = pd.read_sql_query("SELECT AVG(total_cup_points) FROM coffe_ratings", ce)
print(gradingDate)

