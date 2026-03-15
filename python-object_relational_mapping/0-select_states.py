#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


def list_states():
    """
    Connects to the database and prints all states sorted by id.
    """
    # Grab arguments from the command line
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    # Note: localhost and port 3306 are requirements
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    rows = cursor.fetchall()

    # Print results in the specified format
    for row in rows:
        print(row)

    # Clean up: Close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Ensure code doesn't run when imported
    list_states()
