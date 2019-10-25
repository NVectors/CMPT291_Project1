import sys
import sqlite3
import Queries

def main():
        try:
            database_file = sys.argv[1]
        except:
            raise Exception("Database file path not defined")
        connection, cursor = queries.connect(database_file)

        while True:
            user_email = login_menu(connection, cursor)
            main_menu(connection, cursor, user_email)

