
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Función para graficar
def graficar():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Gráfico de Seno')

    # Crear el lienzo de Matplotlib en el frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Gráfico con Matplotlib en Tkinter")

# Crear un frame dentro de la ventana principal
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Botón para graficar
boton_graficar = ttk.Button(frame, text="Graficar", command=graficar)
boton_graficar.pack()

# Ejecutar la aplicación
root.mainloop()
