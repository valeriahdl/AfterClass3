from autos.motor import Motor
from autos.auto import Auto
def crearMotor():
    newMotor = Motor("Gasolina","2.0","255Hp","320Nm")
    print(newMotor.fabricarMotor("focus-a10", "Ecoboost"))

def ComprarMotor():
    getMotor = Motor()
    print(getMotor.obtenerMotor("focus-a10"))

#crearMotor()
#ComprarMotor()

def fabricarAuto():
    newAuto = Auto("4","2","hatchback")
    newAuto.fabricarAuto("ford-f1","Ford","focus-a10")
    
fabricarAuto()
