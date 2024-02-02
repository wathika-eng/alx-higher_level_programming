#!/usr/bin/python3
"""Safe from MySQL injections"""
import sys
import MySQLdb

if __name__ == "__main__":
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
        state = sys.argv[4]
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE name LIKE %s", (state,))

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
