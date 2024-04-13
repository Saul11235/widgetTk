from tkinter import Tk, Button
from widgetTk import widget


if __name__=="__main__":
    from tkinter import Tk
    from tkinter import Button

    window=Tk()

    def action():
        data=widget1.get()
        widget2.set(data=["hello "+str(data[0][1])+" "+str(data[1][1])])
        print("hola")

    def accionCombo(entry):
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

    widget1=widget(window,data=table)#,static=True)
    widget2=widget(window)
    button=Button(window,text="action",command=action)

    widget1.pack()
    button.pack()
    widget2.pack()

    window.mainloop()





