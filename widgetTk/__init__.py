from tkinter import Frame,Label,Entry,Checkbutton
import tkinter

class widget(Frame):
    def __init__(self,master=None,data=[],vertical=True,split=0,editable=False,static=False,cnf={},**kw):
        super().__init__(master,cnf,**kw)  # hereda todas las cualidades de Frame
        self.split=split                  # vars to widget
        self.isvertical=vertical
        self.static=static
        self.original=[]
        self.listOfSubWidgets=[]
        self.__editable=False
        self.__isMatrix=False         #default for Matrix Mode
        self.__maxColumnMatrix=0
        self.set(data,vertical,split,editable,static) #config wdidget

    def getWidgets(self):
        return self.listOfSubWidgets
    
    def get(self,option="None"):
        # option None - do nothing
        # optio  Number - 
        firstv=[]
        var=[]
        counter=0
        for element in self.listOfSubWidgets:
            try:    firstv.append(element.get())
            except: firstv.append(self.original[counter])
            counter+=1
        #------------------------
        for x in firstv:
            if option=="None": var.append(x) # Do nothing
        #------------------------
        if self.__isMatrix:
            matrix=[];row=[]
            for x in var:
                row.append(x)
                if len(row)>=self.__maxColumnMatrix:
                    matrix.append(row[:]);row=[]
            return matrix
        else: return var

    def set(self,data=[],vertical=True,split=1,editable=False,static=False):
        "internal function to config widget)"
        if type(split)==int:
            if split>0: self.split=split
        self.isvertical=vertical
        self.listOfSubWidgets=[]
        self.static=static
        self.original=[]
        self.__editable=editable
        if not(type(data) in [list, tuple]): data=[data]
        formatData=self.__formatMatrixData(data)
        for element in formatData:
            self.listOfSubWidgets.append(self.__getSubwidget(element))
            self.original.append(element)
        self.__unpackAll()
        self.__packAll()

    def __formatMatrixData(self,inputData):
        self.__isListOfLists(inputData)
        if self.__isMatrix:
            formatData=[]
            for fila in inputData:
                for x in range(self.__maxColumnMatrix):
                    try: formatData.append(fila[x])
                    except: formatData.append(None)
            return formatData
        else:return inputData

    def __isListOfLists(self,item):
        self.__isMatrix=False
        self.__maxColumnMatrix=0
        if type(item)==list:
            self.__isMatrix=True
            for x in item:
                if type(x)==list:
                    self.__maxColumnMatrix=max(self.__maxColumnMatrix,len(x))
                else:self.__isMatrix=False

    def  __getSubwidget(self,var):
        # reconoce cada variable y asigna un widget
        if var=="__Entry__" and  not(self.static): return Entry(self)
        elif var=="__Entry__" and self.static: return Label(self)
        if var==None: return Label(self)
        #--------------------------------------------------------
        if type(var) == str and var=="" and not(self.__editable):
            return Label(self,text=var)
        elif type(var) == str and self.__editable:
            e=Entry(self)
            e.insert(0,str(var))      
            if self.static:
                e.config(state="disabled")
            return e
        #---------------------------------------------------------
        elif type(var) in [int,float,str] :
            e=Entry(self)
            e.insert(0,str(var))
            if self.static:
                e.config(state="disabled")
            return e
        #---------------------------------------------------------
        elif type(var)==dict:
            return self.__makeWidgetFromDict(var)
        #---------------------------------------------------------
        elif  type(var) == bool:
            c=Checkbutton(self)
            if var: c.select()
            else:   c.deselect()
            if self.static:
                c.config(state="disabled")
            return c
        #---------------------------------------------------------
        if type(var)==list: return widget(self,data=var,vertical=False)
        else: return "lol"

    def __makeWidgetFromDict(self,dataDict):
        typeStr="Label" #default
        try:typeStr=dataDict["type"][:]
        except: pass
        try: del dataDict["type"]
        except:pass
        try:
            clasw=getattr(tkinter,typeStr)
            w=clasw(self,**dataDict)
            return w
        except:
            return Label(self,text="__Error_"+str(typeStr)+"__")

    def __unpackAll(self):
        for element in self.winfo_children():
            element.grid_forget()

    def __packAll(self):
        if self.__isMatrix:
            self.split=self.__maxColumnMatrix
            self.isvertical=False
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

  











#--------------------------- "
if __name__=="__main__":
    from tkinter import Tk
    from tkinter import Button
    t=Tk()
    l=[]
    for x in range(10):
        l.append("elemento "+str(x))
        pass
    l=[["nombre:","__Entry__",True,19,1.7],["Ingresa tu apellido","__Entry__"],["lolo"],["ll",12,"k"],
       [
           {
               "type":"Label" ,           
               "text": "Hola, mundo!",
    "bg": "lightblue",
    "fg": "black",
    "font": ("Arial", 12),
    "padx": 10,
    "pady": 5

            }
           ]
       ]
    #w=widget(t,data=l,editable=False,static=False)

    w=widget(t,data=l)
    def saludo():
        ll=(w.get())
        ll.append([["tu nombre"]])
        w.set(ll)
        
    w.pack()
    b=Button(t,text="accion",command=saludo)
    b.pack()
    t.mainloop()



