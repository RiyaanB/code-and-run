from Database import DatabaseConnection
from Question import *

if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table()
    for a in range(30):
        database_connection.insert_question(question1)
        database_connection.insert_question(question2)
        print(a+1)
