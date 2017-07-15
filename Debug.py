from tkinter import *
from Database import *

dark_gray = '#1e1e1e'
gray = '#3f3f3f'
light_gray = '#6f6f6f'
white = '#ffffff'

description = None
see_description = None
select = None
database_connection = None
questions = None
listbox = None
root = None


def get_description():
    selected_name = questions[listbox.curselection()[0]]
    selected_description = database_connection.get_description(selected_name)
    description.config(text=selected_description, wrap=True, wraplength=260)
    select.config(state=NORMAL)


def choose_selected():
    selected_name = questions[listbox.curselection()[0]]
    root.destroy()
    print("SELECTED: " + selected_name)


def select_question():
    global root
    root = Tk()
    root.configure(background=gray)
    w = 600
    h = 450
    root.geometry("600x431")
    root.resizable = False
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    global listbox
    listbox = Listbox(root, width=20, height=30, yscrollcommand=scrollbar.set, font=('Monospaced', 18),
                      background=dark_gray, foreground=light_gray)

    global database_connection
    database_connection = DatabaseConnection()

    global questions
    questions = database_connection.get_all_questions()
    print(questions)
    for i in questions:
        listbox.insert(END, i)
    listbox.pack(side=RIGHT, fill=BOTH)

    scrollbar.config(command=listbox.yview)

    global see_description
    see_description = Button(root, font=('Monospaced', 18), width=32, text="See description", command=get_description)
    see_description.pack(side=TOP)

    global description
    description = Label(root, font=('Monospaced', 18), width=32, height=16, background=light_gray, foreground=dark_gray)
    description.pack(side=TOP)

    global select
    select = Button(root, font=('Monospaced', 18), width=32, text="Select question", state=DISABLED, command=choose_selected)
    select.pack(side=TOP)
    root.mainloop()

select_question()

