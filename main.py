class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self, color):
        if (color=='rojo' or color=='verde' or color=='amarillo' or color=='negro' or color=='blanco'):
            self.color=color
 

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=[asientos]
        self.marca=marca
        self.motor=motor
        self.registro=registro
        #cantidadCreados=cantidadCreados

    def cantidadAsientos(self, asientos):
        cantAsientos=0
        for i in range(0,asientos.len):
            if (asientos[i] != False):
                cantAsietos += 1
        return(cantAsientos)

    def verificarIntegridad(self, registro):
        if Motor.registro==registro:
            for i in range(0,Asiento.len):
                if (Asiento[i] != False):
                    if(Asiento[i].registro != registro):
                        return('Las piezas no sonoriginales')
            return('Auto original')
        else:
            return('Las piezas no sonoriginales')


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self, registro):
        self.registro=registro
        
    def asignarTipo(self, tipo):
        if not(tipo=='electrico' or tipo=='gasolina'):
            self.tipo==tipo