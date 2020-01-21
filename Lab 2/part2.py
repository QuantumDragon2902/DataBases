import sqlite3
import random 
import datetime

Countries = ['Russia', 'Japan', 'German', 'USA', 'England']
Cities = {'Russia': ['Surgut', 'Kazan', 'Moscow'],
          'Japan': ['Tokio', 'Kioto', 'Kie'],
          'German': ['Berlin', 'Munchern', 'Hamburg'],
          'USA': ['New-York', 'Los-Angelas', 'Washington'],
          'England': ['London', 'Cambridge', 'Manchester']}
Shop = ['Channel', 'Dolce&Gabanna', 'Gucci', 'Zara']

conn = sqlite3.connect('Sales.db')
cur = conn.cursor()

cur.execute('INSERT INTO Shops SELECT DISTINCT Identifier, City, Country FROM Sales group by City')

country = input("Input the country: ")
for shop in Shops:
    cur.execute('SELECT SUM(Summ) FROM Sales '
              'INNER JOIN Shops ON Sales.Identifier=Shops.Shop_id '
              'WHERE Shops.Country = ? AND Sales.Shop = ? AND '
              'Sales.Date BETWEEN "2019-06-%%" AND "2019-08-%%" ', 
              (country, shop,))
    print("Shops", shop, "in country", country, "has benefit during the summer:", 
        cur.fetchall()[0][0], "rubles")

for country in Countries:
    for city in Cities.get(country):
        cur.execute("SELECT SUM(Summ) FROM Sales"
                  " INNER JOIN Shops ON "
                  "Sales.Identifier=Shops.Shop_id WHERE Shops.City = ? ",
                  (city,))
        print("Summ of sale", city, ":", cur.fetchall()[0][0], "rubles")

print("А")
for shop in Shops:
        cur.execute("SELECT AVG(Summ) FROM Sales "
                  "INNER JOIN Shops ON "
                  "Sales.Identifier=Shops.Shop_id WHERE Sales.Shop = ? ",
                  (shop,))
        print("Average sum ", shop, ":",
              int(cur.fetchall()[0][0]), "rubles")

print("Б")
for country in Countries:
    for city in Cities.get(country):
        cur.execute("SELECT AVG(Summ) FROM Sales "
                  "INNER JOIN Shops ON "
                  "Sales.Identifier=Shops.Shop_id WHERE Shops.City = ? ",
                  (city,))
        print("Average summ ", city, ":",
              int(cur.fetchall()[0][0]), "rubles")

print("В")
for country in Countries:
        cur.execute("SELECT AVG(Summ) FROM Sales "
                  "INNER JOIN Shops ON "
                  "Sales.Identifier=Shops.Shop_id WHERE Shops.Country = ? ",
                  (country,))
        print("Average summ ", country, ":",
              int(cur.fetchall()[0][0]), "rubles")

conn.commit()
conn.close()