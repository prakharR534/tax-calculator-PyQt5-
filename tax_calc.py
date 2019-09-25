# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tax_calc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.price_box = QtWidgets.QTextEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(190, 40, 201, 41))
        self.price_box.setObjectName("price_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 59, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(260, 120, 131, 41))
        self.spinBox.setProperty("value", 18)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cal_tax_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cal_tax_btn.setGeometry(QtCore.QRect(180, 210, 221, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.cal_tax_btn.setFont(font)
        self.cal_tax_btn.setObjectName("cal_tax_btn")
        self.result_window = QtWidgets.QTextEdit(self.centralwidget)
        self.result_window.setGeometry(QtCore.QRect(170, 320, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.result_window.setFont(font)
        self.result_window.setObjectName("result_window")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 40, 541, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Price"))
        self.label_2.setText(_translate("MainWindow", "Tax Rate "))
        self.cal_tax_btn.setText(_translate("MainWindow", "Calculate Tax"))
        self.label_3.setText(_translate("MainWindow", "Sales Tax Calculator"))
        

    def Calculate_tax(self):
        Price =int(self.price_box.toPlainText())
        tax = (self.tax_rate.value())
        total_price = price + ((tax/100)*price)
        total_price_string = "The total price with tax is: "+str(total_price)
        self.result_window.setText(total_price_string)    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    self.cal_tax_btn.clicked.connect(self.Calculate_tax)
    sys.exit(app.exec_())
    self.cal_tax_btn.clicked.connect(self.Calculate_tax)
