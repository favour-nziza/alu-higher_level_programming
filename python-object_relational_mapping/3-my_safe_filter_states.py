#!/usr/bin/python3
"""Safely displays all values in states where name matches the argument."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE BINARY `name` = %s ORDER BY `id`",
              (sys.argv[4],))
    [print(state) for state in c.fetchall()]
    c.close()
    db.close()
