# Name LastName

from tkinter import Tk, Button
from widgetTk import widget,menuWidget

def f1(): print(1)
def f2(): print(2)
def f3(): print(3)
L=[
            ["ljlj",
              ("Funcion desactivada",f1,False),
              ("Funcion activada",f2,True),
             "",
             ("activado",True),
             ("desactivado",False),
            ],
           [1,
             [
                 12,
                 12,
                 [1,2],
                 234
                 ]
            ],
           ["lol"],
           ["sub",
            [
                "subbb",
                [1,(2),3,4]],"sss"],"fun2","nadie es el dueño ","lolo"]
t=Tk()
m=menuWidget(t,data=L)

def accion():
    L.append("texto")
    m.set(["jkjkj"])

b=Button(t,text="accion boto",command=accion)
b.pack()
t.config(menu=m)
t.mainloop()



