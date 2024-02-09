#  Este principio nos dice que ninguna clase debe ser forzada a implementar métodos que no utilizará.

# Ejemplo de una clase que no cumple con el principio de segregación de interfaces:


class Trabajador:
    def trabajar(self):
        pass

    def comer(self):
        pass


class Humano(Trabajador):
    def trabajar(self):
        return "Trabajando..."

    def comer(self):
        return "Comiendo..."


class Robot(Trabajador):
    def trabajar(self):
        return "Trabajando..."
    
    def comer(self):
        # Podria ser incluso un raise NotImplementedError
        return "no necesito comer"


# En este caso, la clase Robot no cumple con el principio de segregación de interfaces, ya que esta siendo
# forzada a implementar un método que no utilizará, el método comer.

# Ejemplo de una clase que cumple con el principio de segregación de interfaces:

from abc import ABC, abstractmethod


class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass


class Comelon(ABC):
    @abstractmethod
    def comer(self):
        pass


class Humano(Trabajador, Comelon):
    def trabajar(self):
        return "Trabajando..."

    def comer(self):
        return "Comiendo..."


class Robot(Trabajador):
    def trabajar(self):
        return "Trabajando..."
    

# En este caso, se cumple con el principio de segregación de interfaces, ya que no ninguna clase esta siendo
# forzada a implementar un método que no utilizará, el método comer.
