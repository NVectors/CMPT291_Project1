import sys
import sqlite3   
import random
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from test_registration import Ui_Dialog_Register    # Import the class for Registeration Dialog from it own seperate file
from test_login import Ui_Dialog_Login              # Import the class for Login Dialog from it own seperate file
from test_OfficerMenu import Ui_Dialog_oMenu
from datetime import datetime


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
        #Dialog_Register = QtWidgets.QDialog()
        #ui = Ui_Dialog_Register()
        #ui.setupUi(Dialog_Register)
        #Dialog_Register.exec_()
        #Dialog_Register.show()
        
        window = UI_Register() 
        window.exec_()      #Note: exec_() blocks the application flow, show() doe not. exec_() is used for modal dialogs. 

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
            #Username is registered in our Database
            if (username.lower() == uID.lower()): 
                valid_user = True
                #Check if password matches username registered in our Database
                if (password == pID): 
                    self.cursor.execute('''Select utype FROM users WHERE uid=?''', (username, ))
                    user_type = self.cursor.fetchone()  
                    
                    if (user_type[0].lower() == 'o'):
                        window = UI_oMenu() 
                        window.exec_()      
                    #valid_dialog = QtWidgets.QMessageBox()
                    #valid_dialog.setText('User is registered!')
                    #valid_dialog.exec_()
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
        
        if (not (username and password_one and password_two and first_name and last_name and city)) and ((checkBox_Agent is False) and (checkBox_Officer is False)):
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
            self.register(username,password_one,password_two, first_name,last_name,city, checkBox_Agent, checkBox_Officer)  
            
    def register(self,username,password_one,password_two, first_name,last_name,city, checkBox_Agent, checkBox_Officer):
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
                #print (username,password_one,user_type,first_name,last_name,city)
                values = (username,password_one,user_type,first_name,last_name,city)
                self.cursor.execute('INSERT into users VALUES (?,?,?,?,?,?)', values)
                self.connection.commit()
                dialog = QtWidgets.QMessageBox()
                dialog.setText('You are now registered!')
                dialog.exec_()    
                self.close()

