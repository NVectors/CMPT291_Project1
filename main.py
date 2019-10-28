#!/usr/bin/python3
import sys
import sqlite3
import Queries


def main():
    try:
        database_file = 'p1.db'  # Once final, edit to sys.argv[] to run in Terminal
    except:
        raise Exception("Database file path not defined")
    connection, cursor = Queries.connect(database_file)
    test_agent_add_b(connection, cursor)


def test_agent_add_b(connection, cursor):
    from agents_backend import agent
    from datetime import date
    # Test add birth
    print("Testing add birth\t| ", end="")
    # Drop test entry
    try:
        cursor.execute("DELETE FROM births WHERE fname = 'Jane' AND lname = 'Doe'")
        cursor.execute("DELETE FROM persons WHERE fname = 'Jane' AND lname = 'Doe'")
        connection.commit()
    except:
        pass

    # Instantiate agent class
    usr = agent(connection, cursor, 'jstainer0')
    # Attempt to add a birth for Jane Doe
    usr.reg_birth('Jane', 'Doe', 'f', '1997-12-12', 'Edmonton', 'Mary', 'Brown', 'Adam', 'Rafiei')
    
    # Check if it worked!
    cursor.execute("SELECT * FROM persons WHERE fname = '{}' and lname = '{}'"
            .format('Jane', 'Doe'))
    p = cursor.fetchone()
    cursor.execute("SELECT * FROM births WHERE fname = '{}' and lname = '{}'"
        .format('Jane', 'Doe'))
    b=cursor.fetchone()

    if p == None or p[2] != '1997-12-12' or p[3] != 'Edmonton' or p[4] != '22,67Ave' or p[5] != '776-655-9955':
        print("Failed |")
        return

    if b == None or b[3] != str(date.today().isoformat()) or b[4] != 'Edmonton' or b[5] != 'f' or b[6] != 'Adam' or b[7] != 'Rafiei' or b[8] != 'Mary' or b[9] != 'Brown':
        print("Failed |")
        return

    print("Passed |")



if __name__ == "__main__":
    main()
