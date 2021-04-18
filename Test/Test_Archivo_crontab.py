#!/usr/bin/env python3
import unittest
from getpass import getuser
from crontab import CronTab
from Capa_logica_negocio.Archivo_crontab import anhadir_sincronizacion, eliminar_sincronizacion, \
    listar_sincronizaciones, editar_sincronizacion


class TestArchivo_crontab(unittest.TestCase):

    def setUp(self):
        self.ruta = "Datasets/tellico"
        # La ruta pueda variar dependiendo del servidor web que se quiere usar
        self.url = "http://192.168.1.47/index/colecciones/sincronizacion/"
        # El token puede variar dependiendo del Servidor web y el usuario a probar en este caso es el token del
        # usuario admin
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.RCr9bzWVbSq9uNCROm0o8" \
                     "-h4SkoNdYyuaASS9JmlaBI "
        self.min = 5
        self.horas = 1
        self.dias = 1
        self.meses = 1

        usuario = getuser()
        my_cron = CronTab(user=usuario)
        my_cron.remove_all()

    def test_anhadir(self):
        result = anhadir_sincronizacion(self.ruta, self.token, self.url, self.min, self.horas, self.dias, self.meses)
        self.assertEqual(result[0], True)
        usuario = getuser()
        my_cron = CronTab(user=usuario)
        my_cron.remove_all()

    def test_anhadir_error_datos(self):
        result = anhadir_sincronizacion("DatasetsNone", self.token, self.url, self.min, self.horas, self.dias,
                                        self.meses)
        self.assertEqual(result[0], False)
        usuario = getuser()
        my_cron = CronTab(user=usuario)
        my_cron.remove_all()

    def test_anhadir_sincronizacionExistente(self):
        anhadir_sincronizacion(self.ruta, self.token, self.url, self.min, self.horas, self.dias, self.meses)
        result = anhadir_sincronizacion(self.ruta, self.token, self.url, self.min, self.horas, self.dias, self.meses)
        self.assertEqual(result[0], False)
        usuario = getuser()
        my_cron = CronTab(user=usuario)
        my_cron.remove_all()

    def test_anhadir_comprobar_tiempo(self):
        result = anhadir_sincronizacion(self.ruta, self.token, self.url, self.min, self.horas, self.dias, self.meses)
        usuario = getuser()
        my_cron = CronTab(user=usuario)
        for job in my_cron:
            if job.comment == self.ruta:
                self.assertEqual(job.minute, self.min)
                self.assertEqual(job.hour, self.horas)
                self.assertEqual(job.day, self.dias)
                self.assertEqual(job.month, self.meses)
        self.assertEqual(result[0], True)
        usuario = getuser()
        my_cron = CronTab(user=usuario)
        my_cron.remove_all()

    def test_eliminar(self):
        anhadir_sincronizacion(self.ruta, self.token, self.url, self.min, self.horas, self.dias, self.meses)
        result = eliminar_sincronizacion(self.ruta)
        self.assertEqual(result, True)

    def test_eliminar_error(self):
        result = eliminar_sincronizacion(self.ruta)
        self.assertEqual(result, False)

    def test_listar(self):
        anhadir_sincronizacion(self.ruta, self.token, self.url, self.min, self.horas, self.dias, self.meses)
        anhadir_sincronizacion("Datasets/tellico2", self.token, self.url, self.min, self.horas, self.dias, self.meses)
        result = listar_sincronizaciones()
        self.assertEqual(len(result), 2)
        usuario = getuser()
        my_cron = CronTab(user=usuario)
        my_cron.remove_all()

    def test_listavacia(self):
        result = listar_sincronizaciones()
        self.assertEqual(len(result), 0)

    def test_editar(self):
        anhadir_sincronizacion(self.ruta, self.token, self.url, self.min, self.horas, self.dias, self.meses)
        result = editar_sincronizacion(self.ruta, 1, 1, 1, 1)
        self.assertEqual(result, True)
        usuario = getuser()
        my_cron = CronTab(user=usuario)
        my_cron.remove_all()

    def test_editar_error(self):
        anhadir_sincronizacion(self.ruta, self.token, self.url, self.min, self.horas, self.dias, self.meses)
        result = editar_sincronizacion("Datasets/tellico2", 1, 1, 1, 1)
        self.assertEqual(result, False)
        usuario = getuser()
        my_cron = CronTab(user=usuario)
        my_cron.remove_all()


if __name__ == "__main__":
    unittest.main()
