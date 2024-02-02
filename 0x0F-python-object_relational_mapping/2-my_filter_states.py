#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N) from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    cursor = None
    db = None
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
        )
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4])
        )

        states = cursor.fetchall()

        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print(f"{e}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
