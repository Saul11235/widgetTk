from tkinter import Tk, Button
from widgetTk import widget ,window, menuWidget
from tkinter import Tk
from tkinter import Button

def funcionP():
    print("has presionado ctrl+p")

def funcionA():
    print("has presionado ctrl+A")

if __name__=="__main__":

    v=window()
    v.header("hola","test.png")
    v.event("<Control-p>",funcionP)
    v.event("<a>",funcionA)
    miMenu=menuWidget(data=["opcion1","opcion2"])
    ww=widget(data=[["hola"],["como vamos"],(("hola",funcionA),),((("lolo",funcionP),))])
    ww.config(background="red")
    v.set(varframe=ww,varmenu=miMenu)
    v.minsize(700,400)

    v.mainloop()






