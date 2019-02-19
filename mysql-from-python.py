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
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                       Friends(name char(20), age int, DOB datetime);""")                         
        #note that the above still may display a warning(not error) if table already exists
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()
    
    #run thids in bash....then go to mysql and type:
    #   select * from Friends;          use Chinook