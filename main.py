import sys
import sqlite3
import Queries


def main():
    try:
        database_file = 'p1.db'  # Once final, edit to sys.argv[] to run in Terminal
    except:
        raise Exception("Database file path not defined")
    connection, cursor = Queries.connect(database_file)


if __name__ == "__main__":
    main()
