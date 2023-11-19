#!/usr/bin/python3
"""
A script that lists all states
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Check for correct number of arguments"""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    """
      Check for correct arguments
      args: Username, password, database
    """
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    """Connect to MySQL server"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    """Create a cursor object to interact with the database"""
    cursor = db.cursor()

    """Execute the SELECT query to retrieve states from the states table"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch all the rows"""
    rows = cursor.fetchall()

    """Display the results"""
    for row in rows:
        print(row)

    """Close the cursor and database connection"""
    cursor.close()
    db.close()
