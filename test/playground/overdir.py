import tkinter as tk

root = tk.Tk()
root.title("Ventana sin maximizar, minimizar ni restaurar")

# Desactivar la capacidad de redimensionar la ventana
root.resizable(width=False, height=False)

# Evitar que la ventana tenga botones de maximizar, minimizar y restaurar
root.overrideredirect(True)

root.mainloop()
