
import tkinter as tk

def create_frame_on_top():
    top_level = tk.Toplevel(root)
    top_level.title("Frame en TopLevel")
    
    frame = tk.Frame(top_level)
    frame.config(background="blue")
    frame.pack(expand=True, fill=tk.BOTH)  # Ajustar al tamaño de la ventana
    
    label = tk.Label(frame, text="Este frame está siempre en la ventana Toplevel")
    label.pack()

root = tk.Tk()
root.title("Ventana Principal")

create_frame_on_top()

root.mainloop()
