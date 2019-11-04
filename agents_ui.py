# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agents.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import agents_backend


def start_ui(connection, cursor, uid):
    import sys
    usr = agents_backend.agent(connection, cursor, uid)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(usr)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

class Ui_MainWindow(object):
    def __init__(self, usr):
        self.usr =usr
        self.cursor = self.connection.cursor()      



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 389)
        MainWindow.setStyleSheet("background-color: rgb(226, 227, 219);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(:/Resource/background.jpg);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_01 = QtWidgets.QWidget()
        self.tab_01.setObjectName("tab_01")
        self.vin_input = QtWidgets.QLineEdit(self.tab_01)
        self.vin_input.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.vin_input.setObjectName("vin_input")
        self.fname_current = QtWidgets.QLineEdit(self.tab_01)
        self.fname_current.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.fname_current.setObjectName("fname_current")
        self.lname_current = QtWidgets.QLineEdit(self.tab_01)
        self.lname_current.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lname_current.setObjectName("lname_current")
        self.fname_new = QtWidgets.QLineEdit(self.tab_01)
        self.fname_new.setGeometry(QtCore.QRect(140, 60, 113, 20))
        self.fname_new.setObjectName("fname_new")
        self.lname_new = QtWidgets.QLineEdit(self.tab_01)
        self.lname_new.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.lname_new.setObjectName("lname_new")
        self.label = QtWidgets.QLabel(self.tab_01)
        self.label.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_01)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 121, 16))
        self.label_2.setObjectName("label_2")
        self.plate_num = QtWidgets.QLineEdit(self.tab_01)
        self.plate_num.setGeometry(QtCore.QRect(10, 120, 113, 20))
        self.plate_num.setObjectName("plate_num")
        self.submit_4 = QtWidgets.QPushButton(self.tab_01)
        self.submit_4.setGeometry(QtCore.QRect(10, 160, 56, 17))
        self.submit_4.setObjectName("submit_4")
        self.tabWidget.addTab(self.tab_01, "")
        self.tab_02 = QtWidgets.QWidget()
        self.tab_02.setObjectName("tab_02")
        self.ticket_num = QtWidgets.QLineEdit(self.tab_02)
        self.ticket_num.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.ticket_num.setObjectName("ticket_num")
        self.amount = QtWidgets.QLineEdit(self.tab_02)
        self.amount.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.amount.setObjectName("amount")
        self.submit_5 = QtWidgets.QPushButton(self.tab_02)
        self.submit_5.setGeometry(QtCore.QRect(10, 290, 56, 17))
        self.submit_5.setObjectName("submit_5")
        self.result_5 = QtWidgets.QListWidget(self.tab_02)
        self.result_5.setGeometry(QtCore.QRect(80, 210, 351, 101))
        self.result_5.setObjectName("result_5")
        self.tabWidget.addTab(self.tab_02, "")
        self.tab_03 = QtWidgets.QWidget()
        self.tab_03.setObjectName("tab_03")
        self.fname_06 = QtWidgets.QLineEdit(self.tab_03)
        self.fname_06.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.fname_06.setObjectName("fname_06")
        self.lname_06 = QtWidgets.QLineEdit(self.tab_03)
        self.lname_06.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self.lname_06.setObjectName("lname_06")
        self.results_06 = QtWidgets.QListWidget(self.tab_03)
        self.results_06.setGeometry(QtCore.QRect(20, 160, 411, 151))
        self.results_06.setObjectName("results_06")
        self.submit_06 = QtWidgets.QPushButton(self.tab_03)
        self.submit_06.setGeometry(QtCore.QRect(400, 56, 56, 21))
        self.submit_06.setObjectName("submit_06")
        self.abstract_06 = QtWidgets.QListWidget(self.tab_03)
        self.abstract_06.setGeometry(QtCore.QRect(20, 90, 411, 61))
        self.abstract_06.setObjectName("abstract_06")
        self.driver_abstract_fname = QtWidgets.QLineEdit(self.tab_03)
        self.driver_abstract_fname.setGeometry(QtCore.QRect(130, 10, 171, 31))
        self.driver_abstract_fname.setObjectName("driver_abstract_fname")
        self.driver_abstract_lname = QtWidgets.QLineEdit(self.tab_03)
        self.driver_abstract_lname.setGeometry(QtCore.QRect(130, 50, 171, 31))
        self.driver_abstract_lname.setObjectName("driver_abstract_lname")
        self.tabWidget.addTab(self.tab_03, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 91, 19))
        self.label_5.setObjectName("label_5")
        self.reg_birth_fname = QtWidgets.QLineEdit(self.tab_6)
        self.reg_birth_fname.setGeometry(QtCore.QRect(110, 20, 113, 36))
        self.reg_birth_fname.setObjectName("reg_birth_fname")
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 81, 19))
        self.label_6.setObjectName("label_6")
        self.reg_birth_lname = QtWidgets.QLineEdit(self.tab_6)
        self.reg_birth_lname.setGeometry(QtCore.QRect(110, 80, 113, 36))
        self.reg_birth_lname.setObjectName("reg_birth_lname")
        self.reg_birth_gender = QtWidgets.QComboBox(self.tab_6)
        self.reg_birth_gender.setGeometry(QtCore.QRect(110, 140, 126, 37))
        self.reg_birth_gender.setObjectName("reg_birth_gender")
        self.reg_birth_gender.addItem("")
        self.reg_birth_gender.addItem("")
        self.reg_birth_gender.addItem("")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(20, 150, 67, 19))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_6)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 81, 19))
        self.label_8.setObjectName("label_8")
        self.reg_birth_date = QtWidgets.QDateEdit(self.tab_6)
        self.reg_birth_date.setGeometry(QtCore.QRect(110, 190, 171, 42))
        self.reg_birth_date.setObjectName("reg_birth_date")
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(20, 250, 81, 19))
        self.label_9.setObjectName("label_9")
        self.reg_birth_place = QtWidgets.QLineEdit(self.tab_6)
        self.reg_birth_place.setGeometry(QtCore.QRect(110, 240, 121, 36))
        self.reg_birth_place.setObjectName("reg_birth_place")
        self.label_10 = QtWidgets.QLabel(self.tab_6)
        self.label_10.setGeometry(QtCore.QRect(240, 30, 161, 19))
        self.label_10.setObjectName("label_10")
        self.reg_birth_mfname = QtWidgets.QLineEdit(self.tab_6)
        self.reg_birth_mfname.setGeometry(QtCore.QRect(390, 20, 113, 36))
        self.reg_birth_mfname.setObjectName("reg_birth_mfname")
        self.label_11 = QtWidgets.QLabel(self.tab_6)
        self.label_11.setGeometry(QtCore.QRect(240, 90, 141, 19))
        self.label_11.setObjectName("label_11")
        self.reg_birth_mlname = QtWidgets.QLineEdit(self.tab_6)
        self.reg_birth_mlname.setGeometry(QtCore.QRect(390, 80, 113, 36))
        self.reg_birth_mlname.setObjectName("reg_birth_mlname")
        self.label_12 = QtWidgets.QLabel(self.tab_6)
        self.label_12.setGeometry(QtCore.QRect(250, 150, 141, 19))
        self.label_12.setObjectName("label_12")
        self.reg_birth_ffname = QtWidgets.QLineEdit(self.tab_6)
        self.reg_birth_ffname.setGeometry(QtCore.QRect(390, 140, 113, 36))
        self.reg_birth_ffname.setObjectName("reg_birth_ffname")
        self.label_13 = QtWidgets.QLabel(self.tab_6)
        self.label_13.setGeometry(QtCore.QRect(290, 200, 131, 19))
        self.label_13.setObjectName("label_13")
        self.reg_birth_flname = QtWidgets.QLineEdit(self.tab_6)
        self.reg_birth_flname.setGeometry(QtCore.QRect(420, 190, 91, 36))
        self.reg_birth_flname.setObjectName("reg_birth_flname")
        self.pushButton = QtWidgets.QPushButton(self.tab_6)
        self.pushButton.setGeometry(QtCore.QRect(410, 240, 104, 36))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.widget, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.pushButton.clicked.connect(MainWindow.driver_abstract_search)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # References functions 4 - 6
        # 04
        self.submit_4.clicked.connect(self.submitNUM04)    
        
        # 05
        self.submit_5.clicked.connect(self.submitNUM05)    
        
        # 06
        self.submit_06.clicked.connect(self.submitNUM06)        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vin_input.setText(_translate("MainWindow", "Vin of Car"))
        self.fname_current.setText(_translate("MainWindow", "First Name"))
        self.lname_current.setText(_translate("MainWindow", "Last Name"))
        self.fname_new.setText(_translate("MainWindow", "First Name"))
        self.lname_new.setText(_translate("MainWindow", "Last Name"))
        self.label.setText(_translate("MainWindow", "Current Owner Information"))
        self.label_2.setText(_translate("MainWindow", "New Owner Information"))
        self.plate_num.setText(_translate("MainWindow", "Plate Number for New Reg."))
        self.submit_4.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_01), _translate("MainWindow", "Process a bill of sale"))
        self.ticket_num.setText(_translate("MainWindow", "Ticket No."))
        self.amount.setText(_translate("MainWindow", "Amount"))
        self.submit_5.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_02), _translate("MainWindow", "Process a payment"))
        self.fname_06.setText(_translate("MainWindow", "First Name"))
        self.lname_06.setText(_translate("MainWindow", "Last Name"))
        self.submit_06.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_03), _translate("MainWindow", "Get a driver abstract"))
        self.label_5.setText(_translate("MainWindow", "First Name"))
        self.label_6.setText(_translate("MainWindow", "Last Name"))
        self.reg_birth_gender.setItemText(0, _translate("MainWindow", "select..."))
        self.reg_birth_gender.setItemText(1, _translate("MainWindow", "Male"))
        self.reg_birth_gender.setItemText(2, _translate("MainWindow", "Female"))
        self.label_7.setText(_translate("MainWindow", "Gender"))
        self.label_8.setText(_translate("MainWindow", "Birth date"))
        self.label_9.setText(_translate("MainWindow", "Birth Place"))
        self.label_10.setText(_translate("MainWindow", "Mother\'s First Name"))
        self.label_11.setText(_translate("MainWindow", "Mother\'s Last name"))
        self.label_12.setText(_translate("MainWindow", "Father\'s First Name"))
        self.label_13.setText(_translate("MainWindow", "Father\'s Last name"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Register Birth"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Register Marriage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Renew Vehicle Registration"))


    def submitNUM04(self): # pretty much done
        vin_no = self.vin_input.text()
        #vin_no = (''.join(vin_no))
        one = True
        
        first_curr = (self.fname_current.text()),
        last_curr = (self.lname_current.text()),
        
        first_new = self.fname_new.text(),
        last_new = (self.lname_new.text()),
        
        plate_no = self.plate_num.text()
        two = True
        
        three = False # checks if plate and vin if they are digits
        
        curr_date = (date.today()),
        new_expiry = new_expiry = date.today() - timedelta(days = -365) # same day as today + 1yr
        new_expiry = (new_expiry),
        
        # check if input box empty/full of spaces 
        if not vin_no or vin_no.isspace() == True:  # checks if vin is empty 
            one = False
        if not plate_no or plate_no.isspace() == True:  # checks if plate_no is empty
            two = False           
                
        
        # first and last name of current owner of vehicle to confirm ownership of alleged current owner
        try:
            stuff = vin_no, curr_date
            self.cursor.execute("SELECT fname FROM registrations WHERE vin =? AND expiry >?", stuff) 
            real_first_current = self.cursor.fetchone()
            self.cursor.execute("SELECT lname FROM registrations WHERE vin =? AND expiry >?", stuff) 
            real_last_current = self.cursor.fetchone()
            name = False
        except:
            return 0
        

        if ((real_first_current == first_curr) and (real_last_current == last_curr)):
            name = True # checks to see if what's in the box matches the real name based on the vin        
                
        if (one == False and two == False and name == True):
            # exp date for current registration change
            self.cursor.execute("UPDATE registrations WHERE vin =? SET expiry =?", stuff)
        
            # new registration for new owner
            registration_entry = REGISTRATIONS_ENTRY.format(regno = uuid.uuid1().int, regdate = curr_date, expiry = new_expiry, plate = plate_no, vin = vin_no,
                                                        fname = first_new, lname = last_new)
            
            
            self.cursor.execute("INSERT INTO registrations VALUES{}".format(registration_entry))
            connection.commit()
        else: # transfer cannot be made, no error message required since not specified in the system functionalities description
            pass 
                          
                                       
                                       
    def submitNUM05(self): # almost done
        ticket_no = self.ticket_num.text()
        input_amount = self.amount.text()
              
        
        if (ticket_no.isdigit() != True or not ticket_no or ticket_no.isspace() == True): # checks for number input and if ticket_no is left blank
            self.result_5.addItem("Error")
        
        else:
            self.cursor.execute("SELECT amount FROM payments WHERE tno =?", (ticket_no,)) 
            amount_remaining = self.cursor.fetchone()
            if(int(input_amount) > int(amount_remaining)): #tno must be a number and input amount must not exceed amount due (cannot overpay)
                self.result_5.addItem("Error")
                
            new_amount = int(amount_remaining) - int(input_amount) # Finds new amount owed
            self.cursor.execute("UPDATE payments WHERE tno =", ticket_no, "SET amount =", new_amount)
            connection.commit()
            
            
            #set pdate to current date            
            curr_date = date.today()
            self.cursor.execute("UPDATE payments WHERE tno =", ticket_no," SET pdate = ",curr_date)
            connection.commit()
            
    def submitNUM06(self): 
        # The last requirement to see more should be satisfied as at least 5
        # should be visable, to which point a scroll wheel will appear, to assist in viewing
        # further tickets (if they exist)
        
        first = self.fname_06.text()
        last = self.lname_06.text()
        curr_date = date.today()
        
        val01 = (first, last)
        self.cursor.execute("SELECT regno FROM registrations WHERE fname =? AND lname =?", val01)
        regno = self.cursor.fetchone()
        
        self.cursor.execute("SELECT regno FROM registrations WHERE fname =? AND lname=?", val01) # number of tickets
        regno = self.cursor.fetchone()
        self.cursor.execute("SELECT COUNT(tno) FROM tickets WHERE regno=?", (regno,)) # number of tickets
        num_tickets = self.cursor.fetchone()
        
        self.cursor.execute("SELECT COUNT(DISTINCT desc) FROM demeritNotices WHERE fname=? AND lname =?", val01) # number of demerit notices
        num_notices = self.cursor.fetchone()        
        
        self.cursor.execute("SELECT points FROM demeritNotices WHERE demeritNotices.fname =? AND demeritNotices.lname =?", val01) # number of demerit points from all time
        points_all = self.cursor.fetchone()
        
        val02 = (first, last, curr_date)
        self.cursor.execute("SELECT points FROM demeritNotices WHERE demeritNotices.fname =? AND demeritNotices.lname =? AND ddate >?", val02) # number of demerit points from all time
        points2y = self.cursor.fetchone()
        
        self.results_06.addItem("Number of tickets, Number of Notices, Total Points, Points (Last 2y)")
        list = str(num_tickets)," ", str(num_notices)," ", str(points_all), " ", str(points2y)
        list = "".join(list)
        self.results_06.addItem(list)    
        
 
