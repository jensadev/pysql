# https://dev.mysql.com/doc/connector-python/en/
# pip install mysql-connector-python

# https://pypi.org/project/python-dotenv/
# pip install python-dotenv

from dotenv import dotenv_values
import mysql.connector
from mysql.connector import errorcode

config = dotenv_values(".env")

db_config = {
  'user': config['DATABASE_USERNAME'],
  'password': config['DATABASE_PASSWORD'],
  'host': config['DATABASE_HOST'],
  'port': config['DATABASE_PORT'],
  'database': config['DATABASE_DATABASE']
}


try:
    cnx = mysql.connector.connect(**db_config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
# else:
#     cnx.close()

cursor = cnx.cursor()
query = ("SELECT Post.*, User.name as author FROM Post JOIN User ON Post.user_id = User.id")
cursor.execute(query)

for row in cursor:
    print(row)
    print(row[1], row[3])

cursor.close()
cnx.close()