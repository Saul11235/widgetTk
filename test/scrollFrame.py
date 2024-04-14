import tkinter as tk
from tkinter import ttk

def on_configure(event):
    # Configurar la región de desplazamiento para que tenga el tamaño del contenido
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Frame con Barras de Desplazamiento")

# Crear un frame que contendrá los widgets
frame = tk.Frame(root)

# Crear una barra de desplazamiento vertical
vsb = ttk.Scrollbar(frame, orient="vertical")
vsb.pack(side="right", fill="y")

# Crear una barra de desplazamiento horizontal
hsb = ttk.Scrollbar(frame, orient="horizontal")
hsb.pack(side="bottom", fill="x")

# Crear un lienzo para el contenido del frame
canvas = tk.Canvas(frame, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
canvas.pack(side="left", fill="both", expand=True)

# Configurar las barras de desplazamiento para controlar el lienzo
vsb.config(command=canvas.yview)
hsb.config(command=canvas.xview)

# Adjuntar el lienzo al frame
canvas.create_window((0, 0), window=frame, anchor="nw")

# Detectar cambios en el tamaño del frame para actualizar la región de desplazamiento
frame.bind("<Configure>", on_configure)

# Añadir contenido al frame
for i in range(50):
    tk.Label(frame, text="Label " + str(i)).pack()

# Ajustar el tamaño de la ventana principal para mostrar el contenido
root.geometry("300x300")

frame.pack()
root.mainloop()
