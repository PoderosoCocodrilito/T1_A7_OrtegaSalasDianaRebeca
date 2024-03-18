from math import sqrt

class Calculadora:
    
    def __init__(self, primerNumero = 0, operacion="", segundoNumero=0):
        self.primerNumero = float(primerNumero) 
        self.operacion = operacion
        self.segundoNumero = float(segundoNumero)
        
    
    def sumar(self):
        return float(self.primerNumero) + float(self.segundoNumero)
    def restar(self):
        return float(self.primerNumero) - float(self.segundoNumero)
    def multiplicar(self):
        return float(self.primerNumero) * float(self.segundoNumero)
    def dividir(self):
        return float(self.primerNumero) / float(self.segundoNumero)
    def residuar(self):
        return float(self.primerNumero) % float(self.segundoNumero)
    def dividirSobreX(self):
        return 1 / float(self.segundoNumero)
    def borrar(self):
        return ""
    def borrarUno(self, textoDeCalculadora):
        self.texto = textoDeCalculadora
        nuevotexto=""
        for i in range(len(textoDeCalculadora)):
            nuevotexto= textoDeCalculadora[0:i:]
            print(i)
        return nuevotexto
    def cuadrado(self):
        return  float(self.segundoNumero)* float(self.segundoNumero)
    def raiz(self):
        return  float(sqrt(self.segundoNumero))
    
    def indicarOperacion_Numero(self, num, op):
        self.primerNumero = num
        self.operacion = op
        print(self.primerNumero)
        print(self.operacion)
        
    def indicarSegundoNumero(self, num):
        self.segundoNumero = num
        print(self.segundoNumero)
        
        
    def realizarOperacion(self, texto):
        if(self.operacion=="+"):
            return self.sumar()
        elif(self.operacion=="-"):
            return self.restar()
        elif(self.operacion=="*"):
            return self.multiplicar()
        elif(self.operacion=="/"):
            return self.dividir()
        elif(self.operacion=="%"):
            return self.residuar()
        elif(self.operacion=="AC"):
            return self.borrar()
        elif(self.operacion=="borrar"):
            return self.borrarUno("")
        elif(self.operacion=="√"):
            return self.raiz()
        elif(self.operacion=="x²"):
            return self.cuadrado()
        elif(self.operacion=="1/X"):
            return self.dividirSobreX()








