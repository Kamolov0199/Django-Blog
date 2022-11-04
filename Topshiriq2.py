import sqlite3 as sql

boglanish = sql.connect("MobilePhone.db")

Telefonlar = boglanish.cursor()

Telefonlar.execute("""
CREATE TABLE IF NOT EXISTS Iphone(
    nomi TEXT,
    rangi TEXT,
    Davlati INTEGER
)                                          
""")

Telefonlar.execute("""
CREATE TABLE IF NOT EXISTS Samsung(
    turi TEXT,
    nomi TEXT,
    Davlati INTEGER
)                                          
""")
