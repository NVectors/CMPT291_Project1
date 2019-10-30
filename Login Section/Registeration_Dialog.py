from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3


class Ui_Dialog_Register(object):
    def __init__(self):
        # QtWidgets.QDialog.__init__(self)
        # self.setupUi(self)
        self.connection = sqlite3.connect('p1.db')
        self.cursor = self.connection.cursor()

    '''
    "Cancel" button has been clicked and cancelButton() function is called to close the window.
    '''

    def cancelButton(self):
        sys.exit()

    def addButton(self):
        username = self.lineEdit_username.text()
        password_one = self.lineEdit_passwordOne.text()
        password_two = self.lineEdit_passwordTwo.text()
        first_name = self.lineEdit_firstName.text()
        last_name = self.lineEdit_lastName.text()
        city = self.lineEdit_city.text()
        checkBox_Agent = self.checkBox_agent.isChecked()
        checkBox_Officer = self.checkBox_officer.isChecked()

        if (not (username and password_one and password_two and first_name and last_name and city)) and (
                (checkBox_Agent is False) and (checkBox_Officer is False)):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Incomplete!')
            error_dialog.exec_()
        elif not username:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Username is missing')
            error_dialog.exec_()
        elif not password_one:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Password is missing')
            error_dialog.exec_()
        elif not first_name:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('First name is missing')
            error_dialog.exec_()
        elif not last_name:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Last name is missing')
            error_dialog.exec_()
        elif not city:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('City is missing')
            error_dialog.exec_()
        elif ((checkBox_Agent is False) and (checkBox_Officer is False)):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Did not check mark at "Type"')
            error_dialog.exec_()
        elif ((checkBox_Agent is True) and (checkBox_Officer is True)):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Can not check mark both at "Type"')
            error_dialog.exec_()
        else:
            self.register(username, password_one, password_two, first_name, last_name, city, checkBox_Agent,
                          checkBox_Officer)

    def register(self, username, password_one, password_two, first_name, last_name, city, checkBox_Agent,
                 checkBox_Officer):
        self.cursor.execute('''Select uid FROM users ''')
        registered_users = self.cursor.fetchall()

        check = False
        for info in registered_users:
            if (username.lower() == info[0].lower()):
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText('Username is already registered!')
                error_dialog.exec_()
                check = True

        if (check == False):
            if (password_one != password_two):
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText('Password does not match!')
                error_dialog.exec_()
            else:
                if (checkBox_Agent is True):
                    user_type = 'a'
                elif (checkBox_Officer is True):
                    user_type = 'o'
                # print (username,password_one,user_type,first_name,last_name,city)
                values = (username, password_one, user_type, first_name, last_name, city)
                self.cursor.execute('INSERT into users VALUES (?,?,?,?,?,?)', values)
                self.connection.commit()
                dialog = QtWidgets.QMessageBox()
                dialog.setText('You are now registered!')
                dialog.exec_()

    def setupUi(self, Dialog_Register):
        Dialog_Register.setObjectName("Dialog_Register")
        Dialog_Register.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Resource/newUser_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog_Register.setWindowIcon(icon)
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
        self.lineEdit_username = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 0, 0, 1, 1)
        self.lineEdit_lastName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        self.gridLayout.addWidget(self.lineEdit_lastName, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_agent = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_agent.setFont(font)
        self.checkBox_agent.setObjectName("checkBox_agent")
        self.horizontalLayout.addWidget(self.checkBox_agent)
        self.checkBox_officer = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_officer.setFont(font)
        self.checkBox_officer.setObjectName("checkBox_officer")
        self.horizontalLayout.addWidget(self.checkBox_officer)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.lineEdit_passwordOne = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_passwordOne.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwordOne.setObjectName("lineEdit_passwordOne")
        self.gridLayout.addWidget(self.lineEdit_passwordOne, 1, 0, 1, 1)
        self.lineEdit_passwordTwo = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_passwordTwo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwordTwo.setObjectName("lineEdit_passwordTwo")
        self.gridLayout.addWidget(self.lineEdit_passwordTwo, 2, 0, 1, 1)
        self.lineEdit_firstName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.gridLayout.addWidget(self.lineEdit_firstName, 3, 0, 1, 1)
        self.lineEdit_city = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.gridLayout.addWidget(self.lineEdit_city, 5, 0, 1, 1)
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

        '''
        Call a cancelButton() function when "Cancel" button is clicked to perfrom an action
        '''
        self.pushButton_rcancel.clicked.connect(self.cancelButton)

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

        '''
        Call an addButton() function when "Add" button is clicked to perfrom an action

        '''
        self.pushButton_add.clicked.connect(self.addButton)

        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.label_newUserBackground = QtWidgets.QLabel(Dialog_Register)
        self.label_newUserBackground.setGeometry(QtCore.QRect(-84, -98, 851, 701))
        self.label_newUserBackground.setStyleSheet("image: url(:/Resource/background.jpg)")
        self.label_newUserBackground.setText("")
        self.label_newUserBackground.setObjectName("label_newUserBackground")
        self.label_newUserBackground.raise_()
        self.groupBox.raise_()

        self.retranslateUi(Dialog_Register)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Register)

    def retranslateUi(self, Dialog_Register):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Register.setWindowTitle(_translate("Dialog_Register", "Registration"))
        self.groupBox.setTitle(_translate("Dialog_Register", "Register as New User"))
        self.label.setText(_translate("Dialog_Register", " Confirm Password "))
        self.checkBox_agent.setText(_translate("Dialog_Register", " Agent "))
        self.checkBox_officer.setText(_translate("Dialog_Register", " Officer"))
        self.label_firstName.setText(_translate("Dialog_Register", " First Name "))
        self.label_userCity.setText(_translate("Dialog_Register", " City"))
        self.label_rPass.setText(_translate("Dialog_Register", " Password"))
        self.label_lastName.setText(_translate("Dialog_Register", " Last Name"))
        self.label_rUser.setText(_translate("Dialog_Register", " Username "))
        self.label_userType.setText(_translate("Dialog_Register", " Type"))
        self.pushButton_rcancel.setText(_translate("Dialog_Register", "Cancel"))
        self.pushButton_add.setText(_translate("Dialog_Register", "Add"))


import source_rc