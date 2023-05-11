# Install mysql on your PC 
# pip install mysql
# pip install my-sql connector 
# pip insyall my-sql-connector-python

import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)

# Prepare a cursor object 
cursorObject = database.cursor()

# Create a database 
cursorObject.execute("CREATE DATABASE elderco")
database.close()
print("All done")
