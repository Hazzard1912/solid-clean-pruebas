# Este principio nos dice que los modulos de alto nivel no deben depender de los modulos de bajo nivel, ambos deben depender de abstracciones.

# Caso donde no se aplican los principios de dependencia de inversion

class Lampara:
    def encender(self):
        print("encendiendo lampara")


class Interruptor:
    def __init__(self, ):
        self.lampara = Lampara() #! esto no cumple con el principio de inversion de dependencia, se ve el acoplamiento entre las clases
    
    def operar(self):
        self.lampara.encender()


lampara = Lampara()
interruptor = Interruptor(lampara)
interruptor.operar() # encendiendo lampara

# Caso donde se aplican los principios de inversion de dependencia

class DispositivoEncendible:
    def encender(self):
        pass


class Lampara(DispositivoEncendible):
    def encender(self):
        print("encendiendo lampara")


class Televisor(DispositivoEncendible):
    def encender(self):
        print("encendiendo televisor")


class Interruptor:
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo
    
    def operar(self):
        self.dispositivo.encender()


lampara = Lampara()
televisor = Televisor()

interruptor = Interruptor(lampara)
interruptor.operar() # encendiendo lampara

interruptor = Interruptor(televisor)
interruptor.operar() # encendiendo televisor

# En este caso, la clase Interruptor depende de la clase DispositivoEncendible, lo cual cumple con el principio de inversion de dependencia
# Si queremos usar el interruptor con otro dispositivo que no sea una lampara o un televisor, podremos hacerlo sin modificar la clase Interruptor

# Basicamente, tanto la clase de alto nivel (Interruptor) como la clase de bajo nivel (Lampara, Televisor) dependen de abstracciones (DispositivoEncendible),
