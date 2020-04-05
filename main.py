# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from MakeData import MakeData

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.shuf = []
        self.market = []
        self.ramilevi = []
        self.product_shufersal = [] # for the items
        self.product_market = [] # for the items
        self.product_ramilevi = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(518, 81, 191, 21))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(248, 82, 191, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 80, 181, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.calcbtn = QtWidgets.QPushButton(self.centralwidget)
        self.calcbtn.setGeometry(QtCore.QRect(320, 510, 141, 41))
        self.calcbtn.setObjectName("calcbtn")
        self.add1 = QtWidgets.QPushButton(self.centralwidget)
        self.add1.setGeometry(QtCore.QRect(720, 80, 31, 23))
        self.add1.setObjectName("add2_2")
        self.add3 = QtWidgets.QPushButton(self.centralwidget)
        self.add3.setGeometry(QtCore.QRect(200, 80, 31, 23))
        self.add3.setObjectName("add3")
        self.add2 = QtWidgets.QPushButton(self.centralwidget)
        self.add2.setGeometry(QtCore.QRect(450, 80, 31, 23))
        self.add2.setObjectName("add2")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(590, 110, 201, 331))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 120, 201, 311))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 201, 321))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 371, 51))
        self.label_1.clear()
        self.label_2.clear()
        self.label_3.clear()
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.price1 = QtWidgets.QLabel(self.centralwidget)
        self.price1.setGeometry(QtCore.QRect(580, 460, 171, 41))
        self.price1.setObjectName("price1")
        self.price2 = QtWidgets.QLabel(self.centralwidget)
        self.price2.setGeometry(QtCore.QRect(300, 460, 171, 41))
        self.price2.setObjectName("price2")
        self.price3 = QtWidgets.QLabel(self.centralwidget)
        self.price3.setGeometry(QtCore.QRect(20, 460, 171, 41))
        self.price3.setObjectName("price3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.manageComboBox()
        self.add1.clicked.connect(self.add1Func)
        self.add2.clicked.connect(self.add2Func)
        self.add3.clicked.connect(self.add3Func)
        self.calcbtn.clicked.connect(self.calc)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calcbtn.setText(_translate("MainWindow", "Calculate"))
        self.add1.setText(_translate("MainWindow", "Add"))
        self.add3.setText(_translate("MainWindow", "Add"))
        self.add2.setText(_translate("MainWindow", "Add"))
        self.label_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Prices comparing"))
        self.price1.setText(_translate("MainWindow", "Shufersal price:"))
        self.price2.setText(_translate("MainWindow", "Storage market price:"))
        self.price3.setText(_translate("MainWindow", "Rami levi price:"))

    def manageComboBox(self):
        maker = MakeData()
        maker.makeAll()
        for i in range(len(maker.data_shufersal)):
            self.shuf.append(maker.data_shufersal[i])
            self.comboBox1.addItem(maker.data_shufersal[i].product_name)
        for j in range(len(maker.data_market)):
            self.market.append(maker.data_market[j])
            self.comboBox_2.addItem(maker.data_market[j].product_name)
        for k in range(len(maker.data_ramilevi)):
            self.ramilevi.append((maker.data_ramilevi[k]))
            self.comboBox_3.addItem(maker.data_ramilevi[k].product_name)
            
    def add1Func(self):
        text = str(self.comboBox1.currentText())
        all_text = self.label_1.text() + "\n" + text
        self.label_1.setText(all_text)
        for i in range(len(self.shuf)):
            if (self.comboBox1.currentText() == self.shuf[i].product_name):
                self.product_shufersal.append(self.shuf[i])

    def add2Func(self):
        text = str(self.comboBox_2.currentText())
        all_text = self.label_2.text() + "\n" + text
        self.label_2.setText(all_text)
        for i in range(len(self.market)):
            if (self.comboBox_2.currentText() == self.market[i].product_name):
                self.product_market.append(self.market[i])

    def add3Func(self):
        text = str(self.comboBox_3.currentText())
        all_text = self.label_3.text() + "\n" + text
        self.label_3.setText(all_text)
        for i in range(len(self.ramilevi)):
            if (self.comboBox_3.currentText() == self.ramilevi[i].product_name):
                self.product_ramilevi.append(self.ramilevi[i])

    def calc(self):
        shuf_total = 0
        market_total = 0
        ramilevi_total = 0
        for i in range(len(self.product_shufersal)):
            shuf_total += float(self.product_shufersal[i].price)
        for j in range(len(self.product_market)):
             market_total += float(self.product_market[j].price)
        for k in range(len(self.product_ramilevi)):
             ramilevi_total += float(self.product_ramilevi[k].price)
        self.price1.clear()
        self.price1.setText("Shufersal price : " + str(shuf_total))
        self.price2.clear()
        self.price2.setText("Storage market price : " + str(market_total))
        self.price3.clear()
        self.price3.setText("Rami Levi price : " + str(ramilevi_total))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

