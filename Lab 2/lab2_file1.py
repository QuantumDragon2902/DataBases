import sqlite3
import datetime
import random

DataBase = sqlite3.connect('Sales.db')
cur = DataBase.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS Sales (
    Identifier INTEGER PRIMARY KEY,
    Country TEXT,
    City TEXT,
    Shop TEXT,
    Date DATETIME,
    Summ INTEGER
);''')

Countries = ['Russia', 'Japan', 'German', 'USA', 'England']
Cities = {'Russia': ['Surgut', 'Kazan', 'Moscow'],
          'Japan': ['Tokio', 'Kioto', 'Kie'],
          'German': ['Berlin', 'Munchern', 'Hamburg'],
          'USA': ['New-York', 'Los-Angelas', 'Washington'],
          'England': ['London', 'Cambridge', 'Manchester']}
Shop = ['Channel', 'Dolce&Gabanna', 'Gucci', 'Zara']

i = 0
for i in range(1000000):
    country_ = random.choice(Countries)
    city_ = random.choice(City[country_])
    shop_ = random.choice(Shop)
    month = random.randint(1, 12)
    date_ = datetime.date(2019, month_, random.randint(1, 28))
    summ_ = random.randint(10000, 1000000)
    a.execute("INSERT INTO Sales VALUES (?,?,?,?,?,?);", (i, country_, city_, shop_, date_, summ_))

cur.execute(''' CREATE TABLE IF NOT EXISTS Shop (
    Shop_id INTEGER PRIMARY KEY,
    City TEXT,
    Country TEXT
);''')

Base.commit()
Base.close()