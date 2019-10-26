#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import source_rc

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Class for Login Window. 
Login Window asks for Username and Password.
There a "Cancel" button, a "New User" button which pops up a new window and "Login" button.
'''


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
class Ui_Dialog_Login(object):
    '''
    "Cancel" button has been clicked and cancelButton() function is called to close the window.
    '''

    def cancelButton(self):
        sys.exit()

    def NewUserButton(self):
        Dialog_Register = QtWidgets.QDialog()
        ui = Ui_Dialog_Register()
        ui.setupUi(Dialog_Register)
        Dialog_Register.exec_()
        Dialog_Register.show()

    def setupUi(self, Dialog_Login):
        Dialog_Login.setObjectName("Dialog_Login")
        Dialog_Login.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Dialog_Login.setFont(font)
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
        self.label_pass = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_pass.setFont(font)
        self.label_pass.setObjectName("label_pass")
        self.gridLayout_2.addWidget(self.label_pass, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
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
        '''
        Call a cliked() function when button is clicked

        '''
        # self.pushButton_cancel.clicked.connect(Dialog_Login.close)
        self.pushButton_cancel.clicked.connect(self.cancelButton)

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

        self.pushButton_newUser.clicked.connect(self.NewUserButton)

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
        self.label = QtWidgets.QLabel(Dialog_Login)
        self.label.setGeometry(QtCore.QRect(-200, -20, 951, 521))
        self.label.setStyleSheet("image:url(:/newPrefix/janke-laskowski-gneiEi5yN1s-unsplash.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.groupBox.raise_()

        self.retranslateUi(Dialog_Login)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Login)

    def retranslateUi(self, Dialog_Login):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Login.setWindowTitle(_translate("Dialog_Login", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog_Login", "Welcome Back!"))
        self.label_user.setText(_translate("Dialog_Login", " Username"))
        self.label_pass.setText(_translate("Dialog_Login", " Password "))
        self.pushButton_cancel.setText(_translate("Dialog_Login", "Cancel"))
        self.pushButton_newUser.setText(_translate("Dialog_Login", "New User"))
        self.pushButton_login.setText(_translate("Dialog_Login", "Login"))
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------


'''
Class for New User Registration Window. 
Pops up when user clicks on the "New User" button int the Login Window.
It get priority as the focus and it's window can only be closed via "Cancel" button click or "Add" button click
'''


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registeration_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

class Ui_Dialog_Register(object):
    def setupUi(self, Dialog_Register):
        Dialog_Register.setObjectName("Dialog_Register")
        Dialog_Register.resize(640, 480)
        Dialog_Register.setModal(True)
        self.groupBox = QtWidgets.QGroupBox(Dialog_Register)
        self.groupBox.setGeometry(QtCore.QRect(80, 50, 491, 321))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 7, 1)
        self.label_firstName = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_firstName.setFont(font)
        self.label_firstName.setObjectName("label_firstName")
        self.gridLayout_2.addWidget(self.label_firstName, 3, 0, 1, 1)
        self.label_userCity = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_userCity.setFont(font)
        self.label_userCity.setObjectName("label_userCity")
        self.gridLayout_2.addWidget(self.label_userCity, 5, 0, 1, 1)
        self.label_rPass = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_rPass.setFont(font)
        self.label_rPass.setObjectName("label_rPass")
        self.gridLayout_2.addWidget(self.label_rPass, 1, 0, 1, 1)
        self.label_lastName = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_lastName.setFont(font)
        self.label_lastName.setObjectName("label_lastName")
        self.gridLayout_2.addWidget(self.label_lastName, 4, 0, 1, 1)
        self.label_rUser = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_rUser.setFont(font)
        self.label_rUser.setObjectName("label_rUser")
        self.gridLayout_2.addWidget(self.label_rUser, 0, 0, 1, 1)
        self.label_userType = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_userType.setFont(font)
        self.label_userType.setObjectName("label_userType")
        self.gridLayout_2.addWidget(self.label_userType, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_rcancel = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_rcancel.setFont(font)
        self.pushButton_rcancel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "")
        self.pushButton_rcancel.setObjectName("pushButton_rcancel")
        self.horizontalLayout_2.addWidget(self.pushButton_rcancel)
        self.pushButton_add = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog_Register)
        self.label_2.setGeometry(QtCore.QRect(-50, -60, 731, 581))
        self.label_2.setStyleSheet("image: url(:/newPrefix/n-n-BtbjCFUvBXs-unsplash.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.groupBox.raise_()

        self.retranslateUi(Dialog_Register)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Register)

    def retranslateUi(self, Dialog_Register):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Register.setWindowTitle(_translate("Dialog_Register", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog_Register", "Register as New User"))
        self.label.setText(_translate("Dialog_Register", " Confirm Password "))
        self.checkBox.setText(_translate("Dialog_Register", " Agent "))
        self.checkBox_2.setText(_translate("Dialog_Register", " Officer"))
        self.label_firstName.setText(_translate("Dialog_Register", " First Name "))
        self.label_userCity.setText(_translate("Dialog_Register", " City"))
        self.label_rPass.setText(_translate("Dialog_Register", " Password"))
        self.label_lastName.setText(_translate("Dialog_Register", " Last Name"))
        self.label_rUser.setText(_translate("Dialog_Register", " Username "))
        self.label_userType.setText(_translate("Dialog_Register", " Type"))
        self.pushButton_rcancel.setText(_translate("Dialog_Register", "Cancel"))
        self.pushButton_add.setText(_translate("Dialog_Register", "Add"))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog_Login = QtWidgets.QDialog()
    ui = Ui_Dialog_Login()
    ui.setupUi(Dialog_Login)
    Dialog_Login.show()
    sys.exit(app.exec_())

