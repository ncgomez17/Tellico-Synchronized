#!/usr/bin/env python3
import sys
from getpass import getuser
from os import remove

usuario = getuser()
sys.path.append('/home/' + usuario + '/PycharmProjects/pythonProject/')
from Capa_logica_negocio.LibrosJSON import LibrosJSON
from capa_acceso_datos.Extraccion import extraer_zip, tratar_xml


def establecer_sincronizacion(ruta, token, servidor):
    """Funcion que sera sincronizada por archivos_cron,envia los datos al servidor"""
    try:
        extraer_zip(ruta)
        l1 = tratar_xml()
        json = LibrosJSON(l1)
        print(json.transform(token))
        remove("tellico.xml")
        return json.peticionUrl(servidor)
    except Exception:
        return False


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("No se estan pasando los parametros necesarios:url del archivo, url del servidor y token del usuario")
    else:
        establecer_sincronizacion(sys.argv[1], sys.argv[2], sys.argv[3])
