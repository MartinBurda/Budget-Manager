# Importy modulů a propojení mezi soubory.
import sys
import os
import tkinter as tk
from tkinter import *


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from app.backend import cashFlow

# Metody pro práci s databází.
def add_income():
    """
    Metoda pro přídání příjmu (z tabulky income)
    """
    amount = entry_income.get()
    source = entry_income_source.get()
    if amount and source:
        try:
            amount = float(amount)  
            cashFlow.addIncome(amount, source)
            label_result.config(text=f"Přidán přijem: {amount} pro {source}")
        except ValueError:
            label_result.config(text="Špatná suma. Prosím zadejte spravnou sumu !")
    else:
        label_result.config(text="Prosím zadejte obojí sumu a zdroj příjmů pro přidání k příjmu !")

def add_expense():
    """
    Metoda pro přídání výdajů (z tabulky outcome)
    """
    amount = entry_expense.get()
    source = entry_expense_source.get()
    if amount and source:
        try:
            amount = float(amount)  
            cashFlow.addOutcome(amount, source)
            label_result.config(text=f"Přidaný výdaj: {amount} pro {source}")
        except ValueError:
            label_result.config(text="Špatná suma. Prosím zadejte spravnou sumu !")
    else:
        label_result.config(text="Prosím zadejte obojí sumu a zdroj výdajů pro přidání k výdaji !")
# Utvoření databáze z cashflow takže se utvoří budget_database.sqlite soubor pokud už není...
cashFlow.createDatabase()
# Celé okno budget manageru (s obsahem income a outcome)
root = tk.Tk()
root.geometry('500x400')
root.resizable(True, True)
root.title("Budget Manager Application")


label_income = tk.Label(root, text="Zadejte sumu pro příjem:")
label_income.pack()

entry_income = tk.Entry(root)
entry_income.pack()


label_income_source = tk.Label(root, text="Zadejte zdroj příjmů:")
label_income_source.pack()

entry_income_source = tk.Entry(root)
entry_income_source.pack()


add_income_btn = Button(root, text="Přidat příjem", command=add_income)
add_income_btn.pack()


label_expense = tk.Label(root, text="Zadejte sumu pro výdaj:")
label_expense.pack()

entry_expense = tk.Entry(root)
entry_expense.pack()


label_expense_source = tk.Label(root, text="Zadejte zdroj výdajů:")
label_expense_source.pack()

entry_expense_source = tk.Entry(root)
entry_expense_source.pack()


add_expense_btn = Button(root, text="Přidat výdaj", command=add_expense)
add_expense_btn.pack()


label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()





