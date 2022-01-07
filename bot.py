from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QHeaderView, QMessageBox
from PyQt5.QtGui import *

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

import traceback
import time
import xml.etree.ElementTree as ET
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(660, 600)
        MainWindow.setMinimumSize(QtCore.QSize(650, 575))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./lib/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_by = QtWidgets.QLabel(self.centralwidget)
        self.label_by.setGeometry(QtCore.QRect(430, 0, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_by.setFont(font)
        self.label_by.setObjectName("label_by")
        self.itemFrame = QtWidgets.QFrame(self.centralwidget)
        self.itemFrame.setGeometry(QtCore.QRect(0, 20, 651, 291))
        self.itemFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.itemFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.itemFrame.setObjectName("itemFrame")
        self.itemGroup = QtWidgets.QGroupBox(self.itemFrame)
        self.itemGroup.setGeometry(QtCore.QRect(10, 0, 221, 281))
        self.itemGroup.setObjectName("itemGroup")
        self.keyLab = QtWidgets.QLabel(self.itemGroup)
        self.keyLab.setGeometry(QtCore.QRect(10, 140, 68, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.keyLab.setFont(font)
        self.keyLab.setObjectName("keyLab")
        self.ocolorLine = QtWidgets.QLineEdit(self.itemGroup)
        self.ocolorLine.setEnabled(False)
        self.ocolorLine.setGeometry(QtCore.QRect(70, 110, 145, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ocolorLine.setFont(font)
        self.ocolorLine.setText("")
        self.ocolorLine.setObjectName("ocolorLine")
        self.sizeLab = QtWidgets.QLabel(self.itemGroup)
        self.sizeLab.setGeometry(QtCore.QRect(30, 50, 28, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sizeLab.setFont(font)
        self.sizeLab.setObjectName("sizeLab")
        self.keyLine = QtWidgets.QLineEdit(self.itemGroup)
        self.keyLine.setEnabled(True)
        self.keyLine.setGeometry(QtCore.QRect(70, 140, 145, 20))
        self.keyLine.setObjectName("keyLine")
        self.sizeCbox = QtWidgets.QComboBox(self.itemGroup)
        self.sizeCbox.setGeometry(QtCore.QRect(70, 50, 145, 20))
        self.sizeCbox.setAcceptDrops(True)
        self.sizeCbox.setObjectName("sizeCbox")
        self.sizeCbox.addItem("")
        self.sizeCbox.addItem("")
        self.sizeCbox.addItem("")
        self.sizeCbox.addItem("")
        self.addBut = QtWidgets.QPushButton(self.itemGroup)
        self.addBut.setGeometry(QtCore.QRect(70, 207, 145, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.addBut.setFont(font)
        self.addBut.setObjectName("addBut")
        self.catCbox = QtWidgets.QComboBox(self.itemGroup)
        self.catCbox.setGeometry(QtCore.QRect(70, 20, 145, 20))
        self.catCbox.setAcceptDrops(True)
        self.catCbox.setObjectName("catCbox")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.colorCombo = QtWidgets.QComboBox(self.itemGroup)
        self.colorCombo.setGeometry(QtCore.QRect(70, 80, 145, 20))
        self.colorCombo.setAcceptDrops(True)
        self.colorCombo.setObjectName("colorCombo")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.catLabel = QtWidgets.QLabel(self.itemGroup)
        self.catLabel.setGeometry(QtCore.QRect(10, 20, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.catLabel.setFont(font)
        self.catLabel.setObjectName("catLabel")
        self.colorLab = QtWidgets.QLabel(self.itemGroup)
        self.colorLab.setGeometry(QtCore.QRect(26, 80, 38, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.colorLab.setFont(font)
        self.colorLab.setObjectName("colorLab")
        self.deleteBut = QtWidgets.QPushButton(self.itemGroup)
        self.deleteBut.setGeometry(QtCore.QRect(70, 240, 145, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.deleteBut.setFont(font)
        self.deleteBut.setObjectName("deleteBut")
        self.tableWidget = QtWidgets.QTableWidget(self.itemFrame)
        self.tableWidget.setGeometry(QtCore.QRect(240, 10, 401, 275))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(401, 275))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setStyleSheet("background-image: url(./lib/bgi.png);")
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        ###### modified #####
        header = self.tableWidget.horizontalHeader()
        header.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
        header.setLineWidth(1)
        self.tableWidget.setHorizontalHeader(header)
        ###### modified ######
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.bilFrame = QtWidgets.QFrame(self.centralwidget)
        self.bilFrame.setEnabled(True)
        self.bilFrame.setGeometry(QtCore.QRect(0, 310, 351, 201))
        self.bilFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bilFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bilFrame.setObjectName("bilFrame")
        self.billGroup = QtWidgets.QGroupBox(self.bilFrame)
        self.billGroup.setGeometry(QtCore.QRect(10, 0, 341, 201))
        self.billGroup.setObjectName("billGroup")
        self.nameLine = QtWidgets.QLineEdit(self.billGroup)
        self.nameLine.setGeometry(QtCore.QRect(10, 20, 319, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nameLine.setFont(font)
        self.nameLine.setInputMask("")
        self.nameLine.setText("")
        self.nameLine.setObjectName("nameLine")
        self.emailLine = QtWidgets.QLineEdit(self.billGroup)
        self.emailLine.setGeometry(QtCore.QRect(10, 50, 319, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.emailLine.setFont(font)
        self.emailLine.setText("")
        self.emailLine.setObjectName("emailLine")
        self.numberLine = QtWidgets.QLineEdit(self.billGroup)
        self.numberLine.setGeometry(QtCore.QRect(10, 80, 319, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.numberLine.setFont(font)
        self.numberLine.setText("")
        self.numberLine.setObjectName("numberLine")
        self.numberLine.setValidator(QIntValidator())
        self.addressLine = QtWidgets.QLineEdit(self.billGroup)
        self.addressLine.setGeometry(QtCore.QRect(10, 110, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addressLine.setFont(font)
        self.addressLine.setText("")
        self.addressLine.setObjectName("addressLine")
        self.aptLine = QtWidgets.QLineEdit(self.billGroup)
        self.aptLine.setGeometry(QtCore.QRect(230, 110, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.aptLine.setFont(font)
        self.aptLine.setText("")
        self.aptLine.setObjectName("aptLine")
        self.zipLine = QtWidgets.QLineEdit(self.billGroup)
        self.zipLine.setGeometry(QtCore.QRect(10, 140, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.zipLine.setFont(font)
        self.zipLine.setText("")
        self.zipLine.setObjectName("zipLine")
        self.zipLine.setValidator(QIntValidator())
        self.cityLine = QtWidgets.QLineEdit(self.billGroup)
        self.cityLine.setGeometry(QtCore.QRect(70, 140, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cityLine.setFont(font)
        self.cityLine.setText("")
        self.cityLine.setObjectName("cityLine")
        self.countryCbox = QtWidgets.QComboBox(self.billGroup)
        self.countryCbox.setGeometry(QtCore.QRect(260, 140, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.countryCbox.setFont(font)
        self.countryCbox.setObjectName("countryCbox")
        self.countryCbox.addItem("")
        self.countryCbox.addItem("")
        self.countryCbox.addItem("")
        self.billLoadBut = QtWidgets.QPushButton(self.billGroup)
        self.billLoadBut.setGeometry(QtCore.QRect(230, 170, 101, 23))
        self.billLoadBut.setObjectName("billLoadBut")
        self.stateCbox = QtWidgets.QComboBox(self.billGroup)
        self.stateCbox.setGeometry(QtCore.QRect(200, 140, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stateCbox.setFont(font)
        self.stateCbox.setObjectName("stateCbox")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.ccFrame = QtWidgets.QFrame(self.centralwidget)
        self.ccFrame.setGeometry(QtCore.QRect(10, 510, 341, 81))
        self.ccFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ccFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ccFrame.setObjectName("ccFrame")
        self.ccGroup = QtWidgets.QGroupBox(self.ccFrame)
        self.ccGroup.setGeometry(QtCore.QRect(0, 0, 341, 81))
        self.ccGroup.setObjectName("ccGroup")
        self.ccnLine = QtWidgets.QLineEdit(self.ccGroup)
        self.ccnLine.setGeometry(QtCore.QRect(10, 20, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ccnLine.setFont(font)
        self.ccnLine.setText("")
        self.ccnLine.setObjectName("ccnLine")
        self.ccnLine.setValidator(QIntValidator())
        self.expmCbox = QtWidgets.QComboBox(self.ccGroup)
        self.expmCbox.setGeometry(QtCore.QRect(10, 50, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expmCbox.setFont(font)
        self.expmCbox.setObjectName("expmCbox")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.cvvLine = QtWidgets.QLineEdit(self.ccGroup)
        self.cvvLine.setGeometry(QtCore.QRect(190, 50, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cvvLine.setFont(font)
        self.cvvLine.setText("")
        self.cvvLine.setObjectName("cvvLine")
        self.cvvLine.setValidator(QIntValidator())
        self.expyCbox = QtWidgets.QComboBox(self.ccGroup)
        self.expyCbox.setGeometry(QtCore.QRect(100, 50, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expyCbox.setFont(font)
        self.expyCbox.setObjectName("expyCbox")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.creLoadBut = QtWidgets.QPushButton(self.ccGroup)
        self.creLoadBut.setGeometry(QtCore.QRect(270, 50, 61, 23))
        self.creLoadBut.setObjectName("creLoadBut")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(350, 460, 301, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.startBut = QtWidgets.QPushButton(self.frame)
        self.startBut.setEnabled(False)
        self.startBut.setGeometry(QtCore.QRect(10, 10, 291, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.startBut.setFont(font)
        self.startBut.setObjectName("startBut")
        self.readyBut = QtWidgets.QPushButton(self.frame)
        self.readyBut.setEnabled(True)
        self.readyBut.setGeometry(QtCore.QRect(10, 70, 131, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.readyBut.setFont(font)
        self.readyBut.setStyleSheet("")
        self.readyBut.setCheckable(False)
        self.readyBut.setChecked(False)
        self.readyBut.setAutoDefault(False)
        self.readyBut.setFlat(False)
        self.readyBut.setObjectName("readyBut")
        self.exitBut = QtWidgets.QPushButton(self.frame)
        self.exitBut.setGeometry(QtCore.QRect(150, 70, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitBut.setFont(font)
        self.exitBut.setObjectName("exitBut")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(550, 0, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)


        ###### Signal and Socket #####

        self.addBut.clicked.connect(self.addTolist)
        self.deleteBut.clicked.connect(self.removeFromlist)
        self.colorCombo.currentIndexChanged.connect(self.colorNotFound)

        self.billLoadBut.clicked.connect(self.loadBill)
        self.creLoadBut.clicked.connect(self.loadCre)

        self.readyBut.clicked.connect(self.setReady)
        self.startBut.clicked.connect(self.initial)
        self.startBut.clicked.connect(self.addToCart)
        self.startBut.clicked.connect(self.fillout)
        self.exitBut.clicked.connect(MainWindow.close)


        ###### Signal and Socket END #####
        try:
            filename = "./savedbinfo.xml"
            tree = ET.parse(filename)
            root = tree.getroot()
            self.nameLine.setText(root[0].text)
            self.emailLine.setText(root[1].text)
            self.numberLine.setText(root[2].text)
            self.addressLine.setText(root[3].text)
            self.aptLine.setText(root[4].text)
            self.zipLine.setText(root[5].text)
            self.cityLine.setText(root[6].text)
            self.stateCbox.setCurrentText(root[7].text)
            self.countryCbox.setCurrentText(root[8].text)

            filename = "./savedcinfo.xml"
            tree = ET.parse(filename)
            root = tree.getroot()
            self.ccnLine.setText(root[0].text)
            self.expmCbox.setCurrentIndex(int(root[1].text)-1)
            self.expyCbox.setCurrentText(root[2].text)
            self.cvvLine.setText(root[3].text)
        except(ValueError,TypeError,IndexError,NameError):
            msgBox = QMessageBox()
            msgBox.setText(traceback.format_exc())
            msgBox.exec()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.catCbox, self.sizeCbox)
        MainWindow.setTabOrder(self.sizeCbox, self.ocolorLine)
        MainWindow.setTabOrder(self.ocolorLine, self.colorCombo)
        MainWindow.setTabOrder(self.colorCombo, self.keyLine)
        MainWindow.setTabOrder(self.keyLine, self.addBut)
        MainWindow.setTabOrder(self.addBut, self.deleteBut)
        MainWindow.setTabOrder(self.deleteBut, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.nameLine)
        MainWindow.setTabOrder(self.nameLine, self.emailLine)
        MainWindow.setTabOrder(self.emailLine, self.numberLine)
        MainWindow.setTabOrder(self.numberLine, self.addressLine)
        MainWindow.setTabOrder(self.addressLine, self.aptLine)
        MainWindow.setTabOrder(self.aptLine, self.zipLine)
        MainWindow.setTabOrder(self.zipLine, self.cityLine)
        MainWindow.setTabOrder(self.cityLine, self.stateCbox)
        MainWindow.setTabOrder(self.stateCbox, self.countryCbox)
        MainWindow.setTabOrder(self.countryCbox, self.billLoadBut)
        MainWindow.setTabOrder(self.billLoadBut, self.ccnLine)
        MainWindow.setTabOrder(self.ccnLine, self.expmCbox)
        MainWindow.setTabOrder(self.expmCbox, self.expyCbox)
        MainWindow.setTabOrder(self.expyCbox, self.cvvLine)
        MainWindow.setTabOrder(self.cvvLine, self.creLoadBut)
        MainWindow.setTabOrder(self.creLoadBut, self.startBut)
        MainWindow.setTabOrder(self.startBut, self.readyBut)
        MainWindow.setTabOrder(self.readyBut, self.exitBut)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Supreme Bot", "By Yeram Hwang"))
        self.label_by.setText(_translate("MainWindow", "Supreme Bot by"))
        self.itemGroup.setTitle(_translate("MainWindow", "Item Section"))
        self.keyLab.setText(_translate("MainWindow", "Key Word"))
        self.ocolorLine.setPlaceholderText(_translate("MainWindow", "Enter Color if not listed."))
        self.sizeLab.setText(_translate("MainWindow", "Size"))
        self.sizeCbox.setItemText(0, _translate("MainWindow", "Small"))
        self.sizeCbox.setItemText(1, _translate("MainWindow", "Medium"))
        self.sizeCbox.setItemText(2, _translate("MainWindow", "Large"))
        self.sizeCbox.setItemText(3, _translate("MainWindow", "XLarge"))
        self.addBut.setText(_translate("MainWindow", "Add"))
        self.catCbox.setItemText(0, _translate("MainWindow", "Jackets"))
        self.catCbox.setItemText(1, _translate("MainWindow", "Shirts"))
        self.catCbox.setItemText(2, _translate("MainWindow", "Top/Sweater"))
        self.catCbox.setItemText(3, _translate("MainWindow", "Pants"))
        self.catCbox.setItemText(4, _translate("MainWindow", "Shorts"))
        self.catCbox.setItemText(5, _translate("MainWindow", "Hats"))
        self.catCbox.setItemText(6, _translate("MainWindow", "Bags"))
        self.catCbox.setItemText(7, _translate("MainWindow", "Acc"))
        self.catCbox.setItemText(8, _translate("MainWindow", "Skate"))
        self.colorCombo.setItemText(0, _translate("MainWindow", "Olive Russian Camo"))
        self.colorCombo.setItemText(1, _translate("MainWindow", "Orange"))
        self.colorCombo.setItemText(2, _translate("MainWindow", "Yellow"))
        self.colorCombo.setItemText(3, _translate("MainWindow", "Green"))
        self.colorCombo.setItemText(4, _translate("MainWindow", "Blue"))
        self.colorCombo.setItemText(5, _translate("MainWindow", "Navy"))
        self.colorCombo.setItemText(6, _translate("MainWindow", "Purple"))
        self.colorCombo.setItemText(7, _translate("MainWindow", "Black"))
        self.colorCombo.setItemText(8, _translate("MainWindow", "White"))
        self.colorCombo.setItemText(9, _translate("MainWindow", "Tan"))
        self.colorCombo.setItemText(10, _translate("MainWindow", "Red"))
        self.colorCombo.setItemText(11, _translate("MainWindow", "Others"))
        self.catLabel.setText(_translate("MainWindow", "Category"))
        self.colorLab.setText(_translate("MainWindow", "Color"))
        self.deleteBut.setText(_translate("MainWindow", "Remove"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Color"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Key Word"))
        self.billGroup.setTitle(_translate("MainWindow", "Billing Section"))
        self.nameLine.setPlaceholderText(_translate("MainWindow", "Full Name (F+L)"))
        self.emailLine.setPlaceholderText(_translate("MainWindow", "Email"))
        self.numberLine.setPlaceholderText(_translate("MainWindow", "Phone Number"))
        self.addressLine.setPlaceholderText(_translate("MainWindow", "Address"))
        self.aptLine.setPlaceholderText(_translate("MainWindow", "APT#"))
        self.zipLine.setPlaceholderText(_translate("MainWindow", "ZIP"))
        self.cityLine.setPlaceholderText(_translate("MainWindow", "City"))
        self.countryCbox.setItemText(0, _translate("MainWindow", "USA"))
        self.countryCbox.setItemText(1, _translate("MainWindow", "Mexico"))
        self.countryCbox.setItemText(2, _translate("MainWindow", "Canada"))
        self.billLoadBut.setText(_translate("MainWindow", "Load"))
        self.stateCbox.setItemText(0, _translate("MainWindow", "AK"))
        self.stateCbox.setItemText(1, _translate("MainWindow", "AL"))
        self.stateCbox.setItemText(2, _translate("MainWindow", "AR"))
        self.stateCbox.setItemText(3, _translate("MainWindow", "AZ"))
        self.stateCbox.setItemText(4, _translate("MainWindow", "CA"))
        self.stateCbox.setItemText(5, _translate("MainWindow", "CO"))
        self.stateCbox.setItemText(6, _translate("MainWindow", "CT"))
        self.stateCbox.setItemText(7, _translate("MainWindow", "DE"))
        self.stateCbox.setItemText(8, _translate("MainWindow", "FL"))
        self.stateCbox.setItemText(9, _translate("MainWindow", "GA"))
        self.stateCbox.setItemText(10, _translate("MainWindow", "HI"))
        self.stateCbox.setItemText(11, _translate("MainWindow", "IA"))
        self.stateCbox.setItemText(12, _translate("MainWindow", "ID"))
        self.stateCbox.setItemText(13, _translate("MainWindow", "IL"))
        self.stateCbox.setItemText(14, _translate("MainWindow", "IN"))
        self.stateCbox.setItemText(15, _translate("MainWindow", "KS"))
        self.stateCbox.setItemText(16, _translate("MainWindow", "KY"))
        self.stateCbox.setItemText(17, _translate("MainWindow", "LA"))
        self.stateCbox.setItemText(18, _translate("MainWindow", "MA"))
        self.stateCbox.setItemText(19, _translate("MainWindow", "MD"))
        self.stateCbox.setItemText(20, _translate("MainWindow", "ME"))
        self.stateCbox.setItemText(21, _translate("MainWindow", "MI"))
        self.stateCbox.setItemText(22, _translate("MainWindow", "MN"))
        self.stateCbox.setItemText(23, _translate("MainWindow", "MO"))
        self.stateCbox.setItemText(24, _translate("MainWindow", "MS"))
        self.stateCbox.setItemText(25, _translate("MainWindow", "MT"))
        self.stateCbox.setItemText(26, _translate("MainWindow", "NC"))
        self.stateCbox.setItemText(27, _translate("MainWindow", "ND"))
        self.stateCbox.setItemText(28, _translate("MainWindow", "NE"))
        self.stateCbox.setItemText(29, _translate("MainWindow", "NH"))
        self.stateCbox.setItemText(30, _translate("MainWindow", "NJ"))
        self.stateCbox.setItemText(31, _translate("MainWindow", "NM"))
        self.stateCbox.setItemText(32, _translate("MainWindow", "NV"))
        self.stateCbox.setItemText(33, _translate("MainWindow", "NY"))
        self.stateCbox.setItemText(34, _translate("MainWindow", "OH"))
        self.stateCbox.setItemText(35, _translate("MainWindow", "OK"))
        self.stateCbox.setItemText(36, _translate("MainWindow", "OR"))
        self.stateCbox.setItemText(37, _translate("MainWindow", "PA"))
        self.stateCbox.setItemText(38, _translate("MainWindow", "RI"))
        self.stateCbox.setItemText(39, _translate("MainWindow", "SC"))
        self.stateCbox.setItemText(40, _translate("MainWindow", "SD"))
        self.stateCbox.setItemText(41, _translate("MainWindow", "TN"))
        self.stateCbox.setItemText(42, _translate("MainWindow", "TX"))
        self.stateCbox.setItemText(43, _translate("MainWindow", "UT"))
        self.stateCbox.setItemText(44, _translate("MainWindow", "VA"))
        self.stateCbox.setItemText(45, _translate("MainWindow", "VT"))
        self.stateCbox.setItemText(46, _translate("MainWindow", "WA"))
        self.stateCbox.setItemText(47, _translate("MainWindow", "WI"))
        self.stateCbox.setItemText(48, _translate("MainWindow", "WV"))
        self.stateCbox.setItemText(49, _translate("MainWindow", "WY"))
        self.ccGroup.setTitle(_translate("MainWindow", "Payment Section"))
        self.ccnLine.setPlaceholderText(_translate("MainWindow", "Credit Card Number"))
        self.expmCbox.setItemText(0, _translate("MainWindow", "01-Jan"))
        self.expmCbox.setItemText(1, _translate("MainWindow", "02-Feb"))
        self.expmCbox.setItemText(2, _translate("MainWindow", "03-Mar"))
        self.expmCbox.setItemText(3, _translate("MainWindow", "04-Apr"))
        self.expmCbox.setItemText(4, _translate("MainWindow", "05-May"))
        self.expmCbox.setItemText(5, _translate("MainWindow", "06-Jun"))
        self.expmCbox.setItemText(6, _translate("MainWindow", "07-Jul"))
        self.expmCbox.setItemText(7, _translate("MainWindow", "08-Aug"))
        self.expmCbox.setItemText(8, _translate("MainWindow", "09-Sept"))
        self.expmCbox.setItemText(9, _translate("MainWindow", "10-Oct"))
        self.expmCbox.setItemText(10, _translate("MainWindow", "11-Nov"))
        self.expmCbox.setItemText(11, _translate("MainWindow", "12-Dec"))
        self.cvvLine.setPlaceholderText(_translate("MainWindow", "CVV"))
        self.expyCbox.setItemText(0, _translate("MainWindow", "2020"))
        self.expyCbox.setItemText(1, _translate("MainWindow", "2021"))
        self.expyCbox.setItemText(2, _translate("MainWindow", "2022"))
        self.expyCbox.setItemText(3, _translate("MainWindow", "2023"))
        self.expyCbox.setItemText(4, _translate("MainWindow", "2024"))
        self.expyCbox.setItemText(5, _translate("MainWindow", "2025"))
        self.expyCbox.setItemText(6, _translate("MainWindow", "2026"))
        self.expyCbox.setItemText(7, _translate("MainWindow", "2027"))
        self.expyCbox.setItemText(8, _translate("MainWindow", "2028"))
        self.expyCbox.setItemText(9, _translate("MainWindow", "2029"))
        self.expyCbox.setItemText(10, _translate("MainWindow", "2030"))
        self.creLoadBut.setText(_translate("MainWindow", "Load"))
        self.startBut.setText(_translate("MainWindow", "START!!!"))
        self.readyBut.setText(_translate("MainWindow", "READY"))
        self.exitBut.setText(_translate("MainWindow", "EXIT"))
        self.label_name.setText(_translate("MainWindow", "BP-FK-G"))

    def initial(self, MainWindow):
        # load chrome
        global driver

        ## Steven Code
        chrome_options = self.add_chrome_argument_options()
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) #added anti-bot behaviors
        ## End of Steven Code

        # Goto Surpeme url
        driver.get('https://www.supremenewyork.com/shop/all')
        
    
    ## Steven Code
    def add_chrome_argument_options(self):
        """
        add_argument_options : None -> Options()
        add_argument_options() Disable Blink features and automation indicator to imitate human interaction with navigator. Return Options.
        """
        chrome_options = Options()
        # chrome_options.add_argument("--kiosk")
        # chrome_options.add_argument("disable-infobars")
        # chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        return chrome_options
    ## End of Steven Code
    

    def addToCart(self, MainWindow):
        try:
            for i in range(self.tableWidget.rowCount()):
                # Category selection
                cattext = self.tableWidget.item(i,0).text().lower()
                category = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.LINK_TEXT, cattext))
                )
                category.click()

                # Product selection
                keytext = self.tableWidget.item(i,3).text().capitalize()
                product = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, keytext))
                )
                product.click()

                # Color selector
                driver.implicitly_wait(2)
                colortext = self.tableWidget.item(i,2).text()
                tempXpath = "//button[@data-style-name='" + colortext + "']"
                colorSel = driver.find_element_by_xpath(tempXpath)
                colorSel.click()

                # Size selector
                driver.implicitly_wait(1)
                sizetext = self.tableWidget.item(i,1).text()
                
                # sizeXpath = "//*[@id='s']/option[. = '" + sizetext +  "']"
                # print("DEBUG-" + sizeXpath)
                # size = driver.find_element_by_xpath(sizeXpath)
                # size.click()
                
                # Steven Code
                sizeSelector = Select(driver.find_element(By.ID,"size"))
                sizeSelector.select_by_visible_text(sizetext)
                # driver.implicitly_wait(1)
                time.sleep(3.5)
                
                # End of Steven Code

                # Click add-to-cart button
                addtocartBut = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.NAME, "commit"))
                )
                addtocartBut.click()
                time.sleep(.5)

                # Navigate back to the listing page
                driver.get('https://www.supremenewyork.com/shop/all')
        except(ValueError,TypeError,IndexError,NameError):
            msgBox = QMessageBox()
            msgBox.setText(traceback.format_exc())
            msgBox.exec()

    def fillout(self, MainWindow):
        try:
            # wait for checkout button element to load
            checkout = driver.find_element_by_xpath("//a[@class='button checkout']")
            checkout.click()

            # fill out checkout screen fields
            driver.find_element_by_id('order_billing_name').send_keys(self.nameLine.text())
            driver.find_element_by_id('order_email').send_keys(self.emailLine.text())
            driver.find_element_by_id('order_tel').send_keys(self.numberLine.text())
            driver.find_element_by_id('order_billing_address').send_keys(self.addressLine.text())
            driver.find_element_by_id('order_billing_address_2').send_keys(self.aptLine.text())
            driver.find_element_by_id('order_billing_zip').send_keys(self.zipLine.text())
            driver.find_element_by_id('order_billing_city').send_keys(self.cityLine.text())

            driver.find_element_by_id('order_billing_state').send_keys(self.stateCbox.currentText())
            driver.find_element_by_id('order_billing_country').send_keys(self.countryCbox.currentText())


            # driver.find_element(By.ID,"order_terms").click()



            # Credit Card info section
            tree = ET.parse('savedcinfo.xml')
            root = tree.getroot()



            ## Steven Code
            driver.find_element(By.ID,'credit_card_number').send_keys(self.ccnLine.text())

            cardmonthSelector = Select(driver.find_element(By.ID,"credit_card_month"))
            cardmonthSelector.select_by_value("07")            

            cardyearSelector = Select(driver.find_element(By.ID,"credit_card_year"))
            cardyearSelector.select_by_value("2023")
            
            driver.find_element(By.ID,"credit_card_verification_value").send_keys(self.cvvLine.text())
            
            # driver.find_element(By.ID,"order_terms").click()
            ## End of Steven Code
            
            
            # Original Code
            # driver.find_element_by_name('credit_card[month]').send_keys(self.expmCbox.currentText())
            # driver.find_element_by_name('credit_card[year]').send_keys(self.expyCbox.currentText())
            # driver.find_element_by_id('orcer').send_keys(self.cvvLine.text())



            # Process save address and term&condition check box click
            for combo in driver.find_elements_by_css_selector('.iCheck-helper'):
                combo.click()

        
            # Click process payment
            driver.find_element_by_name('commit').click()
            
            
            
        except(ValueError,TypeError,IndexError,NameError):
            msgBox = QMessageBox()
            msgBox.setText(traceback.format_exc())
            msgBox.exec()

    def addTolist(self, MainWindow):
        try:
            if(self.keyLine.text() == ""):
                msgBox = QMessageBox()
                msgBox.setText("Key word was not ented")
                msgBox.exec()
                return
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            self.tableWidget.setItem(row, 0, QTableWidgetItem(self.catCbox.currentText()))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(self.sizeCbox.currentText()))

            if(self.colorCombo.currentText() == 'Others'):
                self.tableWidget.setItem(row, 2, QTableWidgetItem(self.ocolorLine.text()))
            else:
                self.tableWidget.setItem(row, 2, QTableWidgetItem(self.colorCombo.currentText()))

            self.tableWidget.setItem(row, 3, QTableWidgetItem(self.keyLine.text()))
        except(ValueError,TypeError,IndexError,NameError):
            msgBox = QMessageBox()
            msgBox.setText(traceback.format_exc())
            msgBox.exec()

    def removeFromlist(self, MainWindow):
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def colorNotFound(self, MainWindow):
        if(self.colorCombo.currentText() == 'Others'):
            self.ocolorLine.setEnabled(True)
        else:
            self.colorCombo.update()
            self.ocolorLine.setEnabled(False)

    def loadBill(self, MainWindow):
        try:
            #OpenFile Dialog and select
            dialog = QFileDialog.getOpenFileName(None, 'Open file',"savedbinfo.xml","XML files (*.xml)")
            filepath = dialog[0]
            if(filepath == ''):
                return


            # Open .xml file and load the data
            tree = ET.parse(filepath)
            root = tree.getroot()
            self.nameLine.setText(root[0].text)
            self.emailLine.setText(root[1].text)
            self.numberLine.setText(root[2].text)
            self.addressLine.setText(root[3].text)
            self.aptLine.setText(root[4].text)
            self.zipLine.setText(root[5].text)
            self.cityLine.setText(root[6].text)
            self.stateCbox.setCurrentText(root[7].text)
            self.countryCbox.setCurrentText(root[8].text)
        except(ValueError,TypeError,IndexError,NameError):
            msgBox = QMessageBox()
            msgBox.setText(traceback.format_exc())
            msgBox.exec()

    def loadCre(self, MainWindow):
        try:
            dialog = QFileDialog.getOpenFileName(None, 'Open file',"savedcinfo.xml","XML files (*.xml)")
            filepath = dialog[0]
            if(filepath == ''):
                return

            tree = ET.parse(filepath)
            root = tree.getroot()

            self.ccnLine.setText(root[0].text)
            self.expmCbox.setCurrentIndex(int(root[1].text)-1)
            self.expyCbox.setCurrentText(root[2].text)
            self.cvvLine.setText(root[3].text)
        except(ValueError,TypeError,IndexError,NameError):
            msgBox = QMessageBox()
            msgBox.setText(traceback.format_exc())
            msgBox.exec()

    def setReady(self, MainWindow):
        try:
            if(self.isReady(MainWindow)):
                if(self.readyBut.text() == "READY"):
                    self.readyBut.setText("Change")
                    self.startBut.setEnabled(True)
                    self.bilFrame.setEnabled(False)
                    self.itemFrame.setEnabled(False)
                    self.ccFrame.setEnabled(False)
                else:
                    self.readyBut.setText("READY")
                    self.startBut.setEnabled(False)
                    self.bilFrame.setEnabled(True)
                    self.itemFrame.setEnabled(True)
                    self.ccFrame.setEnabled(True)
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Warning")
                msgBox.setText("Please check follwing:\nProduct info \nBilling info \nCredit card info ")
                msgBox.exec()

        except(ValueError,TypeError,IndexError,NameError):
            msgBox = QMessageBox()
            msgBox.setText(traceback.format_exc())
            msgBox.exec()

    def isReady(self ,MainWindow):
        if((self.tableWidget.rowCount() != 0) and \
            (self.nameLine.text() != "") and \
            (self.emailLine.text() != "") and \
            (self.numberLine.text() != "") and \
            (self.addressLine.text() != "") and \
            (self.zipLine.text() != "") and \
            (self.cityLine.text() != "") and \
            (self.ccnLine.text() != "") and \
            (self.cvvLine.text() != "")):
            return True
        else:
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
