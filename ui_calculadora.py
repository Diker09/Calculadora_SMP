# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 520)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout_principal = QVBoxLayout(self.centralwidget)
        self.layout_principal.setSpacing(14)
        self.layout_principal.setObjectName(u"layout_principal")
        self.layout_principal.setContentsMargins(16, 16, 16, 16)
        self.display_operaciones = QLineEdit(self.centralwidget)
        self.display_operaciones.setObjectName(u"display_operaciones")
        self.display_operaciones.setMinimumSize(QSize(0, 80))
        self.display_operaciones.setFocusPolicy(Qt.NoFocus)
        self.display_operaciones.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.display_operaciones.setReadOnly(True)

        self.layout_principal.addWidget(self.display_operaciones)

        self.grid_botonera = QGridLayout()
        self.grid_botonera.setSpacing(10)
        self.grid_botonera.setObjectName(u"grid_botonera")
        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_8, 0, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_division = QPushButton(self.centralwidget)
        self.btn_division.setObjectName(u"btn_division")
        sizePolicy.setHeightForWidth(self.btn_division.sizePolicy().hasHeightForWidth())
        self.btn_division.setSizePolicy(sizePolicy)
        self.btn_division.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_division, 0, 3, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_multiplicacion = QPushButton(self.centralwidget)
        self.btn_multiplicacion.setObjectName(u"btn_multiplicacion")
        sizePolicy.setHeightForWidth(self.btn_multiplicacion.sizePolicy().hasHeightForWidth())
        self.btn_multiplicacion.setSizePolicy(sizePolicy)
        self.btn_multiplicacion.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_multiplicacion, 1, 3, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_1, 2, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_2, 2, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_resta = QPushButton(self.centralwidget)
        self.btn_resta.setObjectName(u"btn_resta")
        sizePolicy.setHeightForWidth(self.btn_resta.sizePolicy().hasHeightForWidth())
        self.btn_resta.setSizePolicy(sizePolicy)
        self.btn_resta.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_resta, 2, 3, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_clear, 3, 0, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_0, 3, 1, 1, 1)

        self.btn_igual = QPushButton(self.centralwidget)
        self.btn_igual.setObjectName(u"btn_igual")
        sizePolicy.setHeightForWidth(self.btn_igual.sizePolicy().hasHeightForWidth())
        self.btn_igual.setSizePolicy(sizePolicy)
        self.btn_igual.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_igual, 3, 2, 1, 1)

        self.btn_suma = QPushButton(self.centralwidget)
        self.btn_suma.setObjectName(u"btn_suma")
        sizePolicy.setHeightForWidth(self.btn_suma.sizePolicy().hasHeightForWidth())
        self.btn_suma.setSizePolicy(sizePolicy)
        self.btn_suma.setMinimumSize(QSize(70, 60))

        self.grid_botonera.addWidget(self.btn_suma, 3, 3, 1, 1)


        self.layout_principal.addLayout(self.grid_botonera)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora Mecatr\u00f3nica", None))
        self.display_operaciones.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_multiplicacion.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_resta.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_suma.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

