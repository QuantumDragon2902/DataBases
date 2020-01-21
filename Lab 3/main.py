import sqlite3
import random

connect = sqlite3.connect('database.db')
connect.execute("PRAGMA foreign_keys = 1")
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Clients (
               id INTEGER PRIMARY KEY,
               surname TEXT,
               name TEXT,
               patronymic TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS House (
               client_id INTEGER,
               adress TEXT,
               type TEXT CHECK (type IN
               ("Flat", "House", "Penthouse", "Room")),
               FOREIGN KEY (client_id) REFERENCES clientss(id)
               ON DELETE RESTRICT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Car (
               house_id INTEGER,
               mark TEXT,
               year INTEGER CHECK (year>1899 AND year<2015),
               FOREIGN KEY (house_id) REFERENCES house(id)
               ON DELETE CASCADE)''')

surname = ['Smith', 'Jobs', 'Gates']
name = ['Steve', 'Bill', 'Mark']
patronymic = ['John', 'Leonard', 'Mario']
for id in range(1, 6):
    sql = 'INSERT INTO Clientss VALUES(?,?,?,?)'
    surname = random.choice(surname)
    name = random.choice(name)
    patronymic = random.choice(patronymic)
    cursor.execute(sql, (id, surname, name, patronymic))
    
statuses = ["Flat", "House", "Penthouse", "Room"]
adresses = ["Avenue", "Street", "Shosse", "Bulwaure"]
for i in range(1, 11):
    sql = 'INSERT INTO House VALUES(?,?,?)'
    house_id = random.randint(1, 6)
    adress = random.choice(adresses)
    status = random.choice(statuses)
    cursor.execute(sql, (house_id, adress, status))
    
markes = ['Mersedes', 'BMW', 'Opel', 'Nissan', 'Toyota', 'Audi']
for id in range(1, 11):
    sql = 'INSERT INTO Car VALUES(?,?,?)'
    car_id = random.randint(1, 11)
    mark = random.choice(markes)
    year = random.randint(1900, 2014)
    cursor.execute(sql, (id, car_id, mark, year))



connect.commit()
connect.close()