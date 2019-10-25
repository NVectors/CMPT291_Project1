"""
CMPUT 291 - Group Mini Project 1

This .py file contains the functions that clears and initialize the database required.
The structure, variable names and tables are provided to us.
"""

import sqlite3
import time

'''
Connect(path) is required since main function will be in a separate file.
Establish a connection to the database pass on as a parameter.
Return the connection and a cursor 
'''
def connect(path):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    
    connection.commit()
    return connection, cursor


'''
Drop all the tables in the given database
'''
def drop_tables(connection, cursor):
    drop_query = '''
                        drop table if exists demeritNotices;
                        drop table if exists tickets;
                        drop table if exists registrations;
                        drop table if exists vehicles;
                        drop table if exists marriages;
                        drop table if exists births;
                        drop table if exists persons;
                        drop table if exists payments;
                        drop table if exists users;
                 '''
    cursor.executescript(drop_query)
    
    connection.commit()
    return

def define_tables(connection, cursor):
    persons_query = '''
                        CREATE TABLE persons (
                                    fname	CHAR(12),
                                    lname	CHAR(12),
                                    bDATE	DATE,
                                    bplace	CHAR(20), 
                                    address	CHAR(30),
                                    phone	CHAR(12),
                                    PRIMARY KEY (fname, lname)
                                    );
                    '''

    births_query = '''
                        CREATE TABLE births (
                                    regno	INT,
                                    fname	CHAR(12),
                                    lname	CHAR(12),
                                    regDATE	DATE,
                                    regplace	CHAR(20),
                                    gender	CHAR(1),
                                    f_fname	CHAR(12),
                                    f_lname	CHAR(12),
                                    m_fname	CHAR(12),
                                    m_lname	CHAR(12),
                                    PRIMARY KEY (regno),
                                    FOREIGN KEY (fname,lname) references persons,
                                    FOREIGN KEY (f_fname,f_lname) references persons,
                                    FOREIGN KEY (m_fname,m_lname) references persons
                                    );
                    '''

    marriages_query = '''
                    CREATE TABLE marriages (
                                    regno	INT,
                                    regDATE	DATE,
                                    regplace	CHAR(20),
                                    p1_fname	CHAR(12),
                                    p1_lname	CHAR(12),
                                    p2_fname	CHAR(12),
                                    p2_lname	CHAR(12),
                                    PRIMARY KEY (regno),
                                    FOREIGN KEY (p1_fname,p1_lname) references persons,
                                    FOREIGN KEY (p2_fname,p2_lname) references persons
                                    );
                      '''
    vehicles_query = '''
                    CREATE TABLE vehicles (
                                    vin		CHAR(5),
                                    make	CHAR(10),
                                    model	CHAR(10),
                                    year	INT,
                                    color	CHAR(10),
                                    PRIMARY KEY (vin)
                                    );
                      '''
    registrations_query = '''
                    CREATE TABLE registrations (
                                    regno	INT,
                                    regDATE	DATE,
                                    expiry	DATE,
                                    plate	CHAR(7),
                                    vin		CHAR(5), 
                                    fname	CHAR(12),
                                    lname	CHAR(12),
                                    primary key (regno),
                                    foreign key (vin) references vehicles,
                                    foreign key (fname,lname) references persons
                                    );
                          '''
    tickets_query = '''
                    CREATE TABLE tickets (
                                    tno		INT,
                                    regno	INT,
                                    fine	INT,
                                    violation	text,
                                    vDATE	DATE,
                                    primary key (tno),
                                    foreign key (regno) references registrations
                                    );
                    '''
    demeritNotices_query = '''
                    CREATE TABLE demeritNotices (
                                    dDATE	DATE, 
                                    fname	CHAR(12), 
                                    lname	CHAR(12), 
                                    poINTs	INT, 
                                    desc	text,
                                    primary key (dDATE,fname,lname),
                                    foreign key (fname,lname) references persons
                                    );
                          '''
    payments_query = '''
                    CREATE TABLE payments (
                                    tno		INT,
                                    pDATE	DATE,
                                    amount	INT,
                                    primary key (tno, pDATE),
                                    foreign key (tno) references tickets
                                    );
                    '''
    users_query = '''
                    CREATE TABLE users (
                                    uid		CHAR(8),
                                    pwd		CHAR(8),
                                    utype	CHAR(1),	-- 'a' for agents, 'o' for officers
                                    fname	CHAR(12),
                                    lname	CHAR(12), 
                                    city	CHAR(15),
                                    primary key(uid),
                                    foreign key (fname,lname) references persons
                                    );
                  '''

    cursor.execute(persons_query)
    cursor.execute(births_query)
    cursor.execute(registrations_query)
    cursor.execute(marriages_query)
    cursor.execute(vehicles_query)
    cursor.execute(registrations_query)
    cursor.execute(tickets_query)
    cursor.execute(demeritNotices_query)
    cursor.execute(payments_query)
    cursor.execute(users_query)

    connection.commit()
    return


def insert_data(connection, cursor):
    # Insert VALUES into Data

    cursor.execute(insert_persons)
    cursor.execute(insert_births)
    cursor.execute(insert_marriages)
    cursor.execute(insert_vehicles)
    cursor.execute(insert_registrations)
    cursor.execute(insert_tickets)
    cursor.execute(insert_demeritNotices)
    cursor.execute(insert_payments)
    cursor.execute(insert_users)

    connection.commit()
    return

if __name__ == "__main__":
    main()
