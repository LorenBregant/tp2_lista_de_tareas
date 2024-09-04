# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tareas.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QWidget)

class Ui_ListaDeTareas(object):
    def setupUi(self, ListaDeTareas):
        if not ListaDeTareas.objectName():
            ListaDeTareas.setObjectName(u"ListaDeTareas")
        ListaDeTareas.resize(377, 359)
        self.btnEliminarCompletadas = QPushButton(ListaDeTareas)
        self.btnEliminarCompletadas.setObjectName(u"btnEliminarCompletadas")
        self.btnEliminarCompletadas.setGeometry(QRect(130, 326, 228, 23))
        self.labelDescrpcion = QLabel(ListaDeTareas)
        self.labelDescrpcion.setObjectName(u"labelDescrpcion")
        self.labelDescrpcion.setGeometry(QRect(9, 10, 115, 22))
        self.btnAgregar = QPushButton(ListaDeTareas)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setGeometry(QRect(130, 38, 228, 23))
        self.ListaTareas = QListView(ListaDeTareas)
        self.ListaTareas.setObjectName(u"ListaTareas")
        self.ListaTareas.setGeometry(QRect(9, 67, 349, 221))
        self.btnEliminar = QPushButton(ListaDeTareas)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(130, 297, 228, 23))
        self.inputDescripcion = QLineEdit(ListaDeTareas)
        self.inputDescripcion.setObjectName(u"inputDescripcion")
        self.inputDescripcion.setGeometry(QRect(130, 10, 228, 22))

        self.retranslateUi(ListaDeTareas)

        QMetaObject.connectSlotsByName(ListaDeTareas)
    # setupUi

    def retranslateUi(self, ListaDeTareas):
        ListaDeTareas.setWindowTitle(QCoreApplication.translate("ListaDeTareas", u"Lista de Tareas", None))
        self.btnEliminarCompletadas.setText(QCoreApplication.translate("ListaDeTareas", u"Eliminar tareas completadas", None))
        self.labelDescrpcion.setText(QCoreApplication.translate("ListaDeTareas", u"Ingrese nueva tarea", None))
        self.btnAgregar.setText(QCoreApplication.translate("ListaDeTareas", u"Agregar tarea", None))
        self.btnEliminar.setText(QCoreApplication.translate("ListaDeTareas", u"Eliminar tarea", None))
    # retranslateUi

