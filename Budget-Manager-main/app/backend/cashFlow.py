# Importy modulů:
import sqlite3
import os.path

# Proměnné, které tvoří a editují databázi:
createIncome = "CREATE TABLE IF NOT EXISTS income (id INTEGER PRIMARY KEY, amount INTEGER, source VARCHAR, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
createOutcome = "CREATE TABLE IF NOT EXISTS outcome (id INTEGER PRIMARY KEY, amount INTEGER, source VARCHAR, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
createSavings = "CREATE TABLE IF NOT EXISTS savings (id INTEGER PRIMARY KEY, amount INTEGER, target VARCHAR, needed_amount INTEGER, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
insertIncome = "INSERT INTO income (amount, source) VALUES (?, ?);"
insertOutcome = "INSERT INTO outcome (amount, source) VALUES (?, ?);"
insertSavings = "INSERT INTO savings (amount, target, needed_amount) VALUES (?, ?, ?);"
selectIncome = "SELECT * FROM income"
selectOutcome = "SELECT * FROM outcome"
selectSavings = "SELECT target, SUM(amount) as saved, needed_amount FROM savings GROUP BY target"
sumIncome = "SELECT SUM(amount) FROM income"
sumOutcome = "SELECT SUM(amount) FROM outcome"
sumSavings = "SELECT SUM(amount) FROM savings"

# Metody pro práci s databází s výpisy:
def createDatabase():
    """
    pokud databáze neexistuje, vytvoří ji a přidá tabulky přijmů, výdajů a spoření
    """
    if not os.path.exists("budget_database.sqlite"):
        with sqlite3.connect("budget_database.sqlite") as db:
            db.execute(createIncome)
            db.execute(createOutcome)
            db.execute(createSavings)

def addIncome(amount, source):
    """
    přidání přijmu
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        db.execute(insertIncome, (amount, source))

def addOutcome(amount, source):
    """
    přidání výdaje
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        db.execute(insertOutcome, (-amount, source))

def addSaving(amount, target, needed_amount):
    """
    přidání spoření a současně přidání výdaje
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        db.execute(insertSavings, (amount, target, needed_amount))
        db.execute(insertOutcome, (-amount, f"Savings for {target}"))

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

def getSavings():
    """
    výpis spoření
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        cursor = db.execute(selectSavings)
        savings = cursor.fetchall()
        return savings

# Funkce pro výpočet celkových částek
def getTotalIncome():
    """
    výpočet celkových příjmů
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        cursor = db.execute(sumIncome)
        total_income = cursor.fetchone()[0]
        return total_income if total_income is not None else 0

def getTotalOutcome():
    """
    výpočet celkových výdajů
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        cursor = db.execute(sumOutcome)
        total_outcome = cursor.fetchone()[0]
        return total_outcome if total_outcome is not None else 0

def getTotalSavings():
    """
    výpočet celkového spoření
    """
    with sqlite3.connect("budget_database.sqlite") as db:
        cursor = db.execute(sumSavings)
        total_savings = cursor.fetchone()[0]
        return total_savings if total_savings is not None else 0

def getCurrentState():
    """
    výpočet aktuálního stavu (příjmy - výdaje)
    """
    total_income = getTotalIncome()
    total_outcome = getTotalOutcome()
    current_state = total_income + total_outcome  # total_outcome je záporné číslo
    return current_state

