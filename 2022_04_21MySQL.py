import mysql.connector
from mysql.connector import Error


# setting up connection

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("succesful")
    except Error as err:
        print("Error: '{err}'")
    return connection

# put our MYSQL terminal passwrod


pw = "Anmol@mysql"

# Database name
db = "world"
connection = create_server_connection("localhost", "root", pw)

# create my_sql python


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("database cerated successfully")
    except Error as err:
        print(f"Error: '{err}'")
    create_database_query = "Create database python"
    create_database(connection, create_database_query)


# connect to database

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name)
        print("Mysql database connction successfull")
    except Error as err:
        print("Error: '{err}'")
    return connection


# execute sql queries

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        for x in cursor:
            print(x)
        print("success")
    except Error as err:
        print("Error: '{err}'")

execute_query(connection,"SHOW DATABASES;")