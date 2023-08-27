import tkinter as tk
from tkinter import ttk

ppal = tk.Tk()
ppal.title("App")
ppal.config(width=800, height=500)
def nuevo():
 print("Nuevo archivo.")
def acerca_de():
 print("Acerca de:")
barra_de_menu = tk.Menu()
menu_archivo = tk.Menu(barra_de_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_ayuda = tk.Menu(barra_de_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)
barra_de_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_de_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
ppal.config(width=300, height=200, menu=barra_de_menu)

entry = tk.Entry()
label = tk.Label(text="texto")
label.place(x=10, y=200)
lista = tk.Listbox()
lista.insert(0, "p", "c", "c++")
lista.insert(tk.END, "last element")
def selection():
    print(lista.get(lista.curselection()))
but2 = tk.Button()
but2.place(x=50, y=250)
but2.config(text="imprimir de lista", command=selection)

lista.place(x=50, y = 300)
def print_text():
    print(entry.get())

entry.place(x=50, y=200)

button = tk.Button(text="Imprimir")
def press():
    print_text()
    entry.delete(0, tk.END)
button.place(x=50, y=50)
button.config(command=press)
entry.insert(0, "hola mundo")

lista_desplegable = ttk.Combobox(
 values=[
 "Visual Basic",
 "Python",
 "C",
 "C++",
 "Java"
 ]
)

lista_desplegable.place(x=10, y=10)
checkbutton = ttk.Checkbutton(text="Opción")
checkbutton.place(x=10, y=10)
checkbutton_estado = tk.BooleanVar()
checkbutton = ttk.Checkbutton(text="Opción", variable=checkbutton_estado)


ppal.mainloop()