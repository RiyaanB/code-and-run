import psycopg2
from Question import *

file = open("credentials.txt", "r")
host = file.readline()[:-1]
database = file.readline()[:-1]
user = file.readline()[:-1]
port = file.readline()[:-1]
password = file.readline()[:-1]


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname= '" + database + "' " +
                "user= '" + user + "' " +
                "host= '" + host + "' " +
                "password= '" + password + "' " +
                "port= '" + port + "'"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("Cannot connect to database")

    def create_table(self):
        questions_table_command = "CREATE TABLE IF NOT EXISTS questions(id serial PRIMARY KEY, qname VARCHAR(256) NOT NULL, description VARCHAR(1024))"
        self.cursor.execute(questions_table_command)
        testcases_table_command = "CREATE TABLE IF NOT EXISTS testcases(qname VARCHAR(256) , inputs VARCHAR(256), out VARCHAR(256))"
        self.cursor.execute(testcases_table_command)
        attempts_table_command = "CREATE TABLE IF NOT EXISTS attempts(qname VARCHAR(256), student VARCHAR(256), time TIMESTAMP, successful INTEGER, total INTEGER )"
        self.cursor.execute(attempts_table_command)

    def insert_question(self, question):
        self.cursor.execute("SELECT qname from questions")
        bool = (question.name,) not in self.cursor.fetchall()
        if bool:
            command = "INSERT INTO questions(qname, description) VALUES ('" + question.name + "', '" + question.description + "')"
            self.cursor.execute(command)
            for test_case in question.test_cases:
                self.insert_testcase(test_case, question.name)
            return True
        else:
            return False

    def insert_testcase(self, test_case, qname):
        command = "INSERT INTO testcases(qname, inputs, out) VALUES ('" + qname + "', '" + test_case.inputs + "', '" + test_case.output + "')"
        self.cursor.execute(command)

    def get_all_questions(self):
        self.cursor.execute("SELECT qname FROM questions ")
        results = self.cursor.fetchall()
        questions = []
        for result in results:
            questions.append(result[0])
        return questions

    def get_testcases(self, qname):
        command = "SELECT inputs,out FROM testcases WHERE qname='" + qname + "'"
        self.cursor.execute(command)
        query = self.cursor.fetchall()
        testcases = []
        for tc in query:
            testcases.append(TestCase(tc[0], tc[1]))
        return testcases

    def get_description(self, qname):
        command = "SELECT description FROM questions WHERE qname='" + qname +"'"
        self.cursor.execute(command)
        return self.cursor.fetchall()[0][0]

    def print_questions(self):
        command = "SELECT * FROM questions"
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        for r in result:
            print(r)

    def print_testcases(self):
        command = "SELECT * FROM testcases"
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        for r in result:
            print(r)

    def print_attempts(self):
        command = "SELECT * FROM attempts"
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        for r in result:
            print(r)

