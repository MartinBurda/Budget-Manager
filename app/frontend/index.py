from app.backend import cashFlow
from tkinter import *
import tkinter as tk




root = tk.Tk()


root.geometry('500x500')
root.resizable(True, True)
root.title("Budge")


label = tk.Label(root, text="Vlozte castku:", command=cashFlow.addIncome)
label.pack(side=LEFT)

vloste_castku = tk.Entry(root)
vloste_castku.pack(side = RIGHT)


label = tk.Label(root, text="Vlozte výdaje:", command=cashFlow.addOutcome)
label.pack(side=LEFT)

vloste_castku = tk.Entry(root)
vloste_castku.pack(side = RIGHT)


encrypt_btn = Button(root, text="sifrovat", command=pridani_castky)
encrypt_btn.pack(side='left', padx=5)

decrypt_btn = Button(root, text="desifrovat", command=pridani_vydaju)
decrypt_btn.pack(side='right', padx=5)


root.mainloop()
