from tkinter import Frame,Label,Entry,Checkbutton
from tkinter import Menu,Button,Tk,PhotoImage  
from tkinter import Canvas,Toplevel
from tkinter.ttk import Combobox
import tkinter

class widget(Frame):
    def __init__(self,data=[],vertical=True,split=0,editable=True,static=False,master=None,cnf={},**kw):
        super().__init__(master,cnf,**kw)  # hereda todas las cualidades de Frame
        self.split=split                  # vars to widget
        self.isvertical=vertical
        self.static=static
        self.original=[]
        self.tkvars=[]
        self.listOfSubWidgets=[]
        self.__editable=editable
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

    def set(self,data=[],vertical=True,split=1,editable=True,static=False):
        "internal function to config widget)"
        if type(split)==int:
            if split>0: self.split=split
        self.isvertical=vertical
        self.listOfSubWidgets=[]
        self.static=static
        self.original=[]
        self.tkvars=[]
        self.__editable=editable
        if not(type(data) in [list]): data=[data]
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
        #--------------------------------------------------------
        if   var=="" and  not(self.static): return Entry(self)
        elif var=="" and  self.static: return Label(self)
        #--------------------------------------------------------
        elif var==None: return Label(self)
        #--------------------------------------------------------
        elif type(var) == str and var=="" and not(self.__editable):
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
        elif  type(var) == tuple:
            return self.__tupleWidget(var)
        #---------------------------------------------------------
        elif type(var)==list: return widget(self,data=var,vertical=False)
        else: return Label(self,text="unknow")
        #---------------------------------------------------------


    def __tupleWidget(self,dataTuple):
        if len(dataTuple)==0: return Label(self)
        elif len(dataTuple)==1 and type(dataTuple[0]) in [str,int,float,bool]:
            return Label(self,text=str(dataTuple[0]))
        elif len(dataTuple)==1 and type(dataTuple[0]) == dict:
            return self.__makeWidgetFromDict(dataTuple[0])
        elif type(dataTuple[0])==list:  #----list 
            if len(dataTuple)==1 and not(self.static):
                return Combobox(self,values=dataTuple[0])
            elif len(dataTuple)==1 and (self.static):
                return Combobox(self,values=dataTuple[0],state="disabled")
            elif len(dataTuple)==2 and not(self.static):
                self.tkvars.append(tkinter.StringVar(value=str(dataTuple[1])))
                pointer=len(self.tkvars)-1
                return Combobox(self,textvariable=self.tkvars[pointer],values=dataTuple[0])
            elif len(dataTuple)==2 and (self.static):
                self.tkvars.append(tkinter.StringVar(value=str(dataTuple[1])))
                pointer=len(self.tkvars)-1
                return Combobox(self,textvariable=self.tkvars[pointer],values=dataTuple[0],state="disabled")
            elif len(dataTuple)==3 and not(self.static):  #combobox whith options
                self.tkvars.append(tkinter.StringVar(value=str(dataTuple[1])))
                pointer=len(self.tkvars)-1
                if dataTuple[2]==True:
                    return Combobox(self,textvariable=self.tkvars[pointer],values=dataTuple[0])
                else:
                    return Combobox(self,textvariable=self.tkvars[pointer],values=dataTuple[0],state="disabled")
            elif len(dataTuple)==3 and self.static:  #combobox whith options
                self.tkvars.append(tkinter.StringVar(value=str(dataTuple[1])))
                pointer=len(self.tkvars)-1
                return Combobox(self,textvariable=self.tkvars[pointer],values=dataTuple[0],state="disabled")
            elif not(self.static):  #combobox whith command
                self.tkvars.append(tkinter.StringVar(value=str(dataTuple[1])))
                pointer=len(self.tkvars)-1
                if dataTuple[2]==True:
                    self.tkvars.append(dataTuple[3])
                    limite=len(self.tkvars)-1
                    c=Combobox(self,textvariable=self.tkvars[pointer],values=dataTuple[0])
                    def otherfun(voidVar): dataTuple[3]()
                    c.bind("<<ComboboxSelected>>",otherfun) # [3]) #<--- corregir
                    return c
                else:
                    return Combobox(self,textvariable=self.tkvars[pointer],values=dataTuple[0],state="disabled")
            else :  #combobox whith options
                self.tkvars.append(tkinter.StringVar(value=str(dataTuple[1])))
                pointer=len(self.tkvars)-1
                return Combobox(self,textvariable=self.tkvars[pointer],values=dataTuple[0],state="disabled")
        elif type(dataTuple[0]==tuple):  #--- tuple
            if len(dataTuple[0])==0:
                return Button(self)
            elif len(dataTuple[0])==1 and not(self.static):
                return Button(self,text=str(dataTuple[0][0]))
            elif len(dataTuple[0])==1 and (self.static):
                return Button(self,text=str(dataTuple[0][0]),state="disabled")
            elif len(dataTuple[0])==2 and not(self.static):
                return Button(self,text=str(dataTuple[0][0]),command=dataTuple[0][1])
            elif len(dataTuple[0])==2 and self.static:
                return Button(self,text=str(dataTuple[0][0]),command=dataTuple[0][1],state="disabled")
            elif not(self.static):
                if dataTuple[0][2]==True:
                    return Button(self,text=str(dataTuple[0][0]),command=dataTuple[0][1])
                else:
                    return Button(self,text=str(dataTuple[0][0]),command=dataTuple[0][1],state="disabled")
            else:
                return Button(self,text=str(dataTuple[0][0]),command=dataTuple[0][1],state="disabled")

        else: return Label(self,text="")


    def __makeWidgetFromDict(self,dataDict):
        typeStr="Label" #default
        try:typeStr=dataDict["type"][:]
        except: pass
        try: del dataDict["type"]
        except:pass
        w=Label(self,text="Error_"+str(typeStr)+"__")
        try:
            clasw=getattr(tkinter,typeStr)
            w=clasw(self,**dataDict)
        except:
            pass
        return w

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
            element.grid(row=self.rowVar,column=self.columnVar,sticky="nsew")
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

  



