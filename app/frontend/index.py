from app.backend import cashFlow
from tkinter import *
import tkinter as tk


def robrazeni():
    puvodni_text = vloste_castku.get()
    pridani_castky = sifra(pridani_castky, "castka")
    label_result.config(text="Pridana castka: " + pridani_castky)
    
def desifrovat_text():
    sifrovani_text = vloste_vydaje.get()
    pridani_vydaju = sifra(pridani_vydaju, "vydaje")
    label_result.config(text="Pridane vydaje: " + pridani_vydaju)


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


label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
