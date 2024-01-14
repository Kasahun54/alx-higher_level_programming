#!/usr/bin/python3
"""
this is a script that lists all states from database 'hbtn_0e_0_usa'
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

        user = argv[1]
        passwd = argv[2]
        db = argv[3]

        db_connection = MySQLdb.connect(host="localhost", port=3306, user=user,
                                        passwd=passwd, db=db, charset="utf8")

        cursor = db_connection.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cursor.fetchall()

        for row in query_rows:
                print(row)

        cursor.close()
        db_connection.close()
