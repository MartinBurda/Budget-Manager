import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from app.backend import cashFlow

def hide_all_widgets():
    for widget in root.winfo_children():
        widget.pack_forget()

def add_income():
    amount = entry_income.get()
    source = entry_income_source.get()
    if amount and source:
        try:
            amount = float(amount)
            cashFlow.addIncome(amount, source)
            label_result.config(text=f"Přidán příjem: {amount} pro {source}")
            entry_income.delete(0, END)
            entry_income_source.delete(0, END)
            show_incomes()
        except ValueError:
            label_result.config(text="Špatná suma. Prosím zadejte správnou sumu!")
    else:
        label_result.config(text="Prosím zadejte obojí sumu a zdroj příjmů pro přidání k příjmu!")
    label_result.pack()

def add_expense():
    amount = entry_expense.get()
    source = entry_expense_source.get()
    if amount and source:
        try:
            amount = float(amount)
            cashFlow.addOutcome(amount, source)
            label_result.config(text=f"Přidaný výdaj: {amount} pro {source}")
            entry_expense.delete(0, END)
            entry_expense_source.delete(0, END)
            show_expenses()
        except ValueError:
            label_result.config(text="Špatná suma. Prosím zadejte správnou sumu!")
    else:
        label_result.config(text="Prosím zadejte obojí sumu a zdroj výdajů pro přidání k výdaji!")
    label_result.pack()

def add_savings():
    amount = entry_savings.get()
    source = entry_savings_source.get()
    if amount and source:
        try:
            amount = float(amount)
            cashFlow.addSavings(amount, source)
            label_result.config(text=f"Přidaný výdaj: {amount} pro {source}")
            entry_savings.delete(0, END)
            entry_savings_source.delete(0, END)
            show_savings()
        except ValueError:
            label_result.config(text="Špatná suma. Prosím zadejte správnou sumu!")
    else:
        label_result.config(text="Prosím zadejte obojí sumu a spoření pro přidání ke spoření!")
    label_result.pack()

def show_incomes():
    hide_all_widgets()
    tree.delete(*tree.get_children())
    incomes = cashFlow.getIncome()
    if incomes:
        for income in incomes:
            tree.insert("", "end", values=(income[0], income[1], income[2]))
    else:
        tree.insert("", "end", values=("Žádné příjmy nenalezeny.", "", ""))
    tree.pack(fill=BOTH, expand=True)
    back_btn.pack()

def show_expenses():
    hide_all_widgets()
    tree.delete(*tree.get_children())
    expenses = cashFlow.getOutcome()
    if expenses:
        for expense in expenses:
            tree.insert("", "end", values=(expense[0], expense[1], expense[2]))
    else:
        tree.insert("", "end", values=("Žádné výdaje nenalezeny.", "", ""))
    tree.pack(fill=BOTH, expand=True)
    back_btn.pack()

def show_savings():
    hide_all_widgets()
    tree.delete(*tree.get_children())
    savings = cashFlow.getSavings()
    if savings:
        for savings in savings:
            tree.insert("", "end", values=(savings[0], savings[1], savings[2]))
    else:
        tree.insert("", "end", values=("Žádné spoření nebylo nenalezeno.", "", ""))
    tree.pack(fill=BOTH, expand=True)
    back_btn.pack()

def show_main_menu():
    hide_all_widgets()
    main_menu.pack()
    label_result.pack()

cashFlow.createDatabase()

root = tk.Tk()
root.geometry('600x600')
root.resizable(True, True)
root.title("Budget Manager Application")
root.iconbitmap("favicon.ico")

main_menu = tk.Frame(root)

def show_income_entry():
    hide_all_widgets()
    label_income.pack()
    entry_income.pack()
    label_income_source.pack()
    entry_income_source.pack()
    add_income_btn.pack()
    back_btn.pack()
    tree.pack(fill=BOTH, expand=True)

def show_expense_entry():
    hide_all_widgets()
    label_expense.pack()
    entry_expense.pack()
    label_expense_source.pack()
    entry_expense_source.pack()
    add_expense_btn.pack()
    back_btn.pack()
    tree.pack(fill=BOTH, expand=True)

def show_savings_entry():
    hide_all_widgets()
    label_savings.pack()
    entry_savings.pack()
    label_savings_source.pack()
    entry_savings_source.pack()
    add_savings_btn.pack()
    back_btn.pack()
    tree.pack(fill=BOTH, expand=True)

show_income_entry_btn = ttk.Button(main_menu, text="Přidat příjem", command=show_income_entry)
show_income_entry_btn.pack()

show_expense_entry_btn = ttk.Button(main_menu, text="Přidat výdaj", command=show_expense_entry)
show_expense_entry_btn.pack()

show_savings_entry_btn = ttk.Button(main_menu, text="Správa spoření", command=show_savings_entry)
show_savings_entry_btn.pack()
main_menu.pack()

tree = ttk.Treeview(root, columns=("ID", "Částka", "Zdroj"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Částka", text="Částka")
tree.heading("Zdroj", text="Zdroj")

label_result = tk.Label(root, text="")

label_income = tk.Label(root, text="Zadejte sumu pro příjem:")
entry_income = ttk.Entry(root)
label_income_source = tk.Label(root, text="Zadejte zdroj příjmů:")
entry_income_source = ttk.Entry(root)
add_income_btn = ttk.Button(root, text="Přidat příjem", command=add_income)

label_expense = tk.Label(root, text="Zadejte sumu pro výdaj:")
entry_expense = ttk.Entry(root)
label_expense_source = tk.Label(root, text="Zadejte zdroj výdajů:")
entry_expense_source = ttk.Entry(root)
add_expense_btn = ttk.Button(root, text="Přidat výdaj", command=add_expense)

label_savings = tk.Label(root, text="Zadejte sumu pro spoření:")
entry_savings = ttk.Entry(root)
label_savings_source = tk.Label(root, text="Zadejte zdroj spoření:")
entry_savings_source = ttk.Entry(root)
add_savings_btn = ttk.Button(root, text="Přidat spoření", command=add_savings)

back_btn = ttk.Button(root, text="Zpět", command=show_main_menu)

root.mainloop()


                    



















