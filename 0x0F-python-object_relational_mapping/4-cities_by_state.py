#!/usr/bin/python3
"""
    Script  that lists all cities
    from the database hbtn_0e_4_usa

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
    cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    
    """Print results"""
    for city in cursor.fetchall():
        print(city)
