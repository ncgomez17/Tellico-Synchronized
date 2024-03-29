# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tellico/imagenes/tellico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(151, 165, 204);")
        MainWindow.setIconSize(QtCore.QSize(128, 128))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(350, 350))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.etiqueta1 = QtWidgets.QLabel(self.centralwidget)
        self.etiqueta1.setGeometry(QtCore.QRect(290, 0, 201, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.etiqueta1.sizePolicy().hasHeightForWidth())
        self.etiqueta1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.etiqueta1.setFont(font)
        self.etiqueta1.setStyleSheet("")
        self.etiqueta1.setWordWrap(False)
        self.etiqueta1.setObjectName("etiqueta1")
        self.etiqueta2 = QtWidgets.QLabel(self.centralwidget)
        self.etiqueta2.setGeometry(QtCore.QRect(300, 160, 191, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.etiqueta2.sizePolicy().hasHeightForWidth())
        self.etiqueta2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.etiqueta2.setFont(font)
        self.etiqueta2.setStyleSheet("")
        self.etiqueta2.setObjectName("etiqueta2")
        self.tellico = QtWidgets.QLabel(self.centralwidget)
        self.tellico.setGeometry(QtCore.QRect(320, 40, 131, 121))
        self.tellico.setStyleSheet("image: url(:/tellico/imagenes/tellico.png);")
        self.tellico.setText("")
        self.tellico.setObjectName("tellico")
        self.anhadir = QtWidgets.QPushButton(self.centralwidget)
        self.anhadir.setGeometry(QtCore.QRect(310, 480, 161, 41))
        self.anhadir.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.anhadir.setObjectName("anhadir")
        self.tablaSincronizaciones = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaSincronizaciones.setGeometry(QtCore.QRect(70, 190, 641, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablaSincronizaciones.sizePolicy().hasHeightForWidth())
        self.tablaSincronizaciones.setSizePolicy(sizePolicy)
        self.tablaSincronizaciones.setAutoFillBackground(False)
        self.tablaSincronizaciones.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tablaSincronizaciones.setObjectName("tablaSincronizaciones")
        self.tablaSincronizaciones.setColumnCount(5)
        self.tablaSincronizaciones.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSincronizaciones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSincronizaciones.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSincronizaciones.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSincronizaciones.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaSincronizaciones.setHorizontalHeaderItem(4, item)
        self.tablaSincronizaciones.raise_()
        self.etiqueta1.raise_()
        self.etiqueta2.raise_()
        self.tellico.raise_()
        self.anhadir.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.editar_sincronizaciones = QtWidgets.QAction(MainWindow)
        self.editar_sincronizaciones.setObjectName("editar_sincronizaciones")
        self.anhadir_sincronizaciones = QtWidgets.QAction(MainWindow)
        self.anhadir_sincronizaciones.setObjectName("anhadir_sincronizaciones")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tellico-Synchronized"))
        self.centralwidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>Tellico_Synchronized</p><p><br/></p></body></html>"))
        self.centralwidget.setWhatsThis(_translate("MainWindow", "adsasdasd"))
        self.etiqueta1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.etiqueta1.setText(_translate("MainWindow", "Tellico-Synchronized"))
        self.etiqueta2.setText(_translate("MainWindow", "Sincronizaciones activas"))
        self.anhadir.setText(_translate("MainWindow", "Añadir Sincronización"))
        item = self.tablaSincronizaciones.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ruta_archivo"))
        item = self.tablaSincronizaciones.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Servidor"))
        item = self.tablaSincronizaciones.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tiempo"))
        item = self.tablaSincronizaciones.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Borrar"))
        item = self.tablaSincronizaciones.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Editar"))
        self.editar_sincronizaciones.setText(_translate("MainWindow", "Editar/Borrar sincronizaciones"))
        self.editar_sincronizaciones.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.anhadir_sincronizaciones.setText(_translate("MainWindow", "Añadir sincronización"))
        self.anhadir_sincronizaciones.setShortcut(_translate("MainWindow", "Ctrl+A"))
