#2.para heredar porque auto necesita un  motor
from autos.motor import Motor  #otra opcion
#si solo fuera un arcihvo: import *nombrearchivo*

class Auto(Motor):
    #asginacion de variables
    def __init__(self,ruedas=None, puertas=None, tipo=None):
        self.ruedas = ruedas
        self.puertas = puertas
        self.tipo = tipo

#definicion de metodos
#3 habiliades que le acabo de generar a la clase auto
    def fabricarAuto(self, codigoAuto, nombreAuto, codigoMotor):
        self.codigoMotor = codigoMotor 
        MyMotor = Motor()
        motor1 = MyMotor.obtenerMotor(self.codigoMotor)
        with open('./autos/recursos/listaAutos.txt','a') as nuevoAuto:
            data = f'{codigoAuto}|{nombreAuto}|{self.tipo}|{self.ruedas}|{self.puertas}|{motor1[0]}|'
            nuevoAuto.write(data)
            nuevoAuto.close()
        print("Auto Fabricado")
    def comprarAuto(self, tipo):
        self.listarAutos(tipo)
        seleccion = input("Seleccionar un codigo de auto")
        print("Haz comprado un auto!")
    def listarAutos(self, tipo):
        with open('./autos/recursos/listaAutos.txt','r') as Autos:
            for Autos in Autos:
                detalles = Autos.split("|")
                if tipo == detalles[2]:
                    print(Autos)
                    return detalles
            else:
                Autos.close()
                return False
