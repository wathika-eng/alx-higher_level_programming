#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (state,))

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
