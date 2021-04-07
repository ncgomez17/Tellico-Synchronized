#!/usr/bin/env python3
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QFileDialog, QAction, QTableWidgetItem, QPushButton, QScrollBar, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.uic.properties import QtWidgets
import sys
sys.path.append("..")
from Capa_logica_negocio.Archivo_crontab import anhadir_sincronizacion, editar_sincronizacion
from Capa_presentacion.anhadir import Ui_Ventana_Anhadir
from Capa_presentacion.ventana_ui import *
from Capa_presentacion.editar import Ui_Ventana_Editar
from Capa_logica_negocio import Archivo_crontab
import sys
import recursos


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Clase para relacionar las funciones de la capas inferiores con los elementos de la interfaz"""

    def __init__(self, *args, **kwargs):
        """Constructor que se encargara de inicializar los componentes principales"""
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.anhadir.clicked.connect(self.abrir)
        self.anhadir_sincronizaciones.triggered.connect(self.abrir)
        self.actualizar_tabla()
        self.ruta = None
        self.contenido = None
        # Conectamos los eventos con sus acciones
        # self.SeleccionarArchivo.clicked.connect(self.actualizar)

    def abrir(self):
        """Funcion que se encargara de abrir la ventana de añadir"""
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Ventana_Anhadir()
        self.ui.setupUi(self.ventana)
        self.ui.anhadir_sincro.clicked.connect(self.anhadir_sincro)
        self.ui.SeleccionarArchivo.clicked.connect(self.seleccionar)
        self.ventana.show()

    def anhadir_sincro(self):
        try:
            button = self.sender()
            if button:
                token = self.ui.token.toPlainText()
                servidor = self.ui.servidor.toPlainText()
                min = self.ui.min.text()
                horas = self.ui.horas.text()
                dias = self.ui.dias.text()
                meses = self.ui.meses.text()

                if token and servidor and self.ruta:
                    correcto = anhadir_sincronizacion(self.ruta, token, servidor, min, horas, dias, meses)
                    if correcto[0] is False:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("No se ha podido establecer la sincronizacion")
                        msg.setInformativeText(correcto[1])
                        msg.setWindowTitle("Fallo en la sincronizacion")
                        msg.exec_()
                        self.ruta = None
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Se ha establecido la sincronizacion correctamente")
                        msg.setInformativeText(correcto[1])
                        msg.setWindowTitle("Sincronizacion establecida")
                        msg.exec_()
                        self.ruta = None
                        self.ventana.close()
                        self.actualizar_tabla()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("No se ha podido establecer la sincronizacion")
                    msg.setInformativeText("Faltan campos por completar")
                    msg.setWindowTitle("Warning")
                    msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Sincronizacion no valida")
            msg.setInformativeText('Esto puede ser debido a que algun argumento que has introducido no es correcto o '
                                   'no se puede acceder a el')
            msg.setWindowTitle("Error")
            msg.exec_()
            return None

    def actualizar_tabla(self):
        """Funcion a la que se llamara cada vez que se realice algun cambio para actualizar los datos"""
        self.ajustar_tabla()
        sincronizaciones = Archivo_crontab.listar_sincronizaciones()
        self.tablaSincronizaciones.setRowCount(len(sincronizaciones))
        row = 0
        for i in sincronizaciones:
            (btn_borrar, btn_editar) = self.crear_botones_fila()
            ruta_archivo = QTableWidgetItem(i[0])
            servidor = QTableWidgetItem(i[2])
            tiempo = QTableWidgetItem('   ' + i[3] + ' ' + i[4] + ' ' + i[5] + ' ' + i[6])
            self.tablaSincronizaciones.setItem(row, 0, ruta_archivo)
            self.tablaSincronizaciones.setItem(row, 1, servidor)
            self.tablaSincronizaciones.setItem(row, 2, tiempo)
            self.tablaSincronizaciones.setCellWidget(row, 3, btn_borrar)
            self.tablaSincronizaciones.setCellWidget(row, 4, btn_editar)
            row += 1

        self.tablaSincronizaciones.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tablaSincronizaciones.resizeRowsToContents()

    def crear_botones_fila(self):
        """Funcion para crear los botones de la tabla"""
        btn_borrar = QPushButton()
        btn_editar = QPushButton()
        btn_borrar.clicked.connect(self.elimnar_fila)
        btn_borrar.setIcon(QtGui.QIcon('imagenes/borrar.png'))
        btn_borrar.setIconSize(QtCore.QSize(30, 30))
        btn_borrar.setAutoFillBackground(True)
        pal = QPalette()
        btn_borrar.setPalette(pal)
        btn_borrar.setStyleSheet("QPushButton::hover"
                                 "{"
                                 "background-color : red;"
                                 "}")
        btn_editar.clicked.connect(self.editar_fila)
        btn_editar.setIcon(QtGui.QIcon('imagenes/editar.png'))
        btn_editar.setIconSize(QtCore.QSize(30, 30))
        btn_borrar.setAutoFillBackground(True)
        pal2 = QPalette()
        btn_editar.setPalette(pal2)
        btn_editar.setStyleSheet("QPushButton::hover"
                                 "{"
                                 "background-color : blue;"
                                 "}")

        return btn_borrar, btn_editar

    def ajustar_tabla(self):
        """Funcion para ajustar los elementos de la tabla"""
        self.tablaSincronizaciones.setColumnWidth(0, 200)
        self.tablaSincronizaciones.setColumnWidth(1, 200)
        self.tablaSincronizaciones.setColumnWidth(2, 90)
        self.tablaSincronizaciones.setColumnWidth(3, 70)
        self.tablaSincronizaciones.setColumnWidth(4, 40)

        header = self.tablaSincronizaciones.horizontalHeader()
        self.tablaSincronizaciones.setHorizontalScrollBarPolicy(True)
        header.setStretchLastSection(True)

    def elimnar_fila(self):
        """Funcion para eliminar la fila que esta seleccionada en ese momento"""
        button = self.sender()
        if button:
            row = self.tablaSincronizaciones.indexAt(button.pos()).row()
            contenido = self.tablaSincronizaciones.item(row, 0).text()
            Archivo_crontab.eliminar_sincronizacion(contenido)
            self.tablaSincronizaciones.removeRow(row)

    def editar_fila(self):
        """Funcion que mostrara el formulario para poder editar los datos de la respectiva sincronizacion"""
        button = self.sender()
        if button:
            row = self.tablaSincronizaciones.indexAt(button.pos()).row()
            self.contenido = self.tablaSincronizaciones.item(row, 0).text()
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_Ventana_Editar()
            self.ui.setupUi(self.ventana)
            self.ui.editar.clicked.connect(self.editar_sincro)
            self.ventana.show()

    def editar_sincro(self):
            button = self.sender()
            if button:
                min = self.ui.editar_min.text()
                horas = self.ui.editar_horas.text()
                meses = self.ui.editar_meses.text()
                dias = self.ui.editar_dias.text()

                if min and horas and meses and dias:
                    editar_sincronizacion(self.contenido, min, horas, dias, meses)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Edicion de Sincronizacion")
                    msg.setInformativeText("Sincronizacion editada correctamente")
                    msg.setWindowTitle("Sincronizacion modificada")
                    msg.exec_()
                    self.actualizar_tabla()
                    self.contenido = None
                    self.ventana.close()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Datos incorrectos para editar")
                    msg.setInformativeText("Asegurate de que los datos introducidos son correctos")
                    msg.setWindowTitle("Fallo en editar Sincronizacion")
                    msg.exec_()
                    self.ruta = None
                    self.ventana.close()
                    self.actualizar_tabla()


    def seleccionar(self):
        """Funcion para seleccionar la ruta del archivo"""
        try:
            button = self.sender()
            if button:
                file = QFileDialog.getOpenFileName(None, "Selecciona la coleccion", "/home/", "Zip-files: *")
                print("Ruta seleccionada: ", file[0])
                self.ruta = file[0]
                return file
        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ruta de archivo no valida")
            msg.setInformativeText('Esto puede ser debido a que se ha introducido una ruta de una archivo no valido o '
                                   'no se ha indicado ninguna ruta')
            msg.setWindowTitle("Error")
            msg.exec_()
            return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
