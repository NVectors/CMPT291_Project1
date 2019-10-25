"""
CMPUT 291 F19 - Group Mini Project 1

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
                                    bdate	DATE,
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
                                    regdate	DATE,
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
                                    regdate	DATE,
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
                                    regdate	DATE,
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
                                    vdate	DATE,
                                    primary key (tno),
                                    foreign key (regno) references registrations
                                    );
                    '''
    demeritNotices_query = '''
                    CREATE TABLE demeritNotices (
                                    ddate	DATE, 
                                    fname	CHAR(12), 
                                    lname	CHAR(12), 
                                    points	INT, 
                                    desc	text,
                                    primary key (ddate,fname,lname),
                                    foreign key (fname,lname) references persons
                                    );
                          '''
    payments_query = '''
                    CREATE TABLE payments (
                                    tno		INT,
                                    pdate	DATE,
                                    amount	INT,
                                    primary key (tno, pdate),
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
    insert_persons = ''' insert into persons values
                            ('Trayvon', 'Fox', '1892-07-17', 'PeaceRiver,AB', '133 Street PR', '443-449-9999'),\
                            ('Lillian', 'Bounds', '1899-02-15', 'Spalding, Idaho', 'Los Angeles, US', '213-555-5556'),\
                            ('Adam', 'Rafiei', "1900-01-02", "Shiraz,Iran", "Tehran,Iran", "916-331-3311"),\
                            ('James', 'Smith', '1900-08-08', 'Calgary,AB', '43,43Ave', '720-000-0001'),\
                            ('Walt', 'Disney', '1901-12-05', 'Chicago, US', 'Los Angeles, US', '213-555-5555'),\
                            ('Mary', 'Brown', '1905-11-15', 'Nordegg,AB', '22,67Ave', '776-655-9955'),\
                            ('John', 'Truyens', '1907-05-15', 'Flanders, Belgium', 'Beverly Hills, Los Angeles, US', '213-555-5558'),\
                            ('Linda', 'Smith', '1908-02-26', 'Ohaton,AB', '43,43Ave', '680-099-9943'),\
                            ('Minnie', 'Mouse', '1928-01-05', 'Disneyland', 'Anaheim, US', '714-555-5552'),\
                            ('Mickey', 'Mouse', '1928-01-05', 'Disneyland', 'Anaheim, US', '714-555-5551'),\
                            ("Mary", "Smith", "1950-11-08", "Calgary,AB", "11Ave,1st", "604-555-2244"),\
                            ("Aunt", "Smith", "1951-12-08", "Calgary,AB", "11Ave,1st", "888-555-2244"),\
                            ("Dave", "Fox", "1950-03-29", "Calgary,AB", "11Ave,1st", "664-110-8763"),\
                            ("Uncle", "Fox", "1951-03-29", "Calgary,AB", "11Ave,1st", "780-110-8743"),\
                            ('Michael', 'Fox', '1981-06-09', 'Edmonton, AB', 'Manhattan, New York, US', '212-111-1111'),\
                            ('Cousin1', 'Fox', '1981-06-09', 'Edmonton, AB', 'Manhattan, New York, US', '666-111-1111'),\
                            ('Cousin2', 'Fox', '1991-02-06', 'Edmonton, AB', 'Manhattan, New York, US', '666-111-1111'),\
                            ("Megan", "Fox", "1982-06-09", "Calgary,AB", "12Ave,101st", "780-460-1134"),\
                            ("Fatima", "Fox", "1992-06-09", "Calgary,AB", "12Ave,101st", "444-470-7734"),
                            ("Lisa", "Bounds", "1999-04-10", "Spalding,Idaho", "Moscow,101st", "604-420-1234"),
                            ('Diane', 'Wong', '1973-04-04', 'England', 'London,Hackney', '766-664-6678'),\
                            ('Davood', 'Rafiei', date('now', '-21 years'), 'Iran', '100 Lovely Street,Edmonton,AB', '780-111-2222'),\
                            ('Linda', 'Fox', '1991-02-04', 'England', 'London', '344-447-7755'),\
                            ('Tammy', 'Fox', '1991-02-04', 'England', 'Manchester', '344-111-2345'),
                            ('Henry', 'Wong', '1993-04-04', 'Canada', 'Alert', '566-664-6678'),
                            ('Michael', 'Parenti', '1991-02-04', 'England', 'London', '344-447-7755'); '''
    insert_users = '''insert into users values
                        ('jstainer0','2ZU0pfEWz6v','a','Michael','Fox','Edmonton'),
                        ('zgegg1','P62JfnX','o','Lillian', 'Bounds','Calgary'),
                        ('msemper2','gorLa6','a','Adam','Rafiei','Red Deer'),
                        ('cesselin3','GHRiSvn','o','Linda','Smith','Jasper');'''

    cursor.execute(insert_persons)
    #cursor.execute(insert_births)
    #cursor.execute(insert_marriages)
    #cursor.execute(insert_vehicles)
    #cursor.execute(insert_registrations)
    #cursor.execute(insert_tickets)
    #cursor.execute(insert_demeritNotices)
    #cursor.execute(insert_payments)
    cursor.execute(insert_users)

    connection.commit()
    return

if __name__ == "__main__":
    main()
