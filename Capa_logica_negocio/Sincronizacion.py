#!/usr/bin/env python3
import stat
import sys
from getpass import getuser
from os import chmod
from os import remove

usuario = getuser()
sys.path.append(__file__.replace("Capa_logica_negocio/Sincronizacion.py",""))
chmod(__file__, stat.S_IRWXU)
from Capa_logica_negocio.LibrosJSON import LibrosJSON
from Capa_acceso_datos.Extraccion import extraer_zip, tratar_xml


def establecer_sincronizacion(ruta, token, servidor):
    """Funcion que sera sincronizada por archivos_cron,envia los datos al servidor"""
    try:
        extraer_zip(ruta)
        l1 = tratar_xml()
        json = LibrosJSON(l1)
        print(json.transform(token))
        remove("tellico.xml")
        return json.enviar_URL(servidor)
    except Exception:
        return False


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("No se estan pasando los parametros necesarios:url del archivo, url del servidor y token del usuario")
    else:
        establecer_sincronizacion(sys.argv[1], sys.argv[2], sys.argv[3])
