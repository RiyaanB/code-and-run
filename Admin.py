from Database import DatabaseConnection
from Question import *

"""
from tkinter import *

dark_gray = '#1e1e1e'
gray = '#3f3f3f'
light_gray = '#6f6f6f'
white = '#ffffff'
window = None


def chose_question():
    window.destroy()


def admin():
    global window
    previous_loc = None if window is None else (window.winfo_rootx(), window.winfo_rooty())

    root = Tk()
    root.configure(background=gray)
    w = 600
    h = 450
    if previous_loc is None:
        x = (1440/2) - (w/2)
        y = (900/2) - (h/2) - 100
    else:
        x, y = previous_loc
    root.geometry('%dx%d+%d+%d' % (w, h, x, y - 22))
    root.resizable(False, False)

    window = root

    welcome_label = Label(root, text='Hello!', highlightthickness=0, font=('Monospaced', 48),
                          background=gray, foreground=light_gray)
    welcome_label.place(x=300, y=35, anchor=CENTER)

    python_button = Button(root, height=200, width=200, text="Question", command=chose_question)
    python_button.place(x=75, y=90)

    java_button = Button(root, height=200, width=200, text="Test Case", command=chose_testcase)
    java_button.place(x=325, y=90)

    question_label = Label(root, text='Which language will you use?', font=('Monospaced', 40),
                           background=gray, foreground=dark_gray)
    question_label.place(x=300, y=350, anchor=CENTER)

    exit_button = Button(root, text='Exit', width=8, command=quit, background=dark_gray,
                         font=('Monospaced', 20))
    exit_button.place(x=300, y=415, anchor=CENTER)

    root.mainloop()
"""

if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table()
    database_connection.insert_question(question1)
    database_connection.insert_question(question2)
    database_connection.insert_question(question3)
    database_connection.insert_question(question4)
    database_connection.insert_question(question5)
