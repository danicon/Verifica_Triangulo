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

    def test_eh_triangulo_invalido(self):
        # Teste com lados negativos (não deve formar triângulo)
        self.assertFalse(eh_triangulo(-1, -2, -3))

        # Teste com lados que possuem um valor igual a zero (não deve formar triângulo)
        self.assertFalse(eh_triangulo(0, 1, 2))
    
    def test_tipo_triangulo(self):
        # Teste com triângulo equilátero
        self.assertEqual(tipo_triangulo(3, 3, 3), "Equilátero")

        # Teste com triângulo isósceles
        self.assertEqual(tipo_triangulo(3, 3, 4), "Isósceles")

        # Teste com triângulo escaleno
        self.assertEqual(tipo_triangulo(3, 4, 5), "Escaleno")

if __name__ == '__main__':
    unittest.main()
