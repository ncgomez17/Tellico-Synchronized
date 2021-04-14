#!/usr/bin/env python3
import unittest
import Archivo_crontab


class TestArchivo_crontab(unittest.TestCase):


    def test_anhadir(self):
        Archivo_crontab.anhadir_sincronizacion()

    def test_anhadir_error_datos(self):
        pass

    def test_anhadir_sincronizacionExistente(self):
        pass

    def test_eliminar(self):
        pass

    def test_eliminar_error(self):
        pass

    def test_listar(self):
        pass

    def test_listavacia(self):
        pass

    def test_editar(self):
        pass

    def test_editar_error_datos(self):
        pass




if __name__ == "__main__":
    unittest.main()