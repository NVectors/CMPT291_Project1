# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0


from PyQt5 import QtCore, QtGui, QtWidgets
import sys 
import sqlite3
from datetime import date, datetime, timedelta

import uuid

from db_constants import *

class Ui_MainWindow(object):
    def __init__(self):
        self.connection = sqlite3.connect('p1.db')
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
        self.fname_06.setGeometry(QtCore.QRect(20, 10, 113, 20))
        self.fname_06.setObjectName("fname_06")
        self.lname_06 = QtWidgets.QLineEdit(self.tab_03)
        self.lname_06.setGeometry(QtCore.QRect(20, 30, 113, 20))
        self.lname_06.setObjectName("lname_06")
        self.results_06 = QtWidgets.QListWidget(self.tab_03)
        self.results_06.setGeometry(QtCore.QRect(20, 160, 411, 151))
        self.results_06.setObjectName("results_06")
        self.submit_06 = QtWidgets.QPushButton(self.tab_03)
        self.submit_06.setGeometry(QtCore.QRect(150, 30, 56, 17))
        self.submit_06.setObjectName("submit_06")
        self.next_06 = QtWidgets.QPushButton(self.tab_03)
        self.next_06.setGeometry(QtCore.QRect(450, 290, 56, 17))
        self.next_06.setObjectName("next_06")
        self.tabWidget.addTab(self.tab_03, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # References my own functions below
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
        self.next_06.setText(_translate("MainWindow", "Next 5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_03), _translate("MainWindow", "Get a driver abstract"))


    def submitNUM04(self): # pretty much done
        vin_no = self.vin_input.text()
        
        first_curr = self.fname_current.text()
        last_curr = self.lname_current.text()
        
        first_new = self.fname_new.text()
        last_new = self.lname_new.text()
        
        plate_no = self.plate_num.text()
        
        curr_date = date.today()
        new_expiry = new_expiry = date.today() - timedelta(days = -365) # same day as today + 1yr
        
        
        # first and last name of current owner of vehicle to confirm ownership of alleged current owner
        self.cursor.execute("SELECT fname FROM registrations WHERE vin =", vin_no)
        real_first_current = self.cursor.fetchone()
        self.cursor.execute("SELECT lname FROM registrations WHERE vin =", vin_no)
        real_last_current = self.cursor.fetchone()
        
        if (real_first_current == first_curr) and (real_last_current == last_curr):
            # exp date for current registration change
            self.cursor.execute("UPDATE registrations WHERE vin =", vin_no, "SET expiry =", curr_date)
        
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
              
        
        if (ticket_no.isdigit() != True): 
            self.result_5.addItem("Error")
        
        else:
            self.cursor.execute("SELECT amount FROM payments WHERE tno =?", (ticket_no,)) 
            amount_remaining = self.cursor.fetchone()  # For some reason, this is returning a NoneType now, ohhhh what did i change...
            if(int(input_amount) > int(amount_remaining)): #tno must be a number and input amount must not exceed amount due (cannot overpay)
                self.result_5.addItem("Error")
                
            new_amount = int(amount_remaining) - int(input_amount) # Finds new amount owed
            self.cursor.execute("UPDATE payments WHERE tno =", ticket_no, "SET amount =", new_amount)
            connection.commit()
            
            
            #set pdate to current date            
            curr_date = date.today()
            self.cursor.execute("UPDATE payments WHERE tno =", ticket_no," SET pdate = ",curr_date)
            connection.commit()
            
    def submitNUM06(self): # abondoned to the wilds 
        # NOTE, next button on the ui is a remenent of something I was going to use, you can completely discard it, the last requirement to 
        # see more should be satisfied as at least 5 should be visable, to which point a scroll wheel will appear, to assist in viewing
        # further tickets (if they exist)
        
        first = self.fname_06.text()
        last = self.lname_06.text()
        curr_date = date.today()
        
        self.cursor.execute("SELECT regno FROM registrations WHERE fname =", first," AND lname =", last)
        regno = self.cursor.fetchone()
        
        #self.cursor.execute("SELECT ") # number of tickets
        #num_tickets = 
        #self.cursor.execute("SELECT ") # number of demerit notices
        #num_notices = 
        
        self.cursor.execute("SELECT points FROM demeritNotices WHERE demeritNotices.fname =",first,"AND demeritNotices.lname =", last) # number of demerit points from all time
        points_all = self.cursor.fetchone()
        #self.cursor.execute("SELECT points FROM demeritNotices WHERE fname =",first,"AND lname =", last, "AND ddate >") # number of demerit points from last 2 years
        #points_two = self.cursor.fetchone()
        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
