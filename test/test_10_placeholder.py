from tkinter import Tk, Button, Label
from widgetTk import widget ,window, menuWidget, windowTop, placeholder
from tkinter import Tk
from tkinter import Button

if __name__=="__main__":


    v=window()

    pl=placeholder(v,"lolo"*100,100)
    v.set(varframe=pl)

    v.header("ejemplo placeholder")
    v.size(500,300)
    v.mainloop()


