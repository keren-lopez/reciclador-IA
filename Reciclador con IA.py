import pyttsx3
import pandas as pd
import matplotlib.pyplot as plt
lista = list()
#Lista de las canecas 
lista_producto_blanca = list()
lista_material_blanca= list()
lista_cantidad_blanca= list()

lista_producto_verde= list()
lista_material_verde= list()
lista_cantidad_verde= list()

lista_producto_negra= list()
lista_material_negra= list()
lista_cantidad_negra= list()

def talk(texto):
        engine= pyttsx3.init()
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.say(texto)
        engine.runAndWait()
    

class usuarios:
    def _init_(self):
        self.nombre=("")
        self.edad=()
        self.cedula=()
        self.discapacidad=("")

pb0= """Bienvenidos a tu programa de reciclaje IA""" 
print(pb0)
talk(pb0)
def menu():

    seleccion=0
    while seleccion != 4:
        p1="""Elija una de las opciones"""
        print(p1)
        talk(p1)
        print ("----------------------------------------------------------------")
        pr1="""1.Registrarse"""
        print(pr1)
        talk(pr1)
        pr3="""2.Metodo de reciclaje"""
        print (pr3)
        talk(pr3)
        pr4="""3.Grafica"""
        print (pr4)
        talk(pr4)
        pr5="""4.Salir"""
        print (pr5)
        talk(pr5)
        talk("Seleccione una opcion")
        seleccion =int(input("Seleccione una opcion :"))
        if seleccion == 1:
            registrar()
        if seleccion == 2:
            metodo()
        if seleccion== 3:
            grafica()
        if seleccion == 4:
            salir()
def registrar():
    pr6="""Esta es la funcion de registro"""
    print(pr6)
    talk(pr6)
    usuario=usuarios()
    pr7="""Introduzca su nombre"""
    print(pr7)
    talk(pr7)
    usuario.nombre=input(": ")
    pr8="""Introduzca su edad: """
    print(pr8)
    talk(pr8)
    usuario.edad=int(input(": "))
    pr9="""Introduzca su cedula o tarjeda de identidad: """
    print(pr9)
    talk(pr9)
    usuario.cedula=int(input(": "))
    pr10="""¿Presenta alguna limitacion fisica?\n1. Visual \n2. Auditiva\n3. Ninguna \n elija el numero """
    print(pr10)
    talk(pr10)
    discap=int(input(": "))
    usuario.discapacidad = discap 
    print ("¡registro exitoso!")
    talk("¡registro exitoso!")
    lista.append(usuario)

canecas1=("")
caneca_blanca=("")
caneca_verde=("")
caneca_negra =("")



