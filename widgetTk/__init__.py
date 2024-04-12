from tkinter import Frame,Label,Entry

class widget(Frame):
    def __init__(self,master=None,data=[],vertical=True,split=0,cnf={},**kw):
        super().__init__(master,cnf,**kw)  # hereda todas las cualidades de Frame
        self.split=split                  # vars to widget
        self.isvertical=vertical
        self.listOfSubWidgets=[]
        self.set(data,vertical,split) #config wdidget

    def set(self,dataconfig):
        pass


    def getWidgets(self):
        return self.listOfSubWidgets
    
    def get(self):
        var=[]
        for element in self.listOfSubWidgets:
            try: var.append(element.get())
            except: var.append(None)
        return var

    def set(self,data=[],vertical=True,split=1):
        "internal function to config widget)"
        if type(split)==1:
            if split>0: self.split=split
        self.isvertical=vertical
        self.listOfSubWidgets=[]
        if not(type(data) in [list, tuple]): data=[data]
        for element in data: self.listOfSubWidgets.append(self.__getSubwidget(element))
        self.__unpackAll()
        self.__packAll()

    def  __getSubwidget(self,var):
        # reconoce cada variable y asigna un widget
        if var=="__Entry__": return Entry(self)
        if type(var)==str:return Label(self,text=var)
        if type(var)==list: return widget(self,data=var,vertical=False)
        else: return "lol"

    def __unpackAll(self):
        for element in self.winfo_children():
            element.grid_forget()

    def __packAll(self):
        self.rowVar=0
        self.columnVar=0
        for element in self.listOfSubWidgets:
            element.grid(row=self.rowVar,column=self.columnVar)
            self.__newGridCoordinates()
        
    def __newGridCoordinates(self):
        if self.isvertical:
            self.rowVar+=1
            if self.split and self.rowVar>=self.split:
                self.rowVar=0
                self.columnVar+=1
        else:
            self.columnVar+=1
            if self.split and self.columnVar>=self.split:
                self.columnVar=0
                self.rowVar+=1

  











#---------------------------
if __name__=="__main__":
    from tkinter import Tk
    from tkinter import Button
    t=Tk()
    l=[]
    for x in range(10):
        l.append("elemento "+str(x))
        pass
    l=[["Ingresa tu nombre:","__Entry__"],["Ingresa tu apellido","__Entry__"]]
    w=widget(t,l)
    print(w.get())
    def saludo():
        print(w.get())
        
    w.pack()
    b=Button(t,text="accion",command=saludo)
    b.pack()
    t.mainloop()



