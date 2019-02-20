import os
import datetime
import pymysql

# get username from cloud9 workspace
# modify this if running on another environment

username = os.getenv('C9_USER')

# connect to the database
#So we're saying host is localhost, user is the username variable that we set above, the password is, of course, still blank unless you have changed it, and we're going to use the Chinook database.
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    #run a query
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),      #list seperate by commas..whole thing into square brackets rows plural
                ("Jim", 56, "1955-05-09 13:12:45"),
                ("Fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)    #rows plural. executemany                     
        connection.commit()
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()
    
    #run thids in bash....then go to mysql and type:
    #   select * from Friends;          use Chinook