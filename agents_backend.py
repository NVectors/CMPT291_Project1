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
        # Generate unique ID + get date
        birth_id = uuid.uuid1()
        today = date.today().isoformat()
        # Get registration place
        self.cursor.execute(
                "SELECT city FROM users WHERE users.uid = {uid}"
                .format(uid=self.uid))
        reg_place = self.cursor.fetchone()['city']
        # Get addr + phone of mother.
        self.cursor.execute(
                "SELECT address, phone FROM persons WHERE fname = {mfname} AND lname = {mlname}"
                .format(mfname=mfname, mlname=mlname))
        m_info = self.cursor.fetchone()

        # Create person entry for the newborn.
        person_entry = PERSONS_ENTRY.format(fname=fname, lname=lname, bdate=bdate,
                    bplace=bplace, address=m_info['address'], 
                    phone=m_info['phone'])

        # Create birth entry for the newborn.
        birth_entry = BIRTHS_ENTRY.format(regno=birth_id, fname=fname, lname=lname, 
                regdate=today, regplace=reg_place, gender=gender, 
                f_fname=ffname, f_lname=flname, m_fname=mfname, m_lname=mlname)

        # Insert entries + commit.
        try:
            cursor.execute("INSERT INTO persons VALUES {}".format(person_entry)
            cursor.execute("INSERT INTO births VALUES {}".format(birth_entry))
            self.con.commit()
            return 1


        except Exception as e:
            # TODO Perhaps consider throwing excption here?
            print("FAILED TO INSERT ENTRIES!!")
            print(e)
            self.con.rollback()
            return -1


                





