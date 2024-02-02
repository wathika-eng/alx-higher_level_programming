#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N) from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py user password db_name")
        sys.exit(1)
    cursor = None
    db = None
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
        )
        cursor = db.cursor()

        query = (
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
        )
        cursor.execute(query)

        states = cursor.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        print(f"{e}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
