import unittest
from Algoritmo_Verifica_Triangulo import eh_triangulo, tipo_triangulo

class TestTrianguloFunctions(unittest.TestCase):

    def test_eh_triangulo_valido(self):
        # Teste com lados que formam um triângulo equilátero
        self.assertTrue(eh_triangulo(3, 3, 3))

        # Teste com lados que formam um triângulo isósceles
        self.assertTrue(eh_triangulo(3, 3, 4))

        # Teste com lados que formam um triângulo escaleno
        self.assertTrue(eh_triangulo(3, 4, 5))

if __name__ == '__main__':
    unittest.main()
