# Este principio nos dice que las clases derivadas deben ser sustituibles por sus clases base, es decir,
# que un objeto de una clase derivada debe poder ser sustituido por un objeto de su clase base sin afectar el comportamiento del programa.

# Ejemplo de una clase que no cumple con el principio de sustitución de Liskov:
from abc import ABC, abstractmethod


class Vehiculo(ABC):
    @abstractmethod
    def encender(self):
        pass    


class Moto(Vehiculo):
    def encender(self):
        print("encendiendo moto")


class Bicicleta(Vehiculo):
    def encender(self):
        # Podria ser incluso un raise NotImplementedError
        print("no puedo encender")

    
# Cuando heredamos de una clase, y notamos que hay metodos que o no hacen nada, o simplemente devuelven un error del tipo NotImplementedError,
# es una señal de que la clase no cumple con el principio de sustitución de Liskov, ya que, en un metodo que espera un objeto de la clase base,
# no podremos sustituirlo por un objeto de la clase derivada, ya que el comportamiento del programa no será el esperado.

def encender_vehiculo(vehiculo):
    vehiculo.encender()


moto = Moto()
bicicleta = Bicicleta()

encender_vehiculo(moto) # encendiendo moto
encender_vehiculo(bicicleta) #! no puedo encender - Esto podria ser un problema mayor en un programa mas grande

# Ejemplo de una clase que cumple con el principio de sustitución de Liskov:

class VehiculoMotorizado(ABC):
    @abstractmethod
    def encender(self):
        pass
            

class Moto(Vehiculo):
    def encender(self):
        print("encendiendo moto")


class Carro(Vehiculo):
    def encender(self):
        print("encendiendo carro")
