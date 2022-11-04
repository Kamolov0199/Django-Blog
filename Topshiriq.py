import sqlite3 as sql

boglanish = sql.connect("Stepler.db")

Stepler = boglanish.cursor()

Stepler.execute("""
CREATE TABLE IF NOT EXISTS SteplerPro(
    nomi TEXT,
    rangi TEXT,
    amal qilish muddati INTEGER
)                                          
""")

Stepler.execute("""
CREATE TABLE IF NOT EXISTS Steplereasy(
    turi TEXT,
    nomi TEXT,
    Nechta stepleri bor INTEGER
)                                          
""")