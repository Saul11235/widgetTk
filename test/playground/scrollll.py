
import tkinter as tk
from tkinter import ttk

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

root = tk.Tk()
root.title("Frame con Barras de Desplazamiento")

# Crear un frame que contendrá los widgets
frame = ttk.Frame(root)

# Crear una barra de desplazamiento vertical
vsb = ttk.Scrollbar(frame, orient="vertical")
vsb.pack(side="right", fill="y")

# Crear un lienzo para el contenido del frame
canvas = tk.Canvas(frame, yscrollcommand=vsb.set)
canvas.pack(side="left", fill="both", expand=True)

# Configurar las barras de desplazamiento para controlar el lienzo
vsb.config(command=canvas.yview)

# Adjuntar el lienzo al frame
canvas.create_window((0, 0), window=frame, anchor="nw")

# Permitir desplazamiento con la rueda del mouse
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Añadir contenido al frame
for i in range(50):
    tk.Label(frame, text="Label " + str(i)).pack()

# Ajustar el tamaño de la ventana principal para mostrar el contenido
root.geometry("300x300")

root.mainloop()
