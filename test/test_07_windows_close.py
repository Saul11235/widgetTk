from tkinter import Tk, Button
from widgetTk import widget ,window, menuWidget
from tkinter import Tk
from tkinter import Button


if __name__=="__main__":
    from tkinter import Tk
    from tkinter import Button

    v=window()
    v.size(300,100)
    v.resizable(False,False)
    v.header("hola","test.png")


    miMenu=menuWidget(data=[["opcion1",[1,2,3]],"opcion2"])
    ww=widget(data=[["hola"],["como vamos"]])
    ww.config(background="red")
    #ww.pack()
    v.set(varframe=ww,varmenu=miMenu)

    def funEnter():
        print("Enter")

    def funClose():
        print("Closing")
        v.destroy()



    v.event("<Control-p>",funEnter)
    v.eventIfClose(funClose)

    v.mainloop()





