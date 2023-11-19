#!/usr/bin/python3
"""
Script that takes in the name of a
state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa

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
    query = "SELECT `s`.`name` FROM `cities` as `c` \
        INNER JOIN `states` as `s` \
        ON `c`.`state_id` = `s`.`id` \
        WHERE `s`.`name` = %s \
        ORDER BY `c`.`id`"
    cursor.execute(query, (state_name,))

    """Print results"""
    for state in cursor.fetchall():
        print(state)
