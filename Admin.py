from Database import DatabaseConnection
from Question import *

if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table()
    database_connection.insert_question(question1)
    database_connection.insert_question(question2)
    database_connection.insert_question(question3)
    database_connection.insert_question(question4)
