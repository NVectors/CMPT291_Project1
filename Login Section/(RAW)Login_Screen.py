# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Login(object):
    def setupUi(self, Dialog_Login):
        Dialog_Login.setObjectName("Dialog_Login")
        Dialog_Login.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Dialog_Login.setFont(font)
        Dialog_Login.setWindowTitle("Home")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Resource/home_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog_Login.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Dialog_Login)
        self.groupBox.setGeometry(QtCore.QRect(160, 160, 321, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_user = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")
        self.gridLayout.addWidget(self.label_user, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_pass = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_pass.setFont(font)
        self.label_pass.setObjectName("label_pass")
        self.gridLayout_2.addWidget(self.label_pass, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.pushButton_newUser = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_newUser.setFont(font)
        self.pushButton_newUser.setAutoFillBackground(False)
        self.pushButton_newUser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_newUser.setObjectName("pushButton_newUser")
        self.horizontalLayout_3.addWidget(self.pushButton_newUser)
        self.pushButton_login = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout_3.addWidget(self.pushButton_login)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_loginBackground = QtWidgets.QLabel(Dialog_Login)
        self.label_loginBackground.setGeometry(QtCore.QRect(-260, -110, 971, 691))
        self.label_loginBackground.setStyleSheet("image: url(:/Resource/login_background.jpg)")
        self.label_loginBackground.setText("")
        self.label_loginBackground.setObjectName("label_loginBackground")
        self.label_loginBackground.raise_()
        self.groupBox.raise_()

        self.retranslateUi(Dialog_Login)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Login)

    def retranslateUi(self, Dialog_Login):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("Dialog_Login", "Welcome Back!"))
        self.label_user.setText(_translate("Dialog_Login", " Username"))
        self.label_pass.setText(_translate("Dialog_Login", " Password "))
        self.pushButton_cancel.setText(_translate("Dialog_Login", "Cancel"))
        self.pushButton_newUser.setText(_translate("Dialog_Login", "New User"))
        self.pushButton_login.setText(_translate("Dialog_Login", "Login"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Login = QtWidgets.QDialog()
    ui = Ui_Dialog_Login()
    ui.setupUi(Dialog_Login)
    Dialog_Login.show()
    sys.exit(app.exec_())
