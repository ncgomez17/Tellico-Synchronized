from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QFileDialog, QAction, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.uic.properties import QtWidgets

from Capa_presentacion.anhadir import Ui_Ventana_Anhadir
from Capa_presentacion.ventana_ui import *
import sys
import recursos
from capa_acceso_datos.Libro import Libro
from capa_acceso_datos.Extraccion import extraer_zip


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Clase para relacionar las funciones de la capas inferiores con los elementos de la interfaz"""
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.anhadir.clicked.connect(self.abrir)
        self.anhadir_sincronizaciones.triggered.connect(self.abrir)
        self.actualizar_tabla()
        # Conectamos los eventos con sus acciones
        #self.SeleccionarArchivo.clicked.connect(self.actualizar)


    def abrir(self):
        self.ventana= QtWidgets.QMainWindow()
        self.ui = Ui_Ventana_Anhadir()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def actualizar_tabla(self):
        self.tablaSincronizaciones.insertRow(self.tablaSincronizaciones.rowCount())
        btn_borrar = QPushButton('Borrar')
        btn_editar = QPushButton('Editar')
        btn_borrar.clicked.connect(self.elimnar_fila)
        dato1 = QTableWidgetItem("Servidor2")

        dato1.setFlags(QtCore.Qt.ItemIsEnabled)
        dato2 = QTableWidgetItem("Servidor2")
        dato2.setFlags(QtCore.Qt.ItemIsEnabled)
        dato3 = QTableWidgetItem("Servidor")
        dato3.setFlags(QtCore.Qt.ItemIsEnabled)
        dato4 = QTableWidgetItem("Servidor")
        dato4.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tablaSincronizaciones.setCellWidget(0,3,btn_borrar)
        self.tablaSincronizaciones.setItem(0, 1, dato1)
        self.tablaSincronizaciones.setItem(0, 0, dato2)
        self.tablaSincronizaciones.insertRow(self.tablaSincronizaciones.rowCount())
        self.tablaSincronizaciones.setItem(1, 1, dato3)
        self.tablaSincronizaciones.setItem(1, 0, dato4)

    def elimnar_fila(self):
        button = self.sender()
        if button:
            row = self.tablaSincronizaciones.indexAt(button.pos()).row()
            self.tablaSincronizaciones.removeRow(row)
'''
    def actualizar(self):
        file = QFileDialog.getOpenFileName(self, "Selecciona la coleccion", None, "Zip-files: *")
        extraer_zip(file[0])
        print("Datos extraidos correctamente",file[0])
'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
