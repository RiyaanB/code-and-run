import psycopg2


file = open("credentials.txt", "r")
host = file.readline()
database = file.readline()
user = file.readline()
port = file.readline()
password = file.readline()


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

    def query_all_questions(self):
        self.cursor.execute("SELECT * FROM questions ")
        all_questions = self.cursor.fetchall()
        return all_questions

    def get_testcases(self, qname):
        command = "SELECT * from testcases WHERE qname='" + qname + "'"
        self.cursor.execute(command)
        query = self.cursor.fetchall()
        print(query)

if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table()
    pass