# Este principio nos dice que una clase debe tener una sola razón para cambiar, es decir, una clase debe tener una sola responsabilidad.

# Ejemplo de una clase que no cumple con el principio de responsabilidad única:

# Esta clase viola el principio de responsabilidad única, ya que tiene dos razones para cambiar: 
# si cambia la forma en que se almacenan los datos o si cambia la forma en que se maneja la información del empleado.
class Empleado:
    """gestiona la información de un empleado y al mismo tiempo maneja la logica de almacenamiento de datos"""
    
    def __init__(self, nombre, edad, puesto, salario):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        self.salario = salario
    
    def guardar_datos_empleado(self):
        """guarda la información del empleado en la base de datos"""
        # Codigo para guardar la información del empleado en la base de datos
        pass

# El problema con esta clase es que si cambia la forma en que se almacenan los datos, también tendrá que cambiar la clase Empleado.

# Para solucionar este problema, podemos dividir la clase Empleado en dos clases separadas: 
# una para manejar la información del empleado y otra para manejar el almacenamiento de datos.

class Empleado:
    """gestiona la información de un empleado"""
    
    def __init__(self, nombre, edad, puesto, salario):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        self.salario = salario


class AlmacenamientoDatosEmpleado:
    def guardar_datos_empleado(self, empleado):
        """guarda la información del empleado en la base de datos"""
        # Codigo para guardar la información del empleado en la base de datos
        pass
