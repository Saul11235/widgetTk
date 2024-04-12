# Name LastName

from tkinter import Tk, Button
from widgetTk import widget

window=Tk()

def action():
    data=widget1.get()
    print(data)
    widget2.set(data=["hello "+str(data[0][1])+" "+str(data[1][1])])

table=[["Your name"    ,"__Entry__"],
       ["Your lastname","__Entry__"]]

widget1=widget(window,data=table)
widget2=widget(window)
button=Button(window,text="action",command=action)

widget1.pack()
button.pack()
widget2.pack()

window.mainloop()
