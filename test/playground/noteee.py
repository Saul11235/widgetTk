
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Configurar el estilo para el Notebook
style = ttk.Style(root)
style.layout('Vertical.TNotebook.Tab', [('Notebook.tab', {'sticky': 'nswe', 'children': [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children': [('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children': [('Notebook.label', {'side': 'top', 'sticky': ''})]})]})]})])

# Configurar el Notebook con el estilo personalizado
notebook = ttk.Notebook(root, style='Vertical.TNotebook')

f1 = tk.Frame(notebook, bg='red', width=200, height=200)
f2 = tk.Frame(notebook, bg='blue', width=200, height=200)

notebook.add(f1, text='Frame 1')
notebook.add(f2, text='Frame 2')

notebook.pack()

root.mainloop()
