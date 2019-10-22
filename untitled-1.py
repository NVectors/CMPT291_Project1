import sqlite3
import time
import hashlib

connection = None
cursor = None



def connect(path):
    global connection, cursor

    #
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return

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
                                    fname	char(12),
                                    lname	char(12),
                                    bdate	date,
                                    bplace	char(20), 
                                    address	char(30),
                                    phone	char(12),
                                    PRIMARY KEY (fname, lname)
                                    );
                    '''

    births_query=  '''
                        CREATE TABLE births (
                                    regno	int,
                                    fname	char(12),
                                    lname	char(12),
                                    regdate	date,
                                    regplace	char(20),
                                    gender	char(1),
                                    f_fname	char(12),
                                    f_lname	char(12),
                                    m_fname	char(12),
                                    m_lname	char(12),
                                    PRIMARY KEY (regno),
                                    FOREIGN KEY (fname,lname) references persons,
                                    FOREIGN KEY (f_fname,f_lname) references persons,
                                    FOREIGN KEY (m_fname,m_lname) references persons
                                    );
                    '''

    marriages_query= '''
                    CREATE TABLE marriages (
                                    regno	int,
                                    regdate	date,
                                    regplace	char(20),
                                    p1_fname	char(12),
                                    p1_lname	char(12),
                                    p2_fname	char(12),
                                    p2_lname	char(12),
                                    PRIMARY KEY (regno),
                                    FOREIGN KEY (p1_fname,p1_lname) references persons,
                                    FOREIGN KEY (p2_fname,p2_lname) references persons
                                    );
                    '''
    vehicles_query= '''
                    CREATE TABLE vehicles (
                                    vin		char(5),
                                    make	char(10),
                                    model	char(10),
                                    year	int,
                                    color	char(10),
                                    PRIMARY KEY (vin)
                                    );
                    '''   
    registrations_query= '''
                    CREATE TABLE registrations (
                                    regno	int,
                                    regdate	date,
                                    expiry	date,
                                    plate	char(7),
                                    vin		char(5), 
                                    fname	char(12),
                                    lname	char(12),
                                    primary key (regno),
                                    foreign key (vin) references vehicles,
                                    foreign key (fname,lname) references persons
                                    );
                        '''  
    tickets_query= '''
                    CREATE TABLE tickets (
                                    tno		int,
                                    regno	int,
                                    fine	int,
                                    violation	text,
                                    vdate	date,
                                    primary key (tno),
                                    foreign key (regno) references registrations
                                    );
                    '''
    demeritNotices_query= '''
                    CREATE TABLE demeritNotices (
                                    ddate	date, 
                                    fname	char(12), 
                                    lname	char(12), 
                                    points	int, 
                                    desc	text,
                                    primary key (ddate,fname,lname),
                                    foreign key (fname,lname) references persons
                                    );
                    '''
    payments_query= '''
                    CREATE TABLE payments (
                                    tno		int,
                                    pdate	date,
                                    amount	int,
                                    primary key (tno, pdate),
                                    foreign key (tno) references tickets
                                    );
                    '''
    users_query= '''
                    CREATE TABLE users (
                                    uid		char(8),
                                    pwd		char(8),
                                    utype	char(1),	-- 'a' for agents, 'o' for officers
                                    fname	char(12),
                                    lname	char(12), 
                                    city	char(15),
                                    primary key(uid),
                                    foreign key (fname,lname) references persons
                                    );
                    '''
        
    cursor.execute(course_query)
    cursor.execute(student_query)
    cursor.execute(enroll_query)
    connection.commit()

    return

def insert_data(connection, cursor):
    #Test data for database
    #
    #
    #
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