from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QFileDialog, QAction, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.uic.properties import QtWidgets

from Capa_presentacion.anhadir import Ui_Ventana_Anhadir
from Capa_presentacion.ventana_ui import *
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
        # Conectamos los eventos con sus acciones
        # self.SeleccionarArchivo.clicked.connect(self.actualizar)

    def abrir(self):
        """Funcion que se encargara de abrir la ventana de añadir"""
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Ventana_Anhadir()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def actualizar_tabla(self):
        """Funcion a la que se llamara cada vez que se realice algun cambio para actualizar los datos"""
        self.tablaSincronizaciones.insertRow(self.tablaSincronizaciones.rowCount())

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
        self.ajustar_tabla()

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
        self.tablaSincronizaciones.setColumnWidth(2, 80)
        self.tablaSincronizaciones.setColumnWidth(3, 80)
        self.tablaSincronizaciones.setColumnWidth(4, 40)

        header = self.tablaSincronizaciones.horizontalHeader()
        header.setStretchLastSection(True)

    def elimnar_fila(self):
        """Funcion para eliminar la fila que esta seleccionada en ese momento"""
        button = self.sender()
        if button:
            row = self.tablaSincronizaciones.indexAt(button.pos()).row()
            contenido = self.tablaSincronizaciones.item(row,0).text()
            Archivo_crontab.eliminar_sincronizacion(contenido)
            self.tablaSincronizaciones.removeRow(row)

    def editar_fila(self):
        """Funcion que mostrara el formulario para poder editar los datos de la respectiva sincronizacion"""
        button = self.sender()
        if button:
            row = self.tablaSincronizaciones.indexAt(button.pos()).row()
            contenido = self.tablaSincronizaciones.item(row,0).text()
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_Ventana_Anhadir()
            self.ui.setupUi(self.ventana)
            self.ventana.show()

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
