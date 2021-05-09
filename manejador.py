import csv
from claseEmail import Email
class ManejadorEmail:
    def __init__(self):
        self.__listaEmail=[]
        
    def AgregarEmail (self,unEmail):
        self.__listaEmail.append(unEmail)
    
    def testEmail (self):
        archivo=open("Email.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader :
            if bandera:
                '''saltear cabecera'''
                bandera=not bandera
            else:
                email=fila[0]
                unEmail=Email("0","0","0","0")
                unEmail.creaCuenta(email)
                unEmail.RetornaEmail()
                self.AgregarEmail(unEmail)
        archivo.close()