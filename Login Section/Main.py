from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)
import sqlite3
from Registeration_Dialog import \
    Ui_Dialog_Register  # Import the class for Registeration Dialog from it own seperate file


class Ui_Dialog_Login(object):
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

    '''
    "New User" button has been clicked and newUserButton() function is called to open a new window.
    The new window get priority (modal is on) and is now the focus for the user.
    Must click "Cancel" or close the window to get back to Login Screen
    '''

    def NewUserButton(self):
        Dialog_Register = QtWidgets.QDialog()
        ui = Ui_Dialog_Register()
        ui.setupUi(Dialog_Register)
        Dialog_Register.exec_()
        Dialog_Register.show()

    '''
    "Login" button has been clicked and loginlButton() function is called to check user inputs.
    Get the values from Username and Password typed by the user and check in our database.
    If it is in our database, we can open a new window 
    else we create a pop screen saying "Username or Password incorrect or not registered".
    We can check these conditions when comparing it to our database.
    '''

    def loginButton(self):
        username = self.lineEdit_Username.text()
        password = self.lineEdit_Password.text()

        if (not username) & (not password):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Type in Username and Password!')
            error_dialog.exec_()
        elif not password:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Password Missing!')
            error_dialog.exec_()
        elif not username:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Username Missing!')
            error_dialog.exec_()
        else:
            self.validity(username, password)

    def validity(self, username, password):
        self.cursor.execute('''Select uid, pwd FROM users ''')
        registered_users = self.cursor.fetchall()

        for info in registered_users:
            uID = info[0]
            pID = info[1]

            # Username is registered in our Database
            if (username.lower() == uID.lower()):
                if (password == pID):
                    valid_dialog = QtWidgets.QMessageBox()
                    valid_dialog.setText('User is registered!')
                    valid_dialog.exec_()
                else:
                    error_dialog = QtWidgets.QMessageBox()
                    error_dialog.setText('Password is Incorrect!')
                    error_dialog.exec_()
            # Password is registered in our Database
            elif (password == pID):
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setText('Username is not registered!')
                error_dialog.exec_()

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
        self.lineEdit_Username = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.gridLayout.addWidget(self.lineEdit_Username, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Password.setText("")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.gridLayout_2.addWidget(self.lineEdit_Password, 0, 1, 1, 1)
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

        '''
        Call a cancelButton() function when "Cancel" button is clicked to perfrom an action

        '''
        self.pushButton_cancel.clicked.connect(
            self.cancelButton)  # self.pushButton_cancel.clicked.connect(Dialog_Login.close)

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

        '''
        Call a newUserButton() function when "New User" button is clicked to perform an action

        '''
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

        '''
        Call a newUserButton() function when "New User" button is clicked to perform an action

        '''
        self.pushButton_login.clicked.connect(self.loginButton)

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