class UI_oMenu(QtWidgets.QDialog, Ui_Dialog_oMenu):
    
    def __init__(self):
        REGISTRATION_NUM = 0
        self.connection = sqlite3.connect('p1.db')
        self.cursor = self.connection.cursor()
        
        super(UI_oMenu, self).__init__()
        self.setupUi(self)
    
        self.pushButton_cancel.clicked.connect(self.close)      #"Cancel" buttons will close the current dialog window but not the main login dialog window 
        self.pushButton_cancel_2.clicked.connect(self.close)
        self.pushButton_check.clicked.connect(self.checkButton)
        self.pushButton_issue.clicked.connect(self.issueButton)
        self.pushButton_find.clicked.connect(self.findButton) 
        
        self.layoutWidget.setVisible(False)    #Hide registered car info until we can validate user inputed registration number via our database
        self.groupBox_ticket.setVisible(False)  #Hide ticket section until user inputs a valid registration number
        self.pushButton_issue.setVisible(False) #Hide "Issue" ticket button as well
        self.groupBox.setVisible(False)         #Hide "Results" group box until user inputs a valid string into the provided text boxes
        
        self.tabWidget.currentChanged.connect(self.tabChanged)
    
    def tabChanged(self):
        self.layoutWidget.setVisible(False)    
        self.groupBox_ticket.setVisible(False)  
        self.pushButton_issue.setVisible(False)   
        self.lineEdit_registration.setText('')
        self.lineEdit_make_2.setText('')
        self.lineEdit_model_2.setText('')
        self.lineEdit_year_2.setText('')
        self.lineEdit_colour_2.setText('')        
        
    def checkButton(self):
        global REGISTRATION_NUM
        
        self.layoutWidget.setVisible(False)    
        self.groupBox_ticket.setVisible(False)  
        self.pushButton_issue.setVisible(False)
        self.lineEdit_vDate.setText('')
        self.lineEdit_violation.setText('')
        self.lineEdit_fine.setText('')     
        self.lineEdit_ticNum.setText('')
        
        regNum = self.lineEdit_registration.text()
        if ((regNum) and (regNum).isdigit() ):
            self.cursor.execute('''Select regno FROM registrations''')
            registered_vehicles = self.cursor.fetchall()            
            
            check = False
            for reg in registered_vehicles:
                if (int(regNum) == reg[0]):
                    check = True
                    REGISTRATION_NUM = int(regNum)
                    self.getInfo(int(regNum))
                    
            if check is False:
                window = UI_Popup() 
                window.messagebox('Registeration number is not valid!')
                window.exec_() 
                
        else:
            window = UI_Popup() 
            window.messagebox('Invalid input')
            window.exec_()      
            
    def getInfo(self,regNum):
        self.cursor.execute('''Select vin, fname, lname FROM registrations WHERE regno=?''', (regNum,))
        regInfo = self.cursor.fetchone()
        
        vin = regInfo[0]
        self.cursor.execute('''Select make, model, year, color FROM vehicles WHERE vin=?''', (vin,))
        carInfo = self.cursor.fetchone()      
            
        self.lineEdit_name.setText(regInfo[1].capitalize()+' '+regInfo[2].capitalize())    
        self.lineEdit_make.setText(carInfo[0].capitalize())   
        self.lineEdit_model.setText(carInfo[1].capitalize())
        self.lineEdit_year.setText(str(carInfo[2]))
        self.lineEdit_colour.setText(carInfo[3].capitalize())
        self.layoutWidget.setVisible(True)   
        self.pushButton_issue.setVisible(True) 
        self.groupBox_ticket.setVisible(True) 
        
    def issueButton(self):
        reg = REGISTRATION_NUM
        vDate = self.lineEdit_vDate.text()
        violation = self.lineEdit_violation.text()
        fine_amount = self.lineEdit_fine.text()
            
        if not (violation and fine_amount):
            window = UI_Popup() 
            window.messagebox('Invalid input')
            window.exec_()    
        elif (not violation):
            window = UI_Popup() 
            window.messagebox('Violation is missing')
            window.exec_()          
        elif (not fine_amount):
            window = UI_Popup() 
            window.messagebox('Fine amount is missing')
            window.exec_()                       
        else: #Inputs are given
            if ((not (violation.replace(' ', '').isalpha()) or (not fine_amount.isdigit()))):
                window = UI_Popup() 
                window.messagebox('Invalid input')
                window.exec_()        
            else:
                if (vDate):
                    try:
                        date = time.strptime(vDate,'%Y-%m-%d')
                    except:
                        window = UI_Popup() 
                        window.messagebox('Date format must be "%Y-%m-%d"')
                        window.exec_()    
                else:
                    vDate = datetime.today().strftime('%Y-%m-%d')
                    self.lineEdit_vDate.setText(vDate)                
                self.addTicket(vDate,violation,fine_amount,reg)
                
    def addTicket(self,vDate,violation,fine_amount,reg):
        self.cursor.execute('''Select tno FROM tickets''')
        all_tickets = self.cursor.fetchall()
        list_ticNum = []
        for i in all_tickets:
            list_ticNum.append(i[0])
     
        ticketNum = random.randint(100,200)
        while ticketNum in list_ticNum:
                ticketNum = random.randint(100,200)     
        self.lineEdit_ticNum.setText(str(ticketNum))
        
        values = (ticketNum,reg,fine_amount,violation,vDate)
        self.cursor.execute('INSERT into tickets VALUES (?,?,?,?,?)', values)
        self.connection.commit()        
        
        self.cursor.execute('''Select * FROM tickets WHERE tno=?''', (ticketNum, ))
        user_type = self.cursor.fetchone()          
        
        window = UI_Popup() 
        window.messagebox('Ticket is issued')
        window.exec_()     
        
        
        
        
        
        
        
        '''
        Currently working on taking in 1 or more user inputs and searching the data base with those given values
        
        '''



        '''
        Possible Sol:
        in your gui if the field is left blank then set it to '%';
        then define: query = "SELECT * FROM vehicles WHERE vin LIKE {vin} AND make LIKE {make} AND model LIKE {model} AND year like {year} AND color LIKE {color}".format(vin=vin_input, 
                                                                      make=make_input,
                                                                      model=model_input,
                                                                      year=year_input,
                                                                      color=color_input)

        # Then you can plunk the string query into sursor.execute()
        # The empty values are set to % which is a wild card (just be sure that the % gets surrounded by ' ' in the actual sql statement.





        Sol addapted from 'https://dba.stackexchange.com/questions/122550/search-multiple-values-in-multiple-columns'



        '''

    def findButton(self):
        searchMake = self.lineEdit_make_2.text()
        searchModel = self.lineEdit_model_2.text()
        searchYear = self.lineEdit_year_2.text()
        searchColour = self.lineEdit_colour_2.text()

        if not (searchMake or searchModel or searchYear or searchColour):
            window = UI_Popup()
            window.messagebox('Need atleast one input!')
            window.exec_()
        else:
            alist = [searchMake, searchModel, searchYear, searchColour]
            i = 0
            while i < len(alist):
                if alist[i] == '':
                    alist[i] = "%''%"
                else:
                    i += 1

            print(alist, len(alist), alist[0])

            make_input = str(alist[0])
            model_input = str(alist[1])
            year_input = str(alist[2])
            colour_input = str(alist[3])

            query = "SELECT vin FROM vehicles WHERE make LIKE {make} AND model LIKE {model} AND year like {year} AND color LIKE {color}".format(
                make=escape(make_input), model=escape(model_input), year=escape(year_input), color=escape(colour_input))
            self.cursor.execute(query)
            test = self.cursor.fetchall()
            print(test)

            # self.cursor.execute("SELECT * FROM vehicles WHERE make LIKE ? AND model like ? AND year like ? AND color like ?", (make_input,model_input,year_input,colour_input,))
            # test = self.cursor.fetchall()
            # print(test)

            # self.cursor.execute("SELECT * FROM vehicles WHERE make LIKE ?", ((make_input),))
            # test = self.cursor.fetchall()
            # print(test)

            # if len(removeList) == 4:
            # values = (",".join(str(i) for i in alist))
            # self.cursor.execute('''SELECT vin
            # FROM vehicles v
            # WHERE v.make=?, v.model=?, v.year=?, v.colour=?;''', values[0],values[1],values[2],values[3])
            # test = self.cursor.fetchall()
            # print(test)

            
            
            
            
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI_Login()
    window.show()
    sys.exit(app.exec_())