class menuWidget(Menu):

    def __init__(self,data=[],master=None,cnf={},**kw):
        super().__init__(master,cnf,**kw)
        self.__data=data
        self.set(self.__data)

    def __deleteAll(self):
        self.delete(0,"end")

    def set(self,data=[]):
        self.__deleteAll()
        if type(data)!=list: data=[data]
        for x in data:
            self.__getElementByObj(x,self)

    def __getElementByObj(self,element,father,submenu=[]):
        #-- submenu----------------------
        haveSubmenu=False
        submenuOBJ=None
        if submenu==None: submenu=[]
        if type(submenu)!=list: submenu=[submenu]
        if len(submenu)!=0: haveSubmenu=True
        #-------------------------------
        if haveSubmenu:
            submenuOBJ=tkinter.Menu(father,tearoff=0)
            for x in submenu:
                self.__getElementByObj(x,submenuOBJ)
        #-------------------------------
        if element=="":
            father.add_separator()
        elif type(element) in [str,int,float,bool] and not(haveSubmenu):
            father.add_command(label=str(element))
        elif type(element) in [str,int,float,bool] and haveSubmenu:
            father.add_cascade(label=str(element),menu=submenuOBJ)
        elif type(element)==list:
            if len(element)==0: pass
            elif len(element)==1:
                self.__getElementByObj(element[0],father)
            elif len(element)==2:
                first=element[0]
                second=element[1]
                if type(second)!= list: second=[second]
                self.__getElementByObj(first,father,second)
            else:
                first=None
                seconds=[]
                for x in range(len(element)):
                    if x: seconds.append(element[x])
                    else: first=element[0]
                self.__getElementByObj(first,father,seconds)
        #-------------
        elif  type(element)==tuple:
            if len(element)==0: pass
            elif len(element)==1:
                father.add_command(label=str(element[0]))
            elif len(element)==2:
                if type(element[1])==bool and element[1]:
                    father.add_command(label=str(element[0]))
                elif type(element[1])==bool and not(element[1]):
                    father.add_command(label=str(element[0]),state="disabled")
                else:
                    father.add_command(label=str(element[0]),command=element[1])
            else:
                if type(element[2])==bool:
                    if element[2]:
                        father.add_command(label=str(element[0]),command=element[1])
                    else:
                        father.add_command(label=str(element[0]),state="disabled")
                        #father.entryconfig(label=str(element[0]),state="disabled")
        #-------------------------------------------
        else:
            father.add_command(label="__Error__")


