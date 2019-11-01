import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from test_registration import Ui_Dialog_Register  # Import the class for Registeration Dialog from it own seperate file
from test_login import Ui_Dialog_Login  # Import the class for Login Dialog from it own seperate file
from test_OfficerMenu import Ui_Dialog_oMenu


class UI_Popup(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Error')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Resource/search_icon.png"), QtGui.QIcon.Normal)
        self.setWindowIcon(icon)

    def messagebox(self, text):
        self.setText(text)


class UI_Login(QtWidgets.QDialog, Ui_Dialog_Login):
    def __init__(self):
        super(UI_Login, self).__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect('p1.db')
        self.cursor = self.connection.cursor()

        self.pushButton_cancel.clicked.connect(self.close)  # self.pushButton_cancel.clicked.connect(Dialog_Login.close)
        self.pushButton_newUser.clicked.connect(self.NewUserButton)
        self.pushButton_login.clicked.connect(self.loginButton)

    '''
    "New User" button has been clicked and newUserButton() function is called to open a new dialog window.
    The new window gets priority (modal is on) and is now the focus for the user.
    Must click "Cancel" button to get back to Login Screen
    '''

    def NewUserButton(self):
        # Dialog_Register = QtWidgets.QDialog()
        # ui = Ui_Dialog_Register()
        # ui.setupUi(Dialog_Register)
        # Dialog_Register.exec_()
        # Dialog_Register.show()

        window = UI_Register()
        window.exec_()  # Note: exec_() blocks the application flow, show() doe not. exec_() is used for modal dialogs.

    '''
    "Login" button has been clicked and loginButton() function is called to check user inputs.
    Get the values from Username and Password typed by the user.
    Check to make sure both have been given by user. If both are present, call validity() function. 
    '''

    def loginButton(self):
        username = self.lineEdit_Username.text()
        password = self.lineEdit_Password.text()

        if (not username) & (not password):
            window = UI_Popup()
            window.messagebox('Type in Username and Password!')
            window.exec_()

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

    '''
    Validty() function gets username, password as parameters from loginButton() function.
    Check if username in our database.
    If it is in our database, we can check if password is valid.
    If password is valid we open a new window, 
    else we create a popup screen saying "Password is Incorrect".
    '''

    def validity(self, username, password):
        self.cursor.execute('''Select uid, pwd FROM users ''')
        registered_users = self.cursor.fetchall()
        valid_user = False

        for info in registered_users:
            uID = info[0]
            pID = info[1]
            # Username is registered in our Database
            if (username.lower() == uID.lower()):
                valid_user = True
                # Check if password matches username registered in our Database
                if (password == pID):
                    self.cursor.execute('''Select utype FROM users WHERE uid=?''', (username,))
                    user_type = self.cursor.fetchone()

                    if (user_type[0].lower() == 'o'):
                        window = UI_oMenu()
                        window.exec_()
                        # valid_dialog = QtWidgets.QMessageBox()
                    # valid_dialog.setText('User is registered!')
                    # valid_dialog.exec_()
                else:
                    error_dialog = QtWidgets.QMessageBox()
                    error_dialog.setText('Password is Incorrect!')
                    error_dialog.exec_()

        if (valid_user is False):
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Username is not registered!')
            error_dialog.exec_()


class UI_Register(QtWidgets.QDialog, Ui_Dialog_Register):
    def __init__(self):
        self.connection = sqlite3.connect('p1.db')
        self.cursor = self.connection.cursor()

        super(UI_Register, self).__init__()
        self.setupUi(self)

        self.pushButton_rcancel.clicked.connect(self.close)

        self.pushButton_add.clicked.connect(self.addButton)

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


class UI_oMenu(QtWidgets.QDialog, Ui_Dialog_oMenu):
    def __init__(self):
        self.connection = sqlite3.connect('p1.db')
        self.cursor = self.connection.cursor()
        super(UI_oMenu, self).__init__()
        self.setupUi(self)

        # Added code to disable Close and Help button, won't work if added directly to the Class itself
        # self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        # self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        # self.pushButton_check.clicked.connect(self.close)
        self.pushButton_cancel.clicked.connect(
            self.close)  # "Cancel" buttons will close the current dialog window but not the main login dialog window
        self.pushButton_cancel_2.clicked.connect(self.close)

        # self.layoutWidget1.setVisible(False)    #Hide registered car info until we can validate user inputed registration number via our database
        # self.groupBox_ticket.setVisible(False)  #Hide ticket section until user inputs a valid registration number
        # self.pushButton_issue.setVisible(False) #Hide "Issue" ticket button as well
        # self.groupBox.setVisible(False)         #Hide "Results" group box until user inputs a valid string into the provided text boxes


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI_Login()
    window.show()
    sys.exit(app.exec_())