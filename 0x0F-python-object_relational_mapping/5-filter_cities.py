#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and lists all 
cities of that state, using the database hbtn_0e_4_usa
"""
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

        cursor.execute(
            """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
            (state,),
        )

        cities = cursor.fetchall()
        listing = tuple(city[1] for city in cities)
        print(*listing, sep=(", "))
    except Exception as e:
        print(f"{e}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
