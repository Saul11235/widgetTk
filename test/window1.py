from widgetTk import widget
import tkinter as tk

def resize(event):
    # Redimensionar el frame para que coincida con el tamaño de la ventana
    canvas.itemconfig(frame_id, width=event.width, height=event.height)

if True:
    def action():
        mydata=frame.get()
        mydata.append(["hola"])

        
        frame.set(data=mydata)
        print("hola")

    def accionCombo():
        print("accion combo")
        print("------------------")


diccionarioLabel={
        "type": "Label",
        "text": "Etiqueta 1",
        "font": ("Helvetica", 12),
        "bg": "lightblue",
        "fg": "black",
    },
bb=(("hola",),)
table=[[("Your name",)    ,"Texto"],
       [("Your lastname",),None,""],
           [([1,2,3],)],
           [([1,2,3],"2")],
           [([1,2,3],"Activo",True)],
           [([1,2,3],"Desactivo",False) ],
           [([1,2,3],"COMANDO",True,accionCombo) ],
           [diccionarioLabel,bb],
           [tuple(tuple())],
           [ (("Mi boton",),)      ],
           [ (("Mi boton2",action),)      ],
           [ (("Mi boton2 Activo",action,True),)      ],
           [ (("Mi boton2 Inactivo",action,False),)      ],
           ]







# Crear la ventana principal
root = tk.Tk()
root.title("Ventana con Frame Ajustado")

# Crear un canvas que ocupará toda la ventana
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Crear el frame dentro del canvas
#frame = tk.Frame(canvas, background="red")

frame =widget(data=table)
frame.config(background="red")

frame_id = canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Configurar el canvas para que se expanda con la ventana
canvas.bind("<Configure>", resize)

# Añadir contenido al frame
#label = tk.Label(frame, text="Contenido del Frame")
#label.pack(padx=20, pady=20)

# Iniciar el bucle principal de la ventana
root.mainloop()
