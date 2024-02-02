#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""
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
        cursor = db.cursor()

        cursor.execute(
            """SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id"""
        )

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
