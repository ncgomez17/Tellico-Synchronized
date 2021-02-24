#!/usr/bin/env python3
import sys
from capa_acceso_datos.Libro import Libro
import json
import requests
from urllib.parse import urlparse


class LibrosJSON:
    """Funcion que transforma los objetos libro en formato json y los permite enviar a una direccion"""
    def __init__(self, Libros):
        if len(Libros) == 0:
            raise Exception("La lista de libros esta vacía")
        if type(Libros) != list:
            raise TypeError("Tiene que pasarse una lista de libros")
        if type(Libros[0]) != Libro:
            raise TypeError("Tiene que pasarse una lista de libros")
        self.__libros = Libros
        self.__mensage = None

    # Transforma la coleccion de entrada a un mensaje JSON

    def transform(self, token):
        """Funcion que transforma el libro en json junto a un token que se le pasa"""
        serialize = json.dumps(self.__libros, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)
        objeto = json.loads(serialize)
        tokenfinal = {"token": token}
        objeto.append(tokenfinal)
        serializefinal = json.dumps(objeto, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)
        self.__mensage = serializefinal
        return self.__mensage

    def transform_sintoken(self):
        """Funcion que transforma el libro en json """
        serialize = json.dumps(self.__libros, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)
        self.__mensage = serialize
        return self.__mensage


    def peticionUrl(self, url):
        """Funcion que envia los datos a una determinada url"""
        parsed_url = urlparse(url)
        if bool(parsed_url.scheme):
            response = requests.post(url, json=self.__mensage)
            if response:
                return response.text
            else:
                print("Respuesta fallida")
                return False
        else:
            return False
