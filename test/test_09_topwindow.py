from tkinter import Tk, Button, Label
from widgetTk import widget ,window, menuWidget, windowTop
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

        
    def RUNnew():
        print("sub window")
        vv.run()


    v=window()
    v.header("principal")
    miMenu=menuWidget(data=[["opcion1",[("fullscreen",v.fullScreenSwitch,),("minimizar",v.minimize),("restaurar",v.restore),("maximizar",v.maximize),("center",v.center)]],"opcion2"])
    ww=widget(data=[["hola"],["como vamos"],[(("boton Accion",funEnter),),(("Funcion cerrar",funClose),)],[(("ABRIR SUB",RUNnew),)]])
    ww.config(background="red")
    v.set(varframe=ww,varmenu=miMenu)
    v.event("<Control-p>",funEnter)
    v.eventIfClose(funClose)
    v.size(500,300)
    v.center()
    #v.fullScreenSwitch()
    L=Label(text="hola soy un widget",fg="red")

    www=widget(data=[["hola"],["como vamos"],[(("boton Accion",funEnter),),(("Funcion cerrar",funClose),)],[(("ABRIR SUB",RUNnew),)]])
    www.config(background="blue")



    ll=[
            [("titulo")],
            [("primer titulo"),"texto"],
            [(("boton funcion",funEnter),)],
       ]
 

    vv=windowTop(master=v,dataMenu=["menu1",["menu2","menuu","menuu"]],dataFrame=ll)
    vv.header("run","test.png")
    #vv.minsize(500,400)
    vv.maxsize(500,400)
#    vv.resizable(True,False)


#    vv.title("secundario")
#    miOtroMenu=menuWidget(data=["opcion","otra opcion"])
#    www=widget(data=[("Hola soy una ventana secundaria")])
#    www.config(background="blue")
#    vv.set(varframe=www,varmenu=miOtroMenu)
#    vv.set(varmenu=miOtroMenu)

    v.run()


