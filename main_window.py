# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnsiRefractor(object):
    def setupUi(self, EnsiRefractor):
        EnsiRefractor.setObjectName("EnsiRefractor")
        EnsiRefractor.resize(509, 309)
        EnsiRefractor.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        EnsiRefractor.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(EnsiRefractor)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(140, 230, 181, 31))
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 20, 491, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 201, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 190, 171, 71))
        self.pushButton.setObjectName("pushButton")
        EnsiRefractor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EnsiRefractor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName("menubar")
        EnsiRefractor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EnsiRefractor)
        self.statusbar.setObjectName("statusbar")
        EnsiRefractor.setStatusBar(self.statusbar)

        self.retranslateUi(EnsiRefractor)
        QtCore.QMetaObject.connectSlotsByName(EnsiRefractor)

    def retranslateUi(self, EnsiRefractor):
        _translate = QtCore.QCoreApplication.translate
        EnsiRefractor.setWindowTitle(_translate("EnsiRefractor", "MainWindow"))
        self.checkBox.setText(_translate("EnsiRefractor", "Make backup folder "))
        self.lineEdit.setText(_translate("EnsiRefractor", "Folder containing gprojects to refract"))
        self.label.setText(_translate("EnsiRefractor", "Refracted directory"))
        self.pushButton.setText(_translate("EnsiRefractor", "REFRACTOR PATH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnsiRefractor = QtWidgets.QMainWindow()
    ui = Ui_EnsiRefractor()
    ui.setupUi(EnsiRefractor)
    EnsiRefractor.show()
    sys.exit(app.exec_())