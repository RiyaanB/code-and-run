import sqlite3
from TestCase import *

conn = sqlite3.connect('questions.sqlite')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS questions(difficulty INTEGER, name TEXT, description TEXT, testcases TEXT)")


def add_question(question):
    if True:
        c.execute("INSERT INTO questions (difficulty, name, description, testcases) VALUES (?, ?, ?, ?)", (question.difficulty, question.name, question.description, question.test_case_string))
        conn.commit()


def get_questions():
    pass


def end():
    c.close()
    conn.close()

if __name__ == "__main__":
    create_table()
    add_question(b)
    end()
