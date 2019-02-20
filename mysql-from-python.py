import os
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
        list_of_names = ['fred', 'Fred']
        #prepare a string with the same num of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()
    
    #run thids in bash....then go to mysql and type:
    #   select * from Friends;          use Chinook
    
    
""" python code
>>> names = ['jim', 'bob']
>>> len(names)
2
>>> ['%s']*len(names)
['%s', '%s']
>>> ",".join(['%s']*len(names))
'%s,%s'
>>> "DELETE FROM Friends WHERE name in ({0})".format(",".join(['%s']*len(names))
... exit()
"""