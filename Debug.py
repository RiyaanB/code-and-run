from tkinter import *
from Database import *

dark_gray = '#1e1e1e'
gray = '#3f3f3f'
light_gray = '#6f6f6f'
white = '#ffffff'


def select_question():
    root = Tk()
    root.configure(background=gray)
    w = 600
    h = 450
    root.geometry("600x450")
    root.resizable = False
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root, width=20, height=30, yscrollcommand=scrollbar.set)
    database_connection = DatabaseConnection()
    questions = database_connection.get_all_questions()
    print(questions)
    for i in questions:
        listbox.insert(END, i)
    listbox.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=listbox.yview)
    root.mainloop()

select_question()
