class Email:
    __idCuenta=""
    __Dominio=""
    __tipoDom=""
    __Contr=""
    
    def __init__ (self,idC="idcuenta",dom="dominio",tipoD="tipodominio",Contr="contra"):
        self.__idCuenta=idC
        self.__Dominio=dom
        self.__tipoDom=tipoD
        self.__Contr=Contr
     
    
    def getidCuenta(self):
        return self.__idCuenta
    
    def getDominio(self):
        return self.__Dominio
    
    def gettipoDom(self):
        return self.__tipoDom
    
    def getCont(self):
        return self.__Contr
        
    
    def RetornaEmail(self):
        email=self.__idCuenta+"@"+self.__Dominio+"."+self.__tipoDom
        print (email)
    
    def creaCuenta(self,correo):
        lista=correo.split(sep="@")
        idCuen=lista[0]
        lista2=lista[1]
        lista3=lista2.split(sep=".")
        dom=lista3[0]
        tdom=lista3[1]
        print("ingrese contraseña")
        con=input()
        self.__idCuenta=idCuen
        self.__Dominio=dom
        self.__tipoDom=tdom
        self.__Contr=con
        
    def modificarContr (self, nueva):
        self.__Contr=nueva
        print("La nueva contraseña es "+self.__Contr)
        
        

