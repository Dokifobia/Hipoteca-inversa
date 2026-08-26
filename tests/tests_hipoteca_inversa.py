import unittest
from src.model import logica_hipoteca_inversa

class TestHipoteca(unittest.TestCase):

    # Casos normales
    def test_normal_1(self):
        valor_inmueble = 300_000_000
        porcentaje = 0.40
        tasa_mensual = 0.012
        plazo_meses = 120

        cuota_esperada = 1892165.77
        abonos_esperado = 227059892.25
        intereses_esperado = 107059892.25

        cuota, abonos, intereses = desembolso_mensual(valor_inmueble, porcentaje, tasa_mensual, plazo_meses)

        self.assertAlmostEqual(cuota, cuota_esperada, places=2)
        self.assertAlmostEqual(abonos, abonos_esperado, places=2)
        self.assertAlmostEqual(intereses, intereses_esperado, places=2)

    def test_normal_2(self):
        valor_inmueble = 150_000_000
        porcentaje = 0.50
        tasa_mensual = 0.009
        plazo_meses = 60

        cuota_esperada = 1623211.07
        abonos_esperado = 97392664.32
        intereses_esperado = 22392664.32

        cuota, abonos, intereses = desembolso_mensual(valor_inmueble, porcentaje, tasa_mensual, plazo_meses)

        self.assertAlmostEqual(cuota, cuota_esperada, places=2)
        self.assertAlmostEqual(abonos, abonos_esperado, places=2)
        self.assertAlmostEqual(intereses, intereses_esperado, places=2)

    def test_normal_3(self):
        valor_inmueble = 500_000_000
        porcentaje = 0.30
        tasa_mensual = 0.015
        plazo_meses = 48

        cuota_esperada = 4406249.94
        abonos_esperado = 211499997.18
        intereses_esperado = 61499997.18

        cuota, abonos, intereses = desembolso_mensual(valor_inmueble, porcentaje, tasa_mensual, plazo_meses)

        self.assertAlmostEqual(cuota, cuota_esperada, places=2)
        self.assertAlmostEqual(abonos, abonos_esperado, places=2)
        self.assertAlmostEqual(intereses, intereses_esperado, places=2)

    # Casos extraordinarios
    def test_extraordinario_tasa_cero(self):
        valor_inmueble = 200_000_000
        porcentaje = 0.50
        tasa_mensual = 0.0
        plazo_meses = 36

        cuota_esperada = 2777777.78
        abonos_esperado = 100000000.00
        intereses_esperado = 0.00

        cuota, abonos, intereses = desembolso_mensual(valor_inmueble, porcentaje, tasa_mensual, plazo_meses)

        self.assertAlmostEqual(cuota, cuota_esperada, places=2)
        self.assertAlmostEqual(abonos, abonos_esperado, places=2)
        self.assertAlmostEqual(intereses, intereses_esperado, places=2)

    def test_extraordinario_unica_disposicion(self):
        valor_inmueble = 100_000_000
        porcentaje = 1.00
        tasa_mensual = 0.024
        plazo_meses = 1

        cuota_esperada = 102400000.00
        abonos_esperado = 102400000.00
        intereses_esperado = 2400000.00

        cuota, abonos, intereses = desembolso_mensual(valor_inmueble, porcentaje, tasa_mensual, plazo_meses)

        self.assertAlmostEqual(cuota, cuota_esperada, places=2)
        self.assertAlmostEqual(abonos, abonos_esperado, places=2)
        self.assertAlmostEqual(intereses, intereses_esperado, places=2)

    def test_extraordinario_plazo_maximo(self):
        valor_inmueble = 250_000_000
        porcentaje = 0.40
        tasa_mensual = 0.018
        plazo_meses = 240

        cuota_esperada = 1825226
        abonos_esperado = 438054262
        intereses_esperado = 338054262

        cuota, abonos, intereses = desembolso_mensual(valor_inmueble, porcentaje, tasa_mensual, plazo_meses)

        self.assertAlmostEqual(cuota, cuota_esperada, places=0)
        self.assertAlmostEqual(abonos, abonos_esperado, places=0)
        self.assertAlmostEqual(intereses, intereses_esperado, places=0)

    # Casos de error
    def test_error_valor_inmueble_cero(self):
        with self.assertRaises(ValorPropiedadCero):
            desembolso_mensual(0, 0.40, 0.012, 60)

    def test_error_tasa_usura(self):
        with self.assertRaises(HipotecaUsura):
            desembolso_mensual(200_000_000, 0.50, 0.05, 36)

    def test_error_plazo_cero(self):
        with self.assertRaises(PlazoMenorIgualCero):
            desembolso_mensual(150_000_000, 0.30, 0.012, 0)

    def test_error_plazo_negativo(self):
        with self.assertRaises(PlazoMenorIgualCero):
            desembolso_mensual(150_000_000, 0.30, 0.012, -12)

    def test_error_plazo_mayor_240(self):
        with self.assertRaises(PlazoMayorPermitido):
            desembolso_mensual(150_000_000, 0.30, 0.012, 300)


if __name__ == "__main__":
    unittest.main()
