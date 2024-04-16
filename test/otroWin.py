
import tkinter as tk

def abrir_ventana_activa():
    ventana_activa = tk.Toplevel(root)
    ventana_activa.title("Ventana Activa")
    
    # Hacer que la ventana activa sea modal
    ventana_activa.grab_set()

    def cerrar_ventana_activa():
        ventana_activa.destroy()
        # Liberar el control después de cerrar la ventana activa
        root.grab_release()

    boton_cerrar = tk.Button(ventana_activa, text="Cerrar Ventana Activa", command=cerrar_ventana_activa)
    boton_cerrar.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Principal")

boton_abrir = tk.Button(root, text="Abrir Ventana Activa", command=abrir_ventana_activa)
boton_abrir.pack()

root.mainloop()
