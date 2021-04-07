#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editar.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana_Editar(object):
    def setupUi(self, Ventana_Editar):
        Ventana_Editar.setObjectName("Ventana_Editar")
        Ventana_Editar.resize(500, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ventana_Editar.sizePolicy().hasHeightForWidth())
        Ventana_Editar.setSizePolicy(sizePolicy)
        Ventana_Editar.setMinimumSize(QtCore.QSize(500, 200))
        Ventana_Editar.setMaximumSize(QtCore.QSize(500, 200))
        Ventana_Editar.setStyleSheet("\n"
"background-color: rgb(151, 165, 204);")
        self.centralwidget = QtWidgets.QWidget(Ventana_Editar)
        self.centralwidget.setObjectName("centralwidget")
        self.editar_min = QtWidgets.QSpinBox(self.centralwidget)
        self.editar_min.setGeometry(QtCore.QRect(80, 40, 47, 24))
        self.editar_min.setMaximum(59)
        self.editar_min.setObjectName("editar_min")
        self.editar_horas = QtWidgets.QSpinBox(self.centralwidget)
        self.editar_horas.setGeometry(QtCore.QRect(180, 40, 47, 24))
        self.editar_horas.setMaximum(23)
        self.editar_horas.setObjectName("editar_horas")
        self.editar_dias = QtWidgets.QSpinBox(self.centralwidget)
        self.editar_dias.setGeometry(QtCore.QRect(280, 40, 47, 24))
        self.editar_dias.setMaximum(31)
        self.editar_dias.setObjectName("editar_dias")
        self.editar_meses = QtWidgets.QSpinBox(self.centralwidget)
        self.editar_meses.setGeometry(QtCore.QRect(370, 40, 47, 24))
        self.editar_meses.setMaximum(12)
        self.editar_meses.setObjectName("editar_meses")
        self.edit_min = QtWidgets.QLabel(self.centralwidget)
        self.edit_min.setGeometry(QtCore.QRect(80, 70, 59, 15))
        self.edit_min.setObjectName("edit_min")
        self.edit_dias = QtWidgets.QLabel(self.centralwidget)
        self.edit_dias.setGeometry(QtCore.QRect(280, 70, 59, 15))
        self.edit_dias.setObjectName("edit_dias")
        self.edit_horas = QtWidgets.QLabel(self.centralwidget)
        self.edit_horas.setGeometry(QtCore.QRect(180, 70, 59, 15))
        self.edit_horas.setObjectName("edit_horas")
        self.edit_meses = QtWidgets.QLabel(self.centralwidget)
        self.edit_meses.setGeometry(QtCore.QRect(370, 70, 59, 15))
        self.edit_meses.setObjectName("edit_meses")
        self.editar = QtWidgets.QPushButton(self.centralwidget)
        self.editar.setGeometry(QtCore.QRect(190, 120, 111, 31))
        self.editar.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.editar.setObjectName("editar")
        Ventana_Editar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_Editar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 20))
        self.menubar.setObjectName("menubar")
        Ventana_Editar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_Editar)
        self.statusbar.setObjectName("statusbar")
        Ventana_Editar.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Editar)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Editar)

    def retranslateUi(self, Ventana_Editar):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Editar.setWindowTitle(_translate("Ventana_Editar", "Tellico-Synchronized"))
        self.edit_min.setText(_translate("Ventana_Editar", "minutos"))
        self.edit_dias.setText(_translate("Ventana_Editar", "días"))
        self.edit_horas.setText(_translate("Ventana_Editar", "horas"))
        self.edit_meses.setText(_translate("Ventana_Editar", "meses"))
        self.editar.setText(_translate("Ventana_Editar", "Editar"))
