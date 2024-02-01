#!/usr/bin/python3
"""Read from a database"""
import MySQLdb
import sys


if len(sys.argv) != 4:
    print("Usage: ./0-select_states.py user password db_name")
    sys.exit(1)

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

connection = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name,
)
cursor = connection.cursor()

query = "SELECT * FROM states ORDER BY states.id"
cursor.execute(query)

states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
connection.close()
