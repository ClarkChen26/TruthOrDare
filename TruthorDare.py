# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TruthorDare.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys
import random

class Ui_MainWindow(object):
    def random_name(self):
        with open('name') as f:
            name_list = f.read().splitlines()
            name = random.choice(name_list)
            QtWidgets.qApp.processEvents()
            self.textBrowser.setFontPointSize(100)
            self.textBrowser.setText(name)
            self.textBrowser.setAlignment(QtCore.Qt.AlignCenter)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 1005)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 30, 791, 111))
        font = QtGui.QFont()
        font.setPointSize(100)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1260, 80, 121, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Huafeng/HuafengMagazine/Resources/Assets.xcassets/AppIcon.appiconset/120.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 181, 531))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pics/Screen Shot 2019-04-12 at 11.50.54 PM.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1490, 240, 151, 541))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("pics/Screen Shot 2019-04-13 at 12.05.24 AM.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1500, 920, 161, 31))
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 230, 1601, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 210, 1601, 21))
        self.line_2.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(210, 240, 20, 511))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1480, 240, 20, 541))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 300, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(230, 760, 1251, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 480, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(890, 300, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1180, 480, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setItalic(True)
        font.setUnderline(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1160, 240, 16, 521))
        self.line_5.setStyleSheet("background-color: rgba(253, 102, 102, 153);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(530, 240, 16, 521))
        self.line_6.setStyleSheet("background-color: rgba(102, 255, 255, 153);")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(50, 770, 20, 71))
        self.line_7.setStyleSheet("background-color: rgba(102, 255, 255, 153);")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(140, 840, 20, 71))
        self.line_8.setStyleSheet("background-color: rgba(253, 102, 102, 153);")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 820, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 850, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 890, 16, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(180, 920, 16, 16))
        self.label_9.setObjectName("label_9")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(40, 960, 1601, 21))
        self.line_9.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 640, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 20px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
        "        );\n"
        "    }\n"
        "")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.random_name)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "来自”生活“的压迫"))
        self.label_5.setText(_translate("MainWindow", "Developed by Zhijie Chen"))
        self.pushButton.setText(_translate("MainWindow", "真心话"))
        self.pushButton_2.setText(_translate("MainWindow", "大冒险"))
        self.pushButton_3.setText(_translate("MainWindow", "真心话"))
        self.pushButton_4.setText(_translate("MainWindow", "大冒险"))
        self.label_6.setText(_translate("MainWindow", "正"))
        self.label_7.setText(_translate("MainWindow", "常"))
        self.label_8.setText(_translate("MainWindow", "刺"))
        self.label_9.setText(_translate("MainWindow", "激"))
        self.pushButton_5.setText(_translate("MainWindow", "名字"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())