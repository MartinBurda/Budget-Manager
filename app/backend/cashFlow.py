import sqlite3
import os.path


createIncome = "CREATE TABLE income (id INTEGER PRIMARY KEY, amount INTEGER, source VARCHAR, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
createOutcome = "CREATE TABLE outcome (id INTEGER PRIMARY KEY, amount INTEGER, source VARCHAR), date TIMESTAMP DEFAULT CURRENT_TIMESTAMP;"
insertIncome = "INSERT INTO income (amount, source) VALUES (?, ?);"
insertOutcome = "INSERT INTO outcome (amount, source) VALUES (?, ?);"

def createDatabase():
    """
    pokud databáze neexistuje, vytvoří ji a přidá tabulky přijmů a výdajů
    """
    if not os.path.exists("budget_database.sqlite"):
        with sqlite3.connect("budget_database.sqlite") as db:
            db.execute(createIncome)
            db.execute(createOutcome)

def addIncome():
    """
    přidání přjmu
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        db.execute(insertIncome)

def addOutcome():
    """
    přidání výdaje
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        db.execute(insertIncome)
    