
import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.title("Label con subrayado")

# Creamos una fuente con subrayado
font_with_underline = tkFont.Font(root, underline=True)

# Creamos un Label con la fuente subrayada
label = tk.Label(root, text="Subrayado", font=font_with_underline)
label.pack()

root.mainloop()
