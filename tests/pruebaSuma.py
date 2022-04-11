import unittest
from src.logica.Suma import Suma

class PruebaSuma(unittest.TestCase):
    def setUp(self):
        self.suma = Suma()

    def tearDown(self):
        self.suma=None

    def test_suma_operacionSuma_dosNumerosPositivos_retornaSuma(self):
        # Organizar
        self.sumando1 = 3
        self.sumando2 = 7
        self.resultadoesperado = 10

        # Actuar
        self.resultadoActual = self.suma.operacionSuma(self.sumando1, self.sumando2)

        # Evaluar
        self.assertEqual(self.resultadoesperado, self.resultadoActual)

    def test_suma_operacionSuma_dosNumerosNegativos_retornaSuma(self):
        # Organizar
        self.sumando1 = -3
        self.sumando2 = -7
        self.resultadoesperado = -10

        # Actuar
        self.resultadoActual = self.suma.operacionSuma(self.sumando1, self.sumando2)

        # Evaluar
        self.assertEqual(self.resultadoesperado, self.resultadoActual)