import sys
import sqlite3   
import random
import time
from PyQt5 import QtCore, QtGui, QtWidgets      # Import PyQt5 library
from login_UI import Ui_Dialog_Login            # Import the class for Login Dialog from it own seperate file
from officer_UI import Ui_Dialog_oMenu          # Import the class for Officer Dialog from it own seperate file          
from datetime import datetime
from functools import partial
from db_constants import *                      # Needed for findButton() SQL search code

import agents_ui

'''
Class for Dialog Window that displays a list when there more than 4 matches in Officer Q2, Search for Car
'''
class UI_List(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        global REG_LIST
        self.setWindowTitle('List')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Resource/car_icon.png"), QtGui.QIcon.Normal)     
        self.setWindowIcon(icon) 
        self.layout = QtWidgets.QVBoxLayout()
        self.alist = QtWidgets.QListWidget()
        self.label = QtWidgets.QLabel()
        self.label.setFont(QtGui.QFont("Lato", 15))        
        self.layout.addWidget(self.label)
        
    def test(self, regList):
        row = self.alist.currentRow()
        try:
            currentRow = regList[row]
            text = ("Issued: "+str(currentRow[6])+', Expires: '+str(currentRow[7])+', Name: '+str(currentRow[8]).capitalize()+' '+str(currentRow[9]).capitalize())
            self.label.setText(text)    
        except IndexError:
            window = UI_Popup() 
            window.messagebox('Error')
            window.exec_()  
            
'''
Class for Message Box window when an error occurs.
It has a function messagebox() that takes in text as parameter.
This text will be outputed and displayed in the window.
'''
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
        
'''
Super Class for Login UI class premade when converting .ui to .py
'''        
class UI_Login(QtWidgets.QDialog, Ui_Dialog_Login):
    def __init__(self):
        super(UI_Login, self).__init__()
        self.setupUi(self)
        
        self.connection = sqlite3.connect('p1.db') #<---------------- Can't hard code database
        self.cursor = self.connection.cursor()
        
        self.pushButton_cancel.clicked.connect(self.close)  # self.pushButton_cancel.clicked.connect(Dialog_Login.close)
        self.pushButton_login.setDefault(True)
        self.pushButton_login.clicked.connect(self.loginButton)

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
            window = UI_Popup() 
            window.messagebox('Password is missing!')
            window.exec_()  
        elif not username:
            window = UI_Popup() 
            window.messagebox('Username is missing!')
            window.exec_()  
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
                    #Get account type from the user
                    self.cursor.execute('''Select utype FROM users WHERE uid=?''', (username.lower(), ))
                    user_type = self.cursor.fetchone()  
                    
                    if (user_type[0].lower() == 'o'):       #Open new Dialog Window if user type is 'o' for Officer
                        window = UI_oMenu() 
                        window.exec_()      
                        
                    elif (user_type[0].lower() == 'a'):     #Open new Dialog Window if user type is 'a' for Agent
                        agents_ui.start_ui(self.connection, self.cursor, uID)

                else:
                    window = UI_Popup() 
                    window.messagebox('Password is incorrect!')
                    window.exec_()  
                         
        if (valid_user is False):
            window = UI_Popup() 
            window.messagebox('Username is not registered!')
            window.exec_()  
            
'''
Super class for Officer Menu class premade when converting from .ui to py.
'''
class UI_oMenu(QtWidgets.QDialog, Ui_Dialog_oMenu):
    
    def __init__(self):
        REGISTRATION_NUM = 0
        self.connection = sqlite3.connect('po1.db')
        self.cursor = self.connection.cursor()
        
        super(UI_oMenu, self).__init__()
        self.setupUi(self)
    
        self.pushButton_cancel.clicked.connect(self.close)          #"Cancel" button is clicked in first tab, will close the current dialog window but not the main login dialog window 
        self.pushButton_cancel_2.clicked.connect(self.close)        #"Close" button for second tab
        self.pushButton_check.clicked.connect(self.checkButton)     #"Check" button is clicked in first tab, will call checkButton() function
        self.pushButton_issue.clicked.connect(self.issueButton)     #"Issue" button is clicked in first tab, will call issueButton() function
        self.pushButton_find.clicked.connect(self.findButton)       #"Find" button is clicked in second tab, will call findButton() function
        
        self.layoutWidget.setVisible(False)      #Hide registered car info until we can validate user inputed registration number via our database
        self.groupBox_ticket.setVisible(False)   #Hide ticket section until user inputs a valid registration number
        self.pushButton_issue.setVisible(False)  #Hide "Issue" ticket button as well
        self.groupBox.setVisible(False)          #Hide "Results" group box until user inputs a valid string into the provided text boxes
        
        self.tabWidget.currentChanged.connect(self.tabChanged) #When a tab is clicked
    
    '''
    Function runs when tab is changed in Officer Menu Dialog Window
    Reset text boxes to empty and hide certain aspects of UI
    '''
    def tabChanged(self):
        self.layoutWidget.setVisible(False)    
        self.groupBox_ticket.setVisible(False)  
        self.pushButton_issue.setVisible(False)   
        self.lineEdit_registration.setText('')
        self.lineEdit_make_2.setText('')
        self.lineEdit_model_2.setText('')
        self.lineEdit_year_2.setText('')
        self.lineEdit_colour_2.setText('')  
        
    '''
    Function runs when "Check" button is clicked in Officer Menu Dialog Window
    '''
    def checkButton(self):
        global REGISTRATION_NUM #Global var. to pass reg. num to another function issueButton()
        
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
                    REGISTRATION_NUM = int(regNum)  #Modify global var.
                    self.getInfo(int(regNum))       #Call function to display info. when reg. num is in database
                    
            if check is False:
                window = UI_Popup() 
                window.messagebox('Registeration number is not valid!')
                window.exec_() 
                
        else:
            window = UI_Popup() 
            window.messagebox('Invalid input')
            window.exec_()      
    '''
    Function that displays Name,Make,Model,Year,Colour base off reg.num as the parameter.
    '''
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
        #Once info is displayed, UI to issue ticket is now shown to user
        self.layoutWidget.setVisible(True)   
        self.pushButton_issue.setVisible(True) 
        self.groupBox_ticket.setVisible(True) 
    '''
    Function that issues a ticket to person pass in as info. from reg. num parameter.
    By default, if not date is given, the default date is now.
    Ticket number is unique and given after we check if user inputs are valid.
    '''
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
    '''
    Function gets valid user input from issueButton() function
    and inputs the info. in the database.
    '''
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
    Function is called when 'Find' button is clicked.
    Base on 1 or more user inputs we can search the database for a match.
    If there less than 4 matches, we displayed Car info, Plate # and Registeration Info.
    If there more than 4 matches, we display car info of all matches in a scrollable list
    in a new Dialog Window.
    If user clickes on a row, reg. info specific to that car info is displayed.
    Matches mean different vin for same car base on user input.
    Ex. "Ford Focus 2005 Black" is not a unqiue car but the same car can have mutiple 
        unique vin. Each unqiue vin is a match
    '''
    def findButton(self):
        global REG_LIST
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
            #Set empty user inputs from '' to %
            i = 0
            while i < len(alist):
                if alist[i] == '':
                    alist[i] = "%"
                else:
                    i += 1

            make_input = str(alist[0])
            model_input = str(alist[1])
            year_input = str(alist[2])
            colour_input = str(alist[3])

            #Base on other group member SQL code anywhere var. % escapes and is ignored by SQL
            query = "SELECT * FROM vehicles WHERE make LIKE {make} AND model LIKE {model} AND year like {year} AND color LIKE {color}".format(
                make=escape(make_input), model=escape(model_input), year=escape(year_input), color=escape(colour_input))
            self.cursor.execute(query)
            result_list = self.cursor.fetchall()
            
            #Complicated for loops to get 1 match for each unqiue vin # base on most recent reg. date
            #Returns most_recent_reg as the list of all unqiue matches base on the above condition
            vin_list = []
            matching_list = []
            most_recent_reg = []
            for vin in result_list:
                vin_list.append(vin[0])
                self.cursor.execute('''Select plate, regdate, expiry, fname, lname FROM registrations WHERE vin=? ORDER BY regdate DESC''', (vin[0], ))
                reg_list = self.cursor.fetchall()   
                for info in reg_list:
                    matching_list.append(vin + info) 
                most_recent = matching_list.pop(0)
                most_recent_reg.append(most_recent)
                del matching_list[:] 
       
            #Length of the list is less than 4 means there less than 4 matches
            if len(most_recent_reg) <= 4:
                count = 0
                for i in most_recent_reg:
                    count +=1
                #Base on count # which equal # of matches we can add info to the text boxes created in UI.
                if count == 0:
                    self.lineEdit_1.setText('')
                    self.lineEdit_2.setText('')  
                    self.lineEdit_3.setText('')
                    self.lineEdit_4.setText('')
                    self.lineEdit_5.setText('')
                    self.lineEdit_6.setText('')   
                    self.lineEdit_7.setText('')
                    self.lineEdit_8.setText('')                    
                elif count == 1:
                    text1 = ('Found: ' + (str(most_recent_reg[0][1])).capitalize() + ', ' + (str(most_recent_reg[0][2])).capitalize() + ', ' + (str(most_recent_reg[0][3])).capitalize() + ', ' + (str(most_recent_reg[0][4])).capitalize() + ', ' + str(most_recent_reg[0][5]))
                    text2 = ('Active: ' + (str(most_recent_reg[0][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[0][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[0][8])).capitalize() + ' ' + (str(most_recent_reg[0][9])).capitalize())
                    self.lineEdit_1.setText(text1)
                    self.lineEdit_2.setText(text2)
                    self.groupBox.setVisible(True)    
                elif count == 2:
                    text = ('Found: ' + (str(most_recent_reg[0][1])).capitalize() + ', ' + (str(most_recent_reg[0][2])).capitalize() + ', ' + (str(most_recent_reg[0][3])).capitalize() + ', ' + (str(most_recent_reg[0][4])).capitalize() + ', ' + str(most_recent_reg[0][5]))
                    text2 = ('Active: ' + (str(most_recent_reg[0][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[0][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[0][8])).capitalize() + ' ' + (str(most_recent_reg[0][9])).capitalize())
                    self.lineEdit_1.setText(text)
                    self.lineEdit_2.setText(text2)
                    
                    text3 = ('Found: ' + (str(most_recent_reg[1][1])).capitalize() + ', ' + (str(most_recent_reg[1][2])).capitalize() + ', ' + (str(most_recent_reg[1][3])).capitalize() + ', ' + (str(most_recent_reg[1][4])).capitalize() + ', ' + str(most_recent_reg[1][5]))
                    text4 = ('Active: ' + (str(most_recent_reg[1][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[1][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[1][8])).capitalize() + ' ' + (str(most_recent_reg[1][9])).capitalize())                    
                    self.lineEdit_3.setText(text3)
                    self.lineEdit_4.setText(text4)                    
                    self.groupBox.setVisible(True) 
                elif count == 3:
                    text = ('Found: ' + (str(most_recent_reg[0][1])).capitalize() + ', ' + (str(most_recent_reg[0][2])).capitalize() + ', ' + (str(most_recent_reg[0][3])).capitalize() + ', ' + (str(most_recent_reg[0][4])).capitalize() + ', ' + str(most_recent_reg[0][5]))
                    text2 = ('Active: ' + (str(most_recent_reg[0][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[0][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[0][8])).capitalize() + ' ' + (str(most_recent_reg[0][9])).capitalize())
                    self.lineEdit_1.setText(text)
                    self.lineEdit_2.setText(text2)
                    
                    text3 = ('Found: ' + (str(most_recent_reg[1][1])).capitalize() + ', ' + (str(most_recent_reg[1][2])).capitalize() + ', ' + (str(most_recent_reg[1][3])).capitalize() + ', ' + (str(most_recent_reg[1][4])).capitalize() + ', ' + str(most_recent_reg[1][5]))
                    text4 = ('Active: ' + (str(most_recent_reg[1][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[1][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[1][8])).capitalize() + ' ' + (str(most_recent_reg[1][9])).capitalize())                    
                    self.lineEdit_3.setText(text3)
                    self.lineEdit_4.setText(text4)
                    
                    text5 = ('Found: ' + (str(most_recent_reg[2][1])).capitalize() + ', ' + (str(most_recent_reg[2][2])).capitalize() + ', ' + (str(most_recent_reg[2][3])).capitalize() + ', ' + (str(most_recent_reg[2][4])).capitalize() + ', ' + str(most_recent_reg[2][5]))
                    text6 = ('Active: ' + (str(most_recent_reg[2][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[2][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[2][8])).capitalize() + ' ' + (str(most_recent_reg[2][9])).capitalize())                    
                    self.lineEdit_5.setText(text5)
                    self.lineEdit_6.setText(text6)                    
                    self.groupBox.setVisible(True)     
                elif count == 4:
                    text = ('Found: ' + (str(most_recent_reg[0][1])).capitalize() + ', ' + (str(most_recent_reg[0][2])).capitalize() + ', ' + (str(most_recent_reg[0][3])).capitalize() + ', ' + (str(most_recent_reg[0][4])).capitalize() + ', ' + str(most_recent_reg[0][5]))
                    text2 = ('Active: ' + (str(most_recent_reg[0][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[0][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[0][8])).capitalize() + ' ' + (str(most_recent_reg[0][9])).capitalize())
                    self.lineEdit_1.setText(text)
                    self.lineEdit_2.setText(text2)
                    
                    text3 = ('Found: ' + (str(most_recent_reg[1][1])).capitalize() + ', ' + (str(most_recent_reg[1][2])).capitalize() + ', ' + (str(most_recent_reg[1][3])).capitalize() + ', ' + (str(most_recent_reg[1][4])).capitalize() + ', ' + str(most_recent_reg[1][5]))
                    text4 = ('Active: ' + (str(most_recent_reg[1][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[1][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[1][8])).capitalize() + ' ' + (str(most_recent_reg[1][9])).capitalize())                    
                    self.lineEdit_3.setText(text3)
                    self.lineEdit_4.setText(text4)
                    
                    text5 = ('Found: ' + (str(most_recent_reg[2][1])).capitalize() + ', ' + (str(most_recent_reg[2][2])).capitalize() + ', ' + (str(most_recent_reg[2][3])).capitalize() + ', ' + (str(most_recent_reg[2][4])).capitalize() + ', ' + str(most_recent_reg[2][5]))
                    text6 = ('Active: ' + (str(most_recent_reg[2][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[2][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[2][8])).capitalize() + ' ' + (str(most_recent_reg[2][9])).capitalize())                    
                    self.lineEdit_5.setText(text5)
                    self.lineEdit_6.setText(text6)  
                    
                    text7 = ('Found: ' + (str(most_recent_reg[3][1])).capitalize() + ', ' + (str(most_recent_reg[3][2])).capitalize() + ', ' + (str(most_recent_reg[3][3])).capitalize() + ', ' + (str(most_recent_reg[3][4])).capitalize() + ', ' + str(most_recent_reg[3][5]))
                    text8 = ('Active: ' + (str(most_recent_reg[3][6])).capitalize() + ', Expires: ' + (str(most_recent_reg[3][7])).capitalize() + ', Registered by: ' + (str(most_recent_reg[3][8])).capitalize() + ' ' + (str(most_recent_reg[3][9])).capitalize())                    
                    self.lineEdit_7.setText(text7)
                    self.lineEdit_8.setText(text8)                      
                    self.groupBox.setVisible(True)  
            #List of matches is more than 4 so we can call the List dialog window.
            else:
                window = UI_List()

                count = 1
                for item in most_recent_reg:
                    correct_text = str(item[1].capitalize()+', '+str(item[2]).capitalize()+', '+str(item[3]).capitalize()+', '+str(item[4]).capitalize()+', '+str(item[5]))
                    window.alist.insertItem(count,correct_text)
                    count += 1
                    
                window.layout.addWidget(window.alist)
                window.setLayout(window.layout)
                window.alist.clicked.connect(partial(window.test, most_recent_reg))
                
                window.exec_()
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI_Login()
    window.show()
    sys.exit(app.exec_())
