__author__ = 'chrisgrochmal'


import csv
import sqlite3

database = 'main.db'  # global variable to hold database name



def write_one_to_db(dept, courseNum, semester, meetingType, seatsTaken, seatsOffered, instructor):
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
        cur.execute(sql_cmd, (dept, courseNum, semester, meetingType, seatsTaken, seatsOffered, instructor ))



if __name__ == "__main__":
    # Here are some methods that demo how to write data to a DB with sqlite.
    # Uncomment out each of the calls below and see what it does.
    # The trick is creating the SQL command string.  The 4th version is THE RIGHT way to do this.

    # write_one_to_db_version1()
    # write_one_to_db_version2('APMA', 2120)
    # write_one_to_db_version3('ENGR', 1620)
    # write_one_to_db_version4("XXX's", 2150)

    with open('seas-courses-5years.csv', 'rU') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            write_one_to_db(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            print ', '.join(row)



