#!/usr/bin/env python3
from zipfile import ZipFile
from xml.dom import minidom, DOMException
from capa_acceso_datos.Libro import Libro

##Funcion para extraer todos los archivos a partir de la ruta del zip

def extraer_zip(ruta):
    """Funcion para extraer la informacion del fichero zip indicado en la ruta"""
    with ZipFile(ruta, 'r')as zip:
        # printing all the contents of the zip file
        zip.printdir()
        # extracting all the files
        print('Extracting all the files now...')
        archivo = zip.extract("tellico.xml")
        return archivo
        print('Done!')





def tratar_xml():
    """Funcion que se encargara de sacar la informacion que nos es relevante de cada libro de la coleccion
        Devuelve una lista de objetos Libro con la informacion ya guardada en estos"""
    try:
        doc = minidom.parse("tellico.xml")
        list = []
        libros = doc.getElementsByTagName("entry")
        for libro in libros:
            #creamos el objeto libro donde almacenamos los datos
            l = Libro()
            #cogemos los elementos que nos interesan
            title = libro.getElementsByTagName("title")
            autores = libro.getElementsByTagName("authors")
            publisher = libro.getElementsByTagName("publisher")
            anho_pub = libro.getElementsByTagName("pub_year")
            isbn = libro.getElementsByTagName("isbn")
            pages = libro.getElementsByTagName("pages")
            lang = libro.getElementsByTagName("language")
            comments = libro.getElementsByTagName("comments")
            #Comprobamos si los elementos estan vacios, sino los añadimos al objeto libro
            if title.length != 0:
                l.titulo = title[0].firstChild.data

            if autores.length != 0:
                for autor in autores:
                    a = autor.getElementsByTagName("author")
                    l.añadir_autor(a[0].firstChild.data)

            if publisher.length != 0:
                l.publisher = publisher[0].firstChild.data

            if anho_pub.length != 0:
                l.anho_pub = anho_pub[0].firstChild.data

            if isbn.length != 0:
                l.isbn = isbn[0].firstChild.data

            if pages.length != 0:
                l.pages = pages[0].firstChild.data

            if lang.length != 0:
                l.lang = lang[0].firstChild.data

            if comments.length != 0:
                l.comments = comments[0].firstChild.data

            list.append(l)
    except DOMException:
        print("Error en el parseo de datos XML")

    return list

