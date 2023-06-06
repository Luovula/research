import os
import sqlite3
import timeit
import random
import string


# os.remove("elokuvat.db")
kirjaimet = string.ascii_letters

db = sqlite3.connect("elokuvat.db")
db.isolation_level = None


start = timeit.default_timer()

db.execute("BEGIN;")
db.execute("CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")
for i in range(999999):
    random_name = ''.join(random.choice(kirjaimet) for _ in range(8))
    random_year = random.randint(1900,2000)
    db.execute("INSERT INTO Elokuvat(nimi, vuosi) VALUES (?,?)",[random_name,random_year])
db.execute("COMMIT;")

stop = timeit.default_timer()

print('Aikaa kului: ', stop-start)

start = timeit.default_timer()
db.execute("BEGIN;")
for i in range(999):
    chosen_year = random.randint(1900,2000)
    db.execute("SELECT COUNT(E.id) FROM Elokuvat E WHERE E.vuosi = ?", [chosen_year])
db.execute("COMMIT;")

stop = timeit.default_timer()

print('Aikaa kului: ', stop-start)
print(os.path.getsize("elokuvat.db"))