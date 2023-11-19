#!/usr/bin/python3
"""
    Script to List all states with a name starting
    with N from the database hbtn_0e_0_usa.

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

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    """ Connect the db server"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")

    """Print the state"""
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]

