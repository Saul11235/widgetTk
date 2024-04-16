from tkinter import Tk, Button
from widgetTk import widget ,window, menuWidget
from tkinter import Tk
from tkinter import Button

if __name__=="__main__":
    from tkinter import Tk
    from tkinter import Button

    def funEnter():
        print("Enter o ctrl + p")

    def funClose():
        print("Closing")
        v.destroy()


    v=window()
    v.header("principal")
    miMenu=menuWidget(data=[["opcion1",[("fullscreen",v.fullScreenSwitch,),("minimizar",v.minimize),("restaurar",v.restore),("maximizar",v.maximize)]],"opcion2"])
    ww=widget(data=[["hola"],["como vamos"],[(("boton Accion",funEnter),),(("Funcion cerrar",funClose),)]])
    ww.config(background="red")
    v.set(varframe=ww,varmenu=miMenu)
    v.event("<Control-p>",funEnter)
    v.eventIfClose(funClose)
    v.fullScreenSwitch()


#    vv=windowTop(master=v)
#    vv.title("secundario")
#    miOtroMenu=menuWidget(data=["opcion","otra opcion"])
#    www=widget(data=[("Hola soy una ventana secundaria")])
#    www.config(background="blue")
#    vv.set(varframe=www,varmenu=miOtroMenu)
#    vv.set(varmenu=miOtroMenu)

    v.mainloop()


