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

cur.execute('SELECT COUNT(*) FROM Sales')
print("The number of strings in the table =", cur.fetchall()[0][0])

for country in Countries:
    cur.execute('SELECT COUNT(shop) FROM Sales WHERE country= ?', (country,))
    print("There are", country, cur.fetchall()[0][0], "shops in country")

for shop in Shops:
    cur.execute("SELECT sum(Summ) FROM Sales WHERE shop = ?", (shop,))
    print("Shop", shop, "has got profit in:", cur.fetchall()[0][0], "rubles")

country = input("Input country: ")
for shop in Shops:
    cur.execute('SELECT sum(Summ) FROM Sales '
              'WHERE shop = ? and country = ? and '
              'date BETWEEN "2019-06-%%" AND "2019-08-%%"',(shop, country))
    print("Shops", shop, "in country", country, "has benefit during the summer in:", 
        cur.fetchall()[0][0], "rubles")

conn.commit()
conn.close()