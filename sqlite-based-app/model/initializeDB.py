import os
import sqlite3

os.system('clear')

conn = sqlite3.connect('AnimalList.db')

cursor = conn.cursor()
'''
cursor.execute("""CREATE TABLE Amphibian (
    Amph_Name text,
    Amph_Entry_Date text
    )""")

cursor.execute("""CREATE TABLE Bird (
    Bird_Name text,
    Bird_Entry_Date text
    )""")

cursor.execute("""CREATE TABLE Fish (
    Fish_Name text,
    Fish_Entry_Date text
    )""")

cursor.execute("""CREATE TABLE Mammal (
    Mammal_Name text,
    Mammal_Entry_Date text
    )""")

cursor.execute("""CREATE TABLE Reptile (
    Reptile_Name text,
    Reptile_Entry_Date text
    )""")

cursor.execute("INSERT INTO Amphibian VALUES('Frog','2023-09-13')")
cursor.execute("INSERT INTO Amphibian VALUES('Axolotl','2023-09-13')")
cursor.execute("INSERT INTO Amphibian VALUES('Newt','2023-09-13')")
cursor.execute("INSERT INTO Amphibian VALUES('Olm','2023-09-13')")
cursor.execute("INSERT INTO Amphibian VALUES('Salamander','2023-09-13')")
cursor.execute("INSERT INTO Amphibian VALUES('Toad','2023-09-13')")

cursor.execute("INSERT INTO Bird VALUES('Bald Eagle','2023-09-13')")
cursor.execute("INSERT INTO Bird VALUES('HummingBird','2023-09-13')")
cursor.execute("INSERT INTO Bird VALUES('Penguin','2023-09-13')")
cursor.execute("INSERT INTO Bird VALUES('Falcon','2023-09-13')")
cursor.execute("INSERT INTO Bird VALUES('Barn Swallow','2023-09-13')")
cursor.execute("INSERT INTO Bird VALUES('Heron','2023-09-13')")

cursor.execute("INSERT INTO Fish VALUES('Archer Fish','2023-09-13')")
cursor.execute("INSERT INTO Fish VALUES('CatFish','2023-09-13')")
cursor.execute("INSERT INTO Fish VALUES('Shark','2023-09-13')")
cursor.execute("INSERT INTO Fish VALUES('Gar','2023-09-13')")
cursor.execute("INSERT INTO Fish VALUES('Boxfish','2023-09-13')")
cursor.execute("INSERT INTO Fish VALUES('Marlin','2023-09-13')")

cursor.execute("INSERT INTO Mammal VALUES('cat','2023-09-13')")
cursor.execute("INSERT INTO Mammal VALUES('dog','2023-09-13')")
cursor.execute("INSERT INTO Mammal VALUES('bat','2023-09-13')")
cursor.execute("INSERT INTO Mammal VALUES('horse','2023-09-13')")
cursor.execute("INSERT INTO Mammal VALUES('wolf','2023-09-13')")
cursor.execute("INSERT INTO Mammal VALUES('Binturong','2023-09-13')")

cursor.execute("INSERT INTO Reptile VALUES('snake','2023-09-13')")
cursor.execute("INSERT INTO Reptile VALUES('lizard','2023-09-13')")
cursor.execute("INSERT INTO Reptile VALUES('Crocodile','2023-09-13')")
cursor.execute("INSERT INTO Reptile VALUES('Allosaurus','2023-09-13')")
cursor.execute("INSERT INTO Reptile VALUES('Frilled-lizard','2023-09-13')")
cursor.execute("INSERT INTO Reptile VALUES('turtle','2023-09-13')")
'''
cursor.execute("SELECT * FROM Amphibian")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Bird")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Fish")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Mammal")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Reptile")
print(cursor.fetchall())

conn.commit()

conn.close()
