#!/usr/bin/python3
"""
Module that lists all states from the database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    
    # Create cursor to execute queries
    cur = conn.cursor()
    
    # Execute SELECT query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all results
    query_rows = cur.fetchall()
    
    # Display results
    for row in query_rows:
        print(row)
    
    # Close cursor and connection
    cur.close()
    conn.close()