class window(Tk):

    def __init__(self,varframe=None,varmenu=None):
        super().__init__()
        self.__frame=varframe
        self.__menu=varmenu
        self.__functions=[]
        # canvas to fit window ------
        self.__canvas=Canvas(self)
        self.__canvas.pack(fill=tkinter.BOTH,expand=True)
        self.__frame_id=None
        self.__packFrame=False
        #----------------------------
        self.__PhotoImage=None
        self.set(self.__frame,self.__menu)

    def __unpackAll(self):
        pass

    def fullScreenSwitch(self):
        if self.attributes("-fullscreen"): self.attributes("-fullscreen",False)
        else:self.attributes("-fullscreen",True)

    def minimize(self): self.state("iconic")
    def maximize(self): self.state("zoomed")
    def restore(self):  self.state("normal")
    def run(self):      self.mainloop()
    def quit(self):     self.destroy()

    def getFrame(self): return self.__frame
    def getMenu(self):  return self.__menu

    def size(self,dimx,dimy):
        try: self.geometry(str(int(dimx))+"x"+str(int(dimy)))
        except: pass

    def header(self,title=None,iconPng=None):
        if title!=None:self.title(str(title))
        if iconPng!=None:
            self.__PhotoImage=PhotoImage(master=self,file=str(iconPng))
            self.iconphoto(False,self.__PhotoImage)

    def set(self,varframe=None,varmenu=None):
        self.__unpackAll()
        self.__frame=varframe
        self.__menu=varmenu
        if self.__menu!=None:self.config(menu=self.__menu)
        if self.__frame!=None:
            self.__packFrame=True
            self.__frame_id = self.__canvas.create_window((0, 0), window=self.__frame, anchor=tkinter.NW)
            self.__canvas.bind("<Configure>",self.__resize)

    def event(self,keyEvent,funEnvent):
        def newFun(event=None): funEnvent()
        self.__functions.append(newFun)
        counter=len(self.__functions)-1
        self.bind(str(keyEvent),self.__functions[counter])

    def __resize(self,event):
        self.__canvas.itemconfig(self.__frame_id, width=event.width, height=event.height)
        pass

    def eventIfClose(self,function):
        self.protocol("WM_DELETE_WINDOW", function)

    

class windowTop:

    def __init__(self,master=None,varframe=None,varmenu=None):
        # is running
        self.__isrunning=False # True if is running
        # first vars
        self.__master=master
        self.__frame=varframe
        self.__varmenu=varmenu
        # resize vars
        self.__resizable=None  # (True,False)
        self.__minsize=None    # (200,300)
        self.__maxsize=None    # (1200,1300)
        self.__size=None       # (300,300)
        # window values
        self.__state="normal"  #  state win
        self.__nameWin=None
        self.__iconWin=None
        self.__fullscreen=False
        # events
        self.__events=[]       # all events
        self.__eventClose=None 
        # Internal Vars 


    def run(self):

        pass






#--------------------------- "

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
    miMenu=menuWidget(data=[["opcion1",[("fullscreen",v.fullScreenSwitch,),("minimizar",v.minimize),("restaurar",v.restore),("maximizar",v.maximize)]],"opcion2"])
    ww=widget(data=[["hola"],["como vamos"],[(("boton Accion",funEnter),),(("Funcion cerrar",funClose),)],[(("ABRIR SUB",RUNnew),)]])
    ww.config(background="red")
    v.set(varframe=ww,varmenu=miMenu)
    v.event("<Control-p>",funEnter)
    v.eventIfClose(funClose)
    #v.fullScreenSwitch()


    vv=windowTop(master=v)
#    vv.title("secundario")
#    miOtroMenu=menuWidget(data=["opcion","otra opcion"])
#    www=widget(data=[("Hola soy una ventana secundaria")])
#    www.config(background="blue")
#    vv.set(varframe=www,varmenu=miOtroMenu)
#    vv.set(varmenu=miOtroMenu)

    v.mainloop()


