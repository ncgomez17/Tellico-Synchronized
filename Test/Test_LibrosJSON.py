#!/usr/bin/env python3
import unittest

from Capa_logica_negocio.LibrosJSON import LibrosJSON
from Capa_acceso_datos.Extraccion import extraer_zip, tratar_xml
from os import remove


class TestLibrosJSON(unittest.TestCase):

    def setUp(self):
        self.ruta = "Datasets/tellico"
        # La ruta pueda variar dependiendo del servidor web que se quiere usar
        self.url = "http://192.168.1.47/index/colecciones/sincronizacion/"
        # El token puede variar dependiendo del Servidor web y el usuario a probar en este caso es el token del
        # usuario admin
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.RCr9bzWVbSq9uNCROm0o8" \
                     "-h4SkoNdYyuaASS9JmlaBI"

    def test_lista_libros(self):
        extraer_zip(self.ruta)
        l1 = tratar_xml()
        json = LibrosJSON(l1)
        remove("tellico.xml")
        self.assertIsNotNone(json)

    def test_objeto_no_validos(self):
        try:
            json = LibrosJSON("no soy un libro")
            self.assertIsInstance(json, Exception)
        except Exception as exc:
            print("Excepcion en pruebas " + str(exc))

    def test_lista_vacia(self):
        try:
            json = LibrosJSON(list())
            self.assertIsInstance(json, Exception)
        except Exception as exc:
            print("Excepcion en pruebas " + str(exc))

    def test_transform_valido(self):
        extraer_zip(self.ruta)
        l1 = tratar_xml()
        json = LibrosJSON(l1)
        remove("tellico.xml")
        message = json.transform(self.token)
        self.assertIn(self.token, message)

    def test_transform_no_valido(self):
        extraer_zip(self.ruta)
        l1 = tratar_xml()
        json = LibrosJSON(l1)
        remove("tellico.xml")
        message = json.transform("hola")
        self.assertIn("hola", message)

    def test_peticion_valida(self):
        extraer_zip(self.ruta)
        l1 = tratar_xml()
        json = LibrosJSON(l1)
        remove("tellico.xml")
        json.transform(self.token)
        response = json.enviar_URL(self.url)
        self.assertEqual(response[1], True)

    def test_peticion_no_valida(self):
        extraer_zip(self.ruta)
        l1 = tratar_xml()
        json = LibrosJSON(l1)
        remove("tellico.xml")
        json.transform(self.token)
        response = json.enviar_URL("url no existente")
        self.assertEqual(response, False)


if __name__ == "__main__":
    unittest.main()
