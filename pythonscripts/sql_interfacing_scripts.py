import pymysql.cursors

connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "example",
        )
def create_database():
    with connection.cursor() as cursor:
        sql = "create table users"
    
