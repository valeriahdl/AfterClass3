#clase
class Motor:
#constructor   
    def __init__(self, tipoCombustible= None, cilindrada= None, potencia= None, torque= None):
        self.tipoCombustible = tipoCombustible
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.torque = torque
#metodos
#queremos fabricar un motor u obtener motores ya fabricados
    def fabricarMotor(self, codigoMotor, nombreMotor):
        with open('./autos/recursos/listaMotores.txt', 'a') as nuevoMotor:
            data= f'{codigoMotor}|{nombreMotor}|{self.tipoCombustible}|{self.cilindrada}|{self.potencia}|{self.torque}|'
            nuevoMotor.write(data)
            nuevoMotor.close()
        return("Motor fabricado")

    def obtenerMotor(self, codigoMotor=None):
        with open('./autos/recursos/listaMotores.txt', 'r') as Motores:
            for Motor in Motores:
                detalles = Motor.split("|")
                if codigoMotor == detalles[0]:
                    Motores.close()
                    return detalles
            else:
                Motores.close()
                return False
           
#el auto va a usar estos metodos
#fabricarMotor se puede usar desde u  main para fabricar motros
#y obtenerMotor se puede usar desde auto porque cuando yo fabrico un motor necesito asignárselo a un carro

#yo puedo instanciar a motor dentro de la clase auto y desde el main tmb

