#!/usr/bin/python3
"""
Script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument. This version is safe from
MySQL injections.

args: <mysql username>
    <mysql password>
    <database name>
    <state name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Check for correct arguments
    args: Username, password, database, state_name
    """

    """ Check if the correct number of arguments is provided"""
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
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

        """ Use parameterized query to avoid SQL injection"""
        query = "SELECT * FROM `states` WHERE `name` = %s ORDER BY `id`"
        cursor.execute(query, (state_name,))

        """Print results"""
        for state in cursor.fetchall():
            print(state)
