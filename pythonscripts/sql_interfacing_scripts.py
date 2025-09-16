import pymysql.cursors
from dotenv import dotenv_values
config = dotenv_values('.env')

# making the mysql connection object
connection = pymysql.connect(
        host = config['MYSQL_HOST'],
        user = config['MYSQL_USERNAME'],
        password = config['MYSQL_PASSWORD'],
        database = config['MYSQL_DATABASE']
        )

def list_users():
    with connection.cursor() as cursor:
        sql = "select * from Users"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
list_users() 
