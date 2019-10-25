import sqlite3
import time
import hashlib

connection = None
cursor = None



def connect(path):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return connection, cursor

def drop_tables(connection, cursor):
    # Drop tables for given queries
    drop_query=   '''
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
    # Define and create tables for our DB
    persons_query=   '''
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

    births_query=  '''
                        CREATE TABLE births (
                                    regno	INTEGER,
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

    marriages_query= '''
                    CREATE TABLE marriages (
                                    regno	INTEGER,
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
    vehicles_query= '''
                    CREATE TABLE vehicles (
                                    vin		CHAR(5),
                                    make	CHAR(10),
                                    model	CHAR(10),
                                    year	INTEGER,
                                    color	CHAR(10),
                                    PRIMARY KEY (vin)
                                    );
                    '''   
    registrations_query= '''
                    CREATE TABLE registrations (
                                    regno	INTEGER,
                                    regdate	DATE,
                                    expiry	DATE,
                                    plate	CHAR(7),
                                    vin		CHAR(5), 
                                    fname	CHAR(12),
                                    lname	CHAR(12),
                                    PRIMARY KEY (regno),
                                    FOREIGN KEY (vin) references vehicles,
                                    FOREIGN KEY (fname,lname) references persons
                                    );
                        '''  
    tickets_query= '''
                    CREATE TABLE tickets (
                                    tno		INTEGER,
                                    regno	INTEGER,
                                    fine	INTEGER,
                                    violation	text,
                                    vdate	DATE,
                                    PRIMARY KEY (tno),
                                    FOREIGN KEY (regno) references registrations
                                    );
                    '''
    demeritNotices_query= '''
                    CREATE TABLE demeritNotices (
                                    ddate	DATE, 
                                    fname	CHAR(12), 
                                    lname	CHAR(12), 
                                    points	INTEGER, 
                                    desc	text,
                                    PRIMARY KEY (ddate,fname,lname),
                                    FOREIGN KEY (fname,lname) references persons
                                    );
                    '''
    payments_query= '''
                    CREATE TABLE payments (
                                    tno		INTEGER,
                                    pdate	DATE,
                                    amount	INTEGER,
                                    PRIMARY KEY (tno, pdate),
                                    FOREIGN KEY (tno) references tickets
                                    );
                    '''
    users_query= '''
                    CREATE TABLE users (
                                    uid		CHAR(8),
                                    pwd		CHAR(8),
                                    utype	CHAR(1),	-- 'a' for agents, 'o' for officers
                                    fname	CHAR(12),
                                    lname	CHAR(12), 
                                    city	CHAR(15),
                                    PRIMARY KEY(uid),
                                    FOREIGN KEY (fname,lname) references persons
                                    );
                    '''
                    
    cursor.execute(persons_query)
    cursor.execute(births_query)
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
    # Test data for database
    # Test data from all tables (excpet last 2) from assignment 2 used by markers for their testing
    
    insert_persons= '''insert into persons values
    # Agents
        ('Trayvon','Fox','1892-07-17','PeaceRiver,AB','133 Street PR','443-449-9999'),
        ('Lillian', 'Bounds', '1899-02-15', 'Spalding, Idaho', 'Los Angeles, US', '213-555-5556'),
        ('Adam','Rafiei',"1900-01-02","Shiraz,Iran","Tehran,Iran","916-331-3311"),
    # Officers    
        ('James','Smith','1900-08-08','Calgary,AB','43,43Ave','720-000-0001'),
        ('Walt', 'Disney', '1901-12-05', 'Chicago, US', 'Los Angeles, US', '213-555-5555'),
        ('Mary','Brown','1905-11-15','Nordegg,AB','22,67Ave','776-655-9955'),
    # Normie backround human filler in Agent/Officer suspense thriller    
        ('John', 'Truyens', '1907-05-15', 'Flanders, Belgium', 'Beverly Hills, Los Angeles, US', '213-555-5558'),
        ('Linda','Smith','1908-02-26','Ohaton,AB','43,43Ave','680-099-9943'),
        ('Minnie', 'Mouse', '1928-01-05', 'Disneyland', 'Anaheim, US', '714-555-5552'),
        ('Mickey', 'Mouse', '1928-01-05', 'Disneyland', 'Anaheim, US', '714-555-5551'),
        ("Mary","Smith","1950-11-08","Calgary,AB","11Ave,1st","604-555-2244"),
        ("Aunt","Smith","1951-12-08","Calgary,AB","11Ave,1st","888-555-2244"),
        ("Dave","Fox","1950-03-29","Calgary,AB","11Ave,1st","664-110-8763"),
        ("Uncle","Fox","1951-03-29","Calgary,AB","11Ave,1st","780-110-8743"),
        ('Michael','Fox','1981-06-09','Edmonton, AB','Manhattan, New York, US', '212-111-1111'),
        ('Cousin1','Fox','1981-06-09','Edmonton, AB','Manhattan, New York, US', '666-111-1111'),
        ('Cousin2','Fox','1991-02-06','Edmonton, AB','Manhattan, New York, US', '666-111-1111'),
        ("Megan","Fox","1982-06-09","Calgary,AB","12Ave,101st","780-460-1134"),
        ("Fatima","Fox","1992-06-09","Calgary,AB","12Ave,101st","444-470-7734"),
        ("Lisa","Bounds","1999-04-10","Spalding,Idaho","Moscow,101st","604-420-1234"),
        ('Diane','Wong','1973-04-04','England','London,Hackney','766-664-6678'),
        ('Davood','Rafiei',date('now','-21 years'),'Iran','100 Lovely Street,Edmonton,AB', '780-111-2222'),
        ('Linda','Fox','1991-02-04','England','London','344-447-7755'),
        ('Tammy','Fox','1991-02-04','England','Manchester','344-111-2345'),
        ('Henry','Wong','1993-04-04','Canada','Alert','566-664-6678'),
        ('Michael','Parenti','1991-02-04','England','London','344-447-7755')
    '''
    insert_births= '''insert into births values
        (1,'Mary','Smith','1920-04-04','Ohaton,AB','F','James','Smith','Linda','Smith'),
        (2,'Aunt','Smith','1922-06-04','Ohaton,AB','F','James','Smith','Linda','Smith'),
        (3,'Dave','Fox','1922-03-06','Calgary,AB','M','Trayvon','Fox','Mary','Brown'),
        (5,'Uncle','Fox','1925-11-06','Calgary,AB','M','Trayvon','Fox','Mary','Brown'),
        (6,'Cousin1', 'Fox', '1982-06-10', 'Edmonton,AB', 'F', 'Walt', 'Disney', 'Aunt', 'Smith'),
        (7,'Cousin2', 'Fox', '1991-02-06', 'Edmonton,AB', 'F', 'Uncle', 'Fox', 'Lillian', 'Bounds'),
        (100,'Mickey', 'Mouse', '1928-02-05', 'Anaheim, US', 'M', 'Walt', 'Disney', 'Lillian', 'Bounds'),
        (200,'Minnie', 'Mouse', '1928-02-04', 'Anaheim, US', 'M', 'Walt', 'Disney', 'Lillian', 'Bounds'),
        (300,'Michael', 'Fox', '1981-06-10', 'Edmonton,AB', 'M', 'Dave', 'Fox', 'Mary', 'Smith'),
        (310,'Megan', 'Fox', '1982-06-10', 'Edmonton,AB', 'F', 'Dave', 'Fox', 'Mary', 'Smith'),
        (320,'Fatima', 'Fox', '1992-06-10', 'Edmonton,AB', 'F', 'Dave', 'Fox', 'Lillian', 'Bounds'),
        (330,'Adam', 'Rafiei', '1960-02-10', 'Iran', 'M', 'Walt', 'Disney', 'Mary', 'Brown'),
        (400,'Lisa', 'Bounds', '1999-04-16', 'Spalding,Idaho', 'F', 'John', 'Truyens', 'Lillian', 'Bounds'),
        (600,'Davood', 'Rafiei', date('now','-21 years'), 'Iran', 'M', 'Adam', 'Rafiei', 'Mary', 'Smith'),
        (700,'Linda','Fox','1991-02-06','England','F',"Michael","Fox","Lisa","Bounds"),
        (750,'Tammy','Fox','1991-02-04','England','F',"Michael","Fox","Lisa","Bounds"),
        (775,'Henry','Wong','1993-04-05','Canada','M',"Michael","Fox","Diane","Wong")
    '''
    insert_marriages= '''insert into marriages values
        (200, '1925-07-13', 'Idaho, US', 'Walt', 'Disney', 'Lillian', 'Bounds'),
        (201, '1969-05-03', 'Los Angeles, US', 'Lillian', 'Bounds', 'John', 'Truyens'),
        (300, '1990-04-13', 'Idaho, US', 'Michael', 'Fox', 'Lisa', 'Bounds'),
        (301, '1992-09-12', 'Idaho, US', 'Diane', 'Wong','Michael', 'Fox'),
        (305, '1945-09-11', 'Idaho, US', 'Mickey', 'Mouse', 'Lisa', 'Bounds')
     '''
    
    insert_vehicles= '''insert into vehicles values    
        (200, 'Chevrolet', 'Camaro', 1969, 'red'),
        (100, 'Doge', 'Challenger', 1969, 'red'),
        (101, 'Doge', 'Challenger', 1969, 'red'), 
        (300, 'Mercedes', 'SL 230', 1969, 'black'),
        (400, 'Mercedes', 'Benz', 1980, 'white'),
        (500, 'Ferrari', 'F1', 1999, 'red'),
        (600, 'Toyota', 'Camry', 2005, 'black'),
        (700, 'Nissan', 'Altima', 2005, 'black'),
        (801, 'Honda', 'Accord', 2005, 'white'),
        (800, 'Maza', '3', 2005, 'white'),
        (900, 'Nissan', 'Altima', 2010, 'red'),
        (1000, 'Nissan', 'Altima', 2010, 'blue'),
        (1001, 'Toyota', 'Camry', 2010, 'green')
     '''
    
    insert_registrations= '''insert into registrations values        
        (300, '1964-05-06','1965-05-06', 'Plate1',100, 'Walt', 'Disney'),
        (302, '2019-01-06','2020-01-06', 'Plate2',100, 'Lillian', 'Bounds'),
        (801, '2019-01-06','2020-08-25', 'Plate3',101, 'Michael', 'Fox'),
        (802, '2018-12-08','2019-12-08', 'Plate4',300, "Diane","Wong"),
        (803, '2018-01-08','2020-01-08', 'Plate5',200, "Diane","Wong"),
        (804, '2018-12-25','2019-12-25', 'Plate6',500, "Diane","Wong"),
        (805, '2018-12-16','2020-12-16', 'Plate7',600, 'John', 'Truyens'),
        (901, '2018-11-16','2019-11-16', 'Plate9',801, 'John', 'Truyens'),
        (902, '2016-10-11','2017-10-11', 'PlateA',800, 'Lisa', 'Bounds'),
        (806, '1999-01-11','2001-01-11', 'Plate8',900, 'John', 'Truyens'),
        (903, '2016-02-29','2018-02-28', 'PlateB', 1000, 'Lisa', 'Bounds'),
        (905, '2017-06-26','2019-06-26', 'PlateC', 1001, 'Davood', 'Rafiei'),
        (1001, '2019-01-16','2021-01-16', 'PlateD',200, 'John', 'Truyens'),
        (1002, '2018-11-11','2020-11-11', 'PlateE',100, 'Lisa', 'Bounds'),
        (1003, '2018-01-11','2019-09-30', 'PlateF',101, 'John', 'Truyens'),
        (1004, '2019-02-29','2020-02-28', 'PlateG', 700, 'Lisa', 'Bounds'),
        (1005, '2019-06-26','2020-06-26', 'PlateH', 1000, 'Davood', 'Rafiei')
    '''
    
    insert_tickets= '''insert into tickets values            
        (100,300,40,'red light violation','1964-08-20'),
        (101,805,40,'red light violation','2018-12-20'),
        (107,905,40,'red violation','2019-01-20'),
        (109,902,150,'yellow light violation','2018-01-21'),
        (108,803,150,'Stunting','2019-02-29'),
        (102,901,220,'DUI','2019-02-18'),
        (103,806,70,'illegal parking','2016-08-30'),
        (104,805,40,'speeding','2019-02-29'),
        (105,905,10,'yellow light violation','2019-02-28'),
        (106,905,220,'red violation','2018-12-30'),
        (111,805,220,'DUI','2019-06-12'),
        (112,801,220,'red light violation','2019-06-30'),
        (113,801,221,'grand theft auto','2020-12-30'),
        (114,801,222,'grand theft auto','2020-12-30'),
        (115,801,222,'grand theft auto','2020-12-30')
    '''
    
    insert_demeritNotices= '''insert into demeritNotices values                
        ('1991-03-29', 'Lisa', 'Bounds', 10, 'DUI'),
        ('2018-07-20', 'Michael', 'Fox', 4, 'Speeding'),
        ('1993-04-25', 'Diane', 'Wong', 2, 'Speeding'),
        ('2018-03-20', 'Michael', 'Fox', 12, 'DWI'),
        ('2019-10-31', 'Diane', 'Wong', 2, 'Speeding'),
        ('1964-08-20', 'Walt', 'Disney', 4, 'Speeding'),
        ('1991-03-30', 'Lisa', 'Bounds', 4, 'Speeding'),
        ('2019-09-28', 'Mickey', 'Mouse', 12, 'DUI'),
        ('2018-08-20', 'Walt', 'Disney', 20, 'Vehicular Manslaughter'),
        ('1994-03-30', 'Lisa', 'Bounds', 4, 'Speeding'),
        ('2019-03-22', 'Mickey', 'Mouse', 12, 'DUI')
    '''
    
    insert_payments= '''insert into payments values     
        (100,'1985-08-20', 125),
        (101,'2019-12-20', 25),
        (107,'2019-05-22', 1000),
        (109,'2017-03-22', 29),
        (108,'2019-04-29', 50),
        (102,'2019-08-19', 87),
        (103,'2018-08-30', 42)
    '''
    insert_users= '''insert into users values        
    # (uid, pwd, utype, fname, lname, city)
    # uid/all other string matches are not case sensitive (case-insensitive)
    # password is case-sensitve
    # utype = 'a' for agents and 'o' for officers   
    
    # The ones below are also people from persons
        ('trayvon_123', 'trayway_69', 'a', 'Trayvon', 'Fox', 'Edmonton'),
        ('123_lillith', '69_BoUnD', 'a', 'Lillian', 'Bounds', 'Vancouver'),
        ('rafiki', 'Dark-Dick-Magician', 'a', 'Adam','Rafiei', 'Calgary'),
        
        ('JimJam', 'WamBamJimJoeMamma', 'o', 'James','Smith', 'Edmonton'),
        ('TheMouse', 'Mickey33', 'o', 'Walt', 'Disney', 'Vancouver'),
        ('GoingMary', 'Xerox-';-88', 'o', 'Mary','Brown', 'Calgary'),
        
    # The ones below are completely new people
        ('chie3frich', ';U"]VvvwbZt46,jh', 'a', 'Nick', 'Yames', 'City0'),
        ('honkycr5ingling', 'YbS#cE7'>5E7gQtN', 'a', 'Jane', 'Danith', 'city1'),
        ('sar1ca2stic3caldera', '3XYk<urL4qT<;ZW\', 'a', 'Sam','Pitt', 'city3'),
        
        ('margin1chase', '+!V5uF:d:zsE<7L9', 'o', 'Griffith','Ground', 'city4'),
        ('alco3skies', 'D4uYq[P$Zw"n3<k5', 'o', 'Perry', 'Water', 'city5'),
        ('yellowkn6ife', 'N..)%x}E8(>;Q}(u', 'o', 'Valence','Forespear', 'city6'),
    '''    


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

def main():
    return 

if __name__ == "__main__":
    main()