import tkinter as tk
from tkinter import ttk, messagebox

ppal = tk.Tk()
ppal.title("Ejercicio integrador - app 1")

inptu_box = tk.Entry(ppal, width=30)
inptu_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

button_box = tk.Button(ppal, text="¡Saludar!")
button_box.grid(row=0, column=1, padx=(0, 50), pady=10, sticky="e")

label_text = tk.Label(ppal)
label_text.grid(row=1, column=0, columnspan=2, padx=10, pady=0, sticky="w")

text_intput_box = tk.Text(ppal, width=30, height=10)
text_intput_box.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


def saludar():
    data = text_intput_box.get("1.0", tk.END)
    length = len(data.strip().split("\n"))
    if length == 5:
        messagebox.showerror("Error", "No se permiten mas de 5 elementos")
    else:
        name = inptu_box.get()
        label_text.config(text=f"¡Hola, {name}!")
        text_intput_box.insert(tk.END, name + "\n")
        inptu_box.delete(0, tk.END)

button_box.config(command=saludar)


ppal.grid_columnconfigure(0, weight=1)

ppal.mainloop()