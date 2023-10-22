#IMPORT
import mysql.connector as sql

#CONNECT
def dbconfig():
    db = sql.connect(
        host = 'localhost',
        user = 'root',
        password = 'password',
        auth_plugin='mysql_native_password'
        )  
    return db
