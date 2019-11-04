"""
Provides backend functionality for any agent related tasks. ie. Register a
birth, register a marriage, etc.
"""
import uuid
from datetime import date
from db_constants import *




class agent:

    def __init__(self, connection, cursor, uid):
        self.con = connection
        self.cursor = cursor
        self.uid = uid

    def reg_birth(self, fname, lname, gender, bdate, bplace, mfname, mlname, 
                    ffname, flname):
        # TODO Convert this function to use INSERT INTO sql statements...

        # Generate unique ID + get date
        birth_id = uuid.uuid1().int
        today = date.today().isoformat()
        # Get registration place
        self.cursor.execute(
                "SELECT city FROM users WHERE users.uid = '{uid}'"
                .format(uid=self.uid))
        reg_place = self.cursor.fetchone()[0]
        # Get addr + phone of mother.
        self.cursor.execute(
                "SELECT address, phone FROM persons WHERE fname = '{mfname}' AND lname = '{mlname}'"
                .format(mfname=mfname, mlname=mlname))
        m_info = self.cursor.fetchone()

        # Create person entry for the newborn.
        person_entry = PERSONS_ENTRY.format(fname=escape(fname), lname=escape(lname), bdate=escape(bdate),
                    bplace=escape(bplace), address=escape(m_info[0]), 
                    phone=escape(m_info[1]))

        # Create birth entry for the newborn.
        birth_entry = BIRTHS_ENTRY.format(regno=birth_id, fname=escape(fname), lname=escape(lname), 
                regdate=escape(today), regplace=escape(reg_place), gender=escape(gender), 
                f_fname=escape(ffname), f_lname=escape(flname), m_fname=escape(mfname), m_lname=escape(mlname))

        # Insert entries + commit.
        try:
            self.cursor.execute("INSERT INTO persons VALUES {}".format(person_entry))
            self.cursor.execute("INSERT INTO births VALUES {}".format(birth_entry))
            self.con.commit()
            return 1


        except Exception as e:
            # TODO Perhaps consider throwing excption here?
            print("FAILED TO INSERT ENTRIES!!")
            print(e)
            self.con.rollback()
            return -1


    def reg_marriage(self, p1_fname, p1_lname, p2_fname, p2_lname):
        # Generate unique ID + get date
        regno = uuid.uuid1().int
        today = date.today().isoformat()
        
        vals = MARRIAGES_ENTRY.format(regno=regno, 
                                      regdate=escape(today),
                                      regplace='null',
                                      p1_fname=escape(p1_fname),
                                      p1_lname=escape(p1_lname),
                                      p2_fname=escape(p2_fname),
                                      p2_lname=escape(p2_lname))
        
        main_statement = "INSERT INTO marriages VALUES {vals};"
        main_statement = main_statement.format(vals=vals)
        update_statement = "UPDATE marriages \
                            SET regplace=(SELECT city FROM users WHERE uid={uid}) \
                            WHERE regno={regno};".format(uid=escape(self.uid),
                                                        regno=regno)

        
        # Insert entries + commit.
        try:
            self.cursor.execute(main_statement)
            self.cursor.execute(update_statement)
            self.con.commit()
            return 1


        except Exception as e:
            # TODO Perhaps consider throwing excption here?
            print("FAILED TO INSERT ENTRIES!!")
            print(e)
            self.con.rollback()
            return -1


    def renew_reg(self, regno):

        update_statement = "UPDATE registrations SET expiry = (CASE WHEN expiry <= date('now') THEN date('now', '+1 year') ELSE date(expiry, '+1 year') END) WHERE regno={regno}"
                
        update_statement = update_statemnt.format(regno=regno)

         # Insert entries + commit.
        try:
            self.cursor.execute(update_statement)
            self.con.commit()
            return 1


        except Exception as e:
            # TODO Perhaps consider throwing excption here?
            print("FAILED TO INSERT ENTRIES!!")
            print(e)
            self.con.rollback()
            return -1



    def proc_bill_of_sale(self, vin, f_name_cur, l_name_cur, f_name_new, l_name_new, plate):

        update_statement = "UPDATE registrations SET fname={fname_new}, lname={lname_new}, plate={plate} where vin={vin} AND fname={fname_cur} AND lname={lname_cur}"
        update_statement = update_statement.format(fname_new=escape(f_name_new), 
                                                   lname_new=escape(l_name_new),
                                                   plate=escape(plate),
                                                   vin=vin,
                                                   fname_cur=escape(f_name_cur),
                                                   lname_cur=escape(l_name_cur))

        # Insert entries + commit.
        try:
            self.cursor.execute(update_statement)
            self.con.commit()
            return 1


        except Exception as e:
            # TODO Perhaps consider throwing excption here?
            print("FAILED TO INSERT ENTRIES!!")
            print(e)
            self.con.rollback()
            return -1







