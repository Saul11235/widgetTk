
import tkinter as tk
from tkinter import ttk

class LeftTabNotebook(ttk.Notebook):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tab_position("w")  # Establecer la posición de las pestañas a la izquierda


def main():
    root = tk.Tk()
    root.title("Notebook con Pestañas a la Izquierda")

    notebook = LeftTabNotebook(root)

    # Crear pestañas
    tab1 = tk.Frame(notebook, bg="white", width=400, height=200)
    tab2 = tk.Frame(notebook, bg="white", width=400, height=200)
    tab3 = tk.Frame(notebook, bg="white", width=400, height=200)

    notebook.add(tab1, text="Pestaña 1")
    notebook.add(tab2, text="Pestaña 2")
    notebook.add(tab3, text="Pestaña 3")

    notebook.pack(expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()
