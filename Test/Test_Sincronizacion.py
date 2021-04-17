#!/usr/bin/env python3
import unittest

from Capa_logica_negocio.Sincronizacion import establecer_sincronizacion


class TestSincronizacion(unittest.TestCase):

    def setUp(self):
        self.ruta = "Datasets/tellico"
        # La ruta pueda variar dependiendo del servidor web que se quiere usar
        self.url = "http://192.168.1.47/index/colecciones/sincronizacion/"
        # El token puede variar dependiendo del Servidor web y el usuario a probar en este caso es el token del
        # usuario admin
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.RCr9bzWVbSq9uNCROm0o8" \
                     "-h4SkoNdYyuaASS9JmlaBI"

    def test_establecer_sincro(self):
        result = establecer_sincronizacion(self.ruta, self.token, self.url)
        self.assertEqual(result[1], True)

    def test_establecer_sincro_errorRuta(self):
        result = establecer_sincronizacion("mal", self.token, self.url)
        self.assertEqual(result, False)

    def test_establecer_sincro_errorUrl(self):
        result = establecer_sincronizacion(self.ruta, self.token, "no existe")
        self.assertEqual(result, False)

    def test_establecer_sincro_errorToken(self):
        result = establecer_sincronizacion(self.ruta, "hola", self.url)
        self.assertEqual(result[0], "El token no es válido o tiene algun dato incorrecto")


if __name__ == "__main__":
    unittest.main()
