# Importy modulů:
import sqlite3
import os.path

# Proměnné, které tvoří a editují databázi:
createIncome = "CREATE TABLE IF NOT EXISTS income (id INTEGER PRIMARY KEY, amount INTEGER, source VARCHAR, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
createOutcome = "CREATE TABLE IF NOT EXISTS outcome (id INTEGER PRIMARY KEY, amount INTEGER, source VARCHAR, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
insertIncome = "INSERT INTO income (amount, source) VALUES (?, ?);"
insertOutcome = "INSERT INTO outcome (amount, source) VALUES (?, ?);"
selectIncome = "SELECT * FROM income"
selectOutcome = "SELECT * FROM outcome"

# Metody pro práci s databází s výpisy:
def createDatabase():
    """
    pokud databáze neexistuje, vytvoří ji a přidá tabulky přijmů a výdajů
    """
    if not os.path.exists("budget_database.sqlite"):
        with sqlite3.connect("budget_database.sqlite") as db:
            db.execute(createIncome)
            db.execute(createOutcome)

def addIncome(amount, source):
    """
    přidání přjmu
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        db.execute(insertIncome, (amount, source))

def addOutcome(amount, source):
    """
    přidání výdaje
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        db.execute(insertOutcome, (amount, source))

# Výpisy z databáze:
def getIncome():
    """
    výpis příjmů
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        cursor = db.execute(selectIncome)
        income = cursor.fetchall() 
        return income

def getOutcome():
    """
    výpis výdajů
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        cursor = db.execute(selectOutcome)
        outcome = cursor.fetchall()  
        return outcome



