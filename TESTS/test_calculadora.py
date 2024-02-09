import unittest
from calculadora import sumar, restar

# Para escribir buenos tests se suele seguir la estrategia AAA (Arrange, Act, Assert)

class TestCalculadora(unittest.TestCase):
    
    def test_sumar(self):
        
        # Arrange es la preparación de los datos de entrada
        x = 2
        y = 2
        
        # Act es la ejecución del código a probar y la obtención del resultado
        resultado = sumar(x, y)
        
        # Y Assert es la verificación del resultado
        self.assertEqual(resultado, 4)

    def test_restar(self):
        
        x = 2
        y = 2
        
        resultado = restar(x, y)
        
        self.assertEqual(resultado, 0)
    

if __name__ == '__main__':
    unittest.main()
