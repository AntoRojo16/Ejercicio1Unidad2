import os
from manejador import ManejadorEmail
from claseEmail import Email


def item1 (unEmail):
    print("Ingrese el nombre de una persona")
    nom=input()
    print("Ingrese su correo")
    correo=input()
    j=correo.find("@")
    k=correo.find("gmail")
    h=correo.find("hotmail")
    p=correo.find(".")
    i=unEmail.getidCuenta()
    d=unEmail.getDominio()
    t=unEmail.gettipoDom()
    idC=correo.find(i)
    do=correo.find(d)
    td=correo.find(t)
    if (j!=-1):
        if ((k!=-1)or(h!=-1)):
            if (p!=-1):
                if(idC!=-1):
                    if(do!=-1):
                        if(td!=-1):
                            print ("estimado " + nom + " te enviaremos tus mensajes a  "+correo)
                        else:
                            print("El tipo de dominio es incorrecto")
                    else:
                        print("El dominio ingresado es incorrecto")
                else:
                    print("El id de la cuenta es incorrecto")
            else:
                print("Error al escribir el correo falta .")
        else:
            print("Error al escribir el correo falta gmail/hotmail")
    else:
        print("Error al escribir el correo falta @ ")
    
    print("Se mostrara la contraseña actual del correo")
    cont=unEmail.getCont()
    print(cont)
def item2(unEmail):
    print("Ingrse contraseña actual")
    contac=input()
    con=unEmail.getCont()
    if(contac==con):
        print("La contraseña se puede cambiar")
        print("Ingrse la nueva contraseña")
        nueva=input()
        unEmail.modificarContr(nueva)
    else:
        print("La contraseña que ingreso no es correcta")

def item3 (unEmail):
    print("Ingrese el correo")
    co=input()
    j=co.find("@")
    k=co.find("gmail")
    h=co.find("hotmail")
    p=co.find(".")
    if (j!=-1):
        if ((k!=-1)or(h!=-1)):
            if (p!=-1):
                unEmail.creaCuenta(co)
                print ("Se creo el objeto Email correctamente")
            else:
                print("Error al escribir el correo falta .")
        else:
            print("Error al escribir el correo falta gmail/hotmail")
    else:
        print("Error al escribir el correo falta @ ")

def item4 ():
    unManejador=ManejadorEmail()
    unManejador.testEmail()

def test ():
    print ("Ingrese ID de cuenta")
    idC=input()
    print("Ingrese dominio")
    dom=input()
    print("Ingreso tipo de  dominio")
    tipoD=input()
    print("Ingrese contraseña")
    cont=input()
    b=0   
    if (dom=="gmail")or(dom=="hotmail"):
        if (tipoD=="com"):
            unEmail=Email(idC,dom,tipoD,cont)
            print("Se mostrara el Email creado")
            unEmail.RetornaEmail()     
        else:
            print("Error al escribir el tipo de dominio")
            b=-1
    else:
        print("Error al escribir el tipo de dominio")
        b=-1
    if (b!=-1):
        dom=unEmail.getDominio()
        print("Se mostrara el dominio del Email creado"+ dom)
    else:
        print("No se puede mostrar el dominio")
    otroEmail=Email("n","n","n","n")
    if (b!=-1):
        print("ITEM 1")
        item1(unEmail)
        #print("ITEM 2")
        ##item2(unEmail)
    print("ITEM 3")
    item3(otroEmail)
    print("ITEM 4")
    item4()




    

if __name__=="__main__":
    os.system('cls')
    test()
    
        
