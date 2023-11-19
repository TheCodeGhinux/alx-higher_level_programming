#!/usr/bin/python3
"""
Script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument. This version is safe from
MySQL injections.

args: <mysql username>
    <mysql password>
    <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Check for correct arguments
    args: Username, password, database
    """

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        """ Connect to the db server"""
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )
        cursor = db.cursor()

        # Use parameterized query to avoid SQL injection
        query = "SELECT * FROM `states`"
        cursor.execute(query)

        """Print results"""
        for state in cursor.fetchall():
            print(state)
