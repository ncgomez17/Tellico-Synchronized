#!/usr/bin/env python3
from crontab import CronTab
from getpass import getuser
import os
import re
from Capa_logica_negocio.Sincronizacion import establecer_sincronizacion


def anhadir_sincronizacion(ruta, token, ServidorWeb, min, horas, dias, meses):
    """ Function para añadir una sincronizacion a partir de la ruta del archivo,token y url del Servidor cada x
    tiempo. """
    usuario = getuser()
    wd = os.getcwd()
    wd = ' python3 ' + wd + '/Sincronizacion.py' + ' ' + ruta + ' ' + token + ' ' + ServidorWeb
    my_cron = CronTab(user=usuario)
    exists = list(my_cron.find_comment(ruta))
    if exists.__len__() == 0:
        job = my_cron.new(command=wd, comment=ruta)
        if str(meses) == "0":
            meses = "*"
        if str(dias) == "0":
            dias = "*"
        job.setall(str(min) + " " + str(horas) + " " + str(dias) + " " + str(meses) + " " + "*")
        if job.is_valid() and establecer_sincronizacion(ruta, token, ServidorWeb):
            my_cron.write()
            return True
        else:
            print("La sincronizacion no es correcta")
            return False
    else:
        print("Ese archivo ya se esta sincronizando")
        return False


def eliminar_sincronizacion(ruta):
    """Elimina la synchronization de un determinado archivo(el nombre de la sincronizacion sera la ruta del archivo)"""
    usuario = getuser()
    existe = False
    my_cron = CronTab(user=usuario)
    for job in my_cron:
        if job.comment == ruta:
            my_cron.remove(job)
            my_cron.write()
            existe = True

    return existe


def listar_sincronizaciones():
    """Encontrara todas las sincronziaciones crontab del usuario y devolvera una lista con estas,
    la lista devolvera elementos de las sincronizaciones con info sobre: localizacion del archivo,token,Servidor y tiempos"""
    lista = []
    usuario = getuser()
    my_cron = CronTab(user=usuario)
    for job in my_cron:
        minutos = str(job.minute)
        horas = str(job.hour)
        dias = str(job.day)
        meses = str(job.month)
        datos_sincro = re.split(" ", job.command)
        datos_sincro.remove(datos_sincro[0])
        datos_sincro.remove(datos_sincro[0])
        datos_sincro.append(minutos)
        datos_sincro.append(horas)
        datos_sincro.append(meses)
        datos_sincro.append(dias)
        lista.append(datos_sincro)
    return lista


def editar_sincronizacion(ruta_archivo, minutos, horas, dias, meses):
    """Funcion que se encargara de editar el tiempo de una sincronizacion pasandole la ruta del archivo que se esta
    sincronizando """
    usuario = getuser()
    my_cron = CronTab(user=usuario)
    for job in my_cron:
        if job.comment == ruta_archivo:
            if str(meses) == "0":
                meses = "*"
            if str(dias) == "0":
                dias = "*"
            job.setall(str(minutos) + " " + str(horas) + " " + str(dias) + " " + str(meses) + " " + "*")
            if job.is_valid():
                my_cron.write()
                print("Archivo crontab modificado correctamente")
                return True


if __name__ == "__main__":
    ruta = "/home/ncgomez17/Documentos/asdsad"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.RCr9bzWVbSq9uNCROm0o8-h4SkoNdYyuaASS9JmlaBI"
    ServidorWeb = 'http://192.168.1.47/index/colecciones/sincronizacion/'
    anhadir_sincronizacion(ruta, token, ServidorWeb, 5, 0, 0, 12)
    editar_sincronizacion(ruta, 5, 0, 0, 12)
    print(listar_sincronizaciones())