def metodo():
    pr11= """Esta es la funcion de estrategia de reciclaje """
    print (pr11)
    talk(pr11)
    pr12="""¿Presenta habitos de reciclaje?\n1.Si \n2. No"""
    print(pr12)
    talk(pr12)
    habito=int(input(": "))
    p13="""Para hacer uso de reciclaje es importante saber en donde van nuestros residuos, en la actualidad se manejan 3 tipos de canecas:\n Caneca Blanca: Van los residuos aprovechables como: (plastico,carton,vidrio y papel )\n Caneca Verde: Van los residuos organicos aprovechables como (Restos de comida y desechos agricolas)\n Caneca Negra: Van los residos no aprovechables como (Papel higienico, servilletas,papeles contaminados con comida)\n """
    print(p13)
    talk(p13)
    repetir = 1
    while repetir != 0:
        pr14=""" ¿Que tipo de caneca desea utilizar para desechar sus productos \n1. Blanca \n2. Verde  \n3 Negra \nElija el numero: ?"""
        print(pr14)
        talk(pr14)
        canecas1= input(": ")
        if canecas1 == "1":
             pr15="""Digite su producto """
             print(pr15)
             talk(pr15)
             producto_blanca=input(":")
             pr16=""" Que tipo de material es su producto?\n1. plastico \n2. carton \n3. vidrio \n4.papel \nElija el numero """
             print(pr16)
             talk(pr16)
             material_blanca=int(input(": "))
             pr17="""Que cantidad desea ingresar """
             print(pr17)
             talk(pr17)
             cantidad_blanca=int(input(": ")) 
             lista_producto_blanca.append(producto_blanca)
             lista_material_blanca.append(material_blanca)
             lista_cantidad_blanca.append(cantidad_blanca)
             prepetir=""" Desea ingresar otro producto?(digite 0 para no y 1 para si """
             print(prepetir)
             talk(prepetir)
             repetir = int(input(": "))
        elif canecas1 == "2":
             pr15="""Digite su producto """
             print(pr15)
             talk(pr15)
             producto_verde=input(":")
             p19=" ""Que tipo de material es su producto? """
             print(p19)
             talk(p19)
             material_verde=(input(": "))
             pr17="""Que cantidad desea ingresar """
             print(pr17)
             talk(pr17)
             cantidad_verde=int(input(":"))
             lista_producto_verde.append(producto_verde)
             lista_material_verde.append(material_verde)
             lista_cantidad_verde.append(cantidad_verde)
             prepetir=""" Desea ingresar otro producto?(digite 0 para no y 1 para si )"""
             print(prepetir)
             talk(prepetir)
             repetir = int(input(": "))
        elif canecas1 == "3":
             pr15="""Digite su producto """
             print(pr15)
             talk(pr15)
             producto_negra=input(":")
             prm="""Que tipo de material es su producto?\n1. Papel higienico \n2. Servilletas \n3. Papeles contaminados con comida \nElija el numero """
             print(prm)
             talk(prm)
             material_negra=int(input(":"))
             pr17="""Que cantidad desea ingresar """
             print(pr17)
             talk(pr17)
             cantidad_negra=int(input(":"))
             lista_producto_negra.append(producto_negra)
             lista_material_negra.append(material_negra)
             lista_cantidad_negra.append(cantidad_negra)
             prepetir=""" Desea ingresar otro producto?(digite 0 para no y 1 para si) """
             print(prepetir)
             talk(prepetir)
             repetir = int(input(": "))


def grafica():
    #Calculo Caneca Blanca
    if canecas1 == "1": 
      sum_caneca_blanca= sum(lista_cantidad_blanca)
      contador_blanca= len (lista_cantidad_blanca)
      caneca_blanca= (sum_caneca_blanca)/contador_blanca 


    #calculo caneca verde
    if canecas1 == "2": 
        contador_verde= len(lista_cantidad_verde)
        sum_caneca_verde= sum(lista_cantidad_verde)
        caneca_verde= (sum_caneca_verde)/contador_verde

    # calculo caneca negra

    if canecas1 == "3": 
        contador_negra= len(lista_cantidad_negra)
        sum_caneca_negra= sum(lista_cantidad_negra)
        caneca_negra=(sum_caneca_negra)/contador_negra

   
    """lista_de_canecas= [10,20,30]
    etiquetas_canecas=['caneca_blanca','caneca_verde','caneca_negra']

    lista_rrs= [etiquetas_canecas,lista_de_canecas]
    df_rrss=pd.DataFrame(lista_rrs,
               columns=['Nombre Caneca','','Promedio'])
    df_rrss

    plt.bar(df_rrss['Nombre Caneca'], df_rrss['Promedio'])
    plt.show() """
    blanca=['Caneca Blanca', sum (lista_cantidad_blanca)]
    verde= ['Caneca Verde', sum(lista_cantidad_verde)] 
    negra=['Caneca Negra', sum(lista_cantidad_negra)]

    lista_rrs= [blanca,verde,negra]
    df_rrss=pd.DataFrame(lista_rrs,
    columns=['Nombre Caneca','Promedio'])
    df_rrss

    plt.bar(df_rrss['Nombre Caneca'], df_rrss['Promedio'])
    plt.show()

def salir():
    print ("Gracias por usar nuestro algoritmo :)")
#--------------------------------------------------------
menu()