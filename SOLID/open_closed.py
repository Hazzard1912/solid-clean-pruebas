# Este principio nos dice que una clase debe estar abierta para extensión pero cerrada para modificación, es decir, 
# una clase debe ser fácil de extender sin necesidad de modificar su código fuente.

# Ejemplo de una clase que no cumple con el principio de abierto/cerrado:

class GeneradorReportes:
    """genera reportes en formato HTML"""
    
    def generar_reporte_html(self, contenido):
        """genera un reporte en formato HTML"""
        # Codigo para generar un reporte en formato HTML
        return f"<html>{contenido}</html>"
    
# En este caso, si queremos agregar soporte para generar reportes en formato PDF,
# tendremos que modificar la clase GeneradorReportes para agregar un nuevo método generar_reporte_pdf.
# Esto viola el principio de abierto/cerrado, ya que estamos modificando el código existente en lugar de extenderlo.

# Ejemplo de uso de el principio de abierto/cerrado:
from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    """genera reportes"""
    
    @abstractmethod
    def generar_reporte(self, contenido):
        pass


class GeneradorReportesHTML(ReportGenerator):
    """genera reportes en formato HTML"""
    
    def generar_reporte(self, contenido):
        """genera un reporte en formato HTML"""
        # Codigo para generar un reporte en formato HTML
        return f"<html>{contenido}</html>"


class GeneradorReportesPDF(ReportGenerator):
    """genera reportes en formato PDF"""
    
    def generar_reporte(self, contenido):
        """genera un reporte en formato PDF"""
        # Codigo para generar un reporte en formato PDF
        return f"PDF: {contenido}"

# El beneficio de utilizar el principio de abierto/cerrado es que hace que el código sea más fácil de mantener y extender.
# Al evitar la modificación de las clases existentes, reducimos el riesgo de introducir errores en el código existente. 
