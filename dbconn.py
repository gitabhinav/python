import mysql.connector
from mysql.connector import errorcode

def open(l_User, l_Password,l_Database):
    try:
        conn = mysql.connector.connect(user= l_User, password= l_Password, database= l_Database)
        return conn
    except mysql.connection.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return -1
    
def close(conn):
    try:
        conn.close()
        print("connection closed")
    except mysql.connection.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


      
    
