import os
from tkinter import *
from time import sleep
import time
from tkinter.scrolledtext import ScrolledText
from subprocess import Popen, PIPE
from Database import DatabaseConnection

dark_gray = '#1e1e1e'
gray = '#3f3f3f'
light_gray = '#6f6f6f'
white = '#ffffff'


editor = None
output = None
inputs = None
language = None
name = None

current_question = None
current_description = "Select a question!"

instruction_label = None
window = None

description = None
see_description = None
select = None
database_connection = None
questions = None
listbox = None

o = None
e = None
i = None


def get_description(evt=None):
    selected_name = questions[listbox.curselection()[0]]
    selected_description = database_connection.get_description(selected_name)
    description.config(text=selected_description, wrap=True, wraplength=260)
    select.config(state=NORMAL)


def choose_selected():
    global current_question, current_description
    current_question = questions[listbox.curselection()[0]]
    current_description = database_connection.get_description(current_question)
    window.destroy()
    main_ui((o, e, i))


def select_question():
    root = Tk()
    root.configure(background=gray)
    root.geometry("600x431")
    root.resizable = False

    global window
    global o, e, i
    o = output.get(1.0, END)
    e = editor.get(1.0, END)
    i = inputs.get(1.0, END)
    window.destroy()
    window = root

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    global listbox
    listbox = Listbox(root, width=20, height=30, yscrollcommand=scrollbar.set, font=('Monospaced', 18),
                      background=dark_gray, foreground=light_gray)

    global database_connection
    database_connection = DatabaseConnection() if database_connection is None else database_connection

    global questions
    questions = database_connection.get_all_questions()
    for it in questions:
        listbox.insert(END, it)
    listbox.bind("<<ListboxSelect>>", get_description)
    listbox.pack(side=RIGHT, fill=BOTH)

    scrollbar.config(command=listbox.yview)

    global description
    description = Label(root, font=('Monospaced', 18), width=32, height=17, background=light_gray, foreground=dark_gray)
    description.pack(side=TOP)

    global select
    select = Button(root, font=('Monospaced', 18), width=32, text="Select question", command=choose_selected)
    select.pack(side=TOP)
    root.mainloop()


def close_all_windows():
    try:
        global window
        if window is not None:
            window.destroy()
            window = None
    except:
        pass


def startup():
    global window
    previous_loc = None if window is None else (window.winfo_rootx(), window.winfo_rooty())
    close_all_windows()

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

    welcome_label = Label(root, text='Welcome!', highlightthickness=0, font=('Monospaced', 48),
                          background=gray, foreground=light_gray)
    welcome_label.place(x=300, y=35, anchor=CENTER)

    py_image = PhotoImage(file='images/python_icon.gif')
    python_button = Button(root, height=200, width=200, image=py_image, command=chose_python)
    python_button.place(x=75, y=90)

    java_image = PhotoImage(file='images/java_icon.gif')
    java_button = Button(root, height=200, width=200, image=java_image, command=chose_java)
    java_button.place(x=325, y=90)

    question_label = Label(root, text='Which language will you use?', font=('Monospaced', 40),
                           background=gray, foreground=dark_gray)
    question_label.place(x=300, y=350, anchor=CENTER)

    exit_button = Button(root, text='Exit', width=8, command=close_all_windows, background=dark_gray,
                         font=('Monospaced', 20))
    exit_button.place(x=300, y=415, anchor=CENTER)

    root.mainloop()


def chose_python():
    global language
    language = "python"
    get_name()


def chose_java():
    global language
    language = "java"
    get_name()


def get_name():
    global window
    previous = window.winfo_rootx(), window.winfo_rooty()

    close_all_windows()

    root = Tk()
    root.geometry('%dx%d+%d+%d' % (600, 450, previous[0], previous[1]-22))
    root.configure(background=gray)
    root.resizable = False
    window = root

    if language == "python":
        icon = PhotoImage(file='images/python_icon.gif')
    else:
        icon = PhotoImage(file='images/java_icon.gif')
    image_label = Label(root, image=icon)
    image_label.place(x=300, y=120, anchor=CENTER)

    global name
    name = StringVar()
    file_name = Entry(root, width=25, font=('Monospaced', 28), background=light_gray, foreground='#121212',
                      justify=CENTER, textvariable=name)
    file_name.place(x=300, y=325, anchor=CENTER)

    cancel_button = Button(root, text='Cancel', width=8, command=startup, justify=CENTER, background=dark_gray,
                           font=('Monospaced', 20))
    cancel_button.place(x=135, y=400)

    ok_button = Button(root, text='Continue', width=8, command=verify_name, background=dark_gray,
                       font=('Monospaced', 20))
    ok_button.place(x=335, y=400)

    global instruction_label
    # global language
    if language == "python":
        instruction_label = Label(root, text='Please enter a valid name for your python script',
                                  font=('Monospaced', 26), background=gray, foreground=light_gray)
    else:
        instruction_label = Label(root, text='Please enter a valid Java filename', font=('Monospaced', 26),
                                  background=gray, foreground=light_gray)

    instruction_label.place(x=300, y=250, anchor=CENTER)

    root.mainloop()


def verify_name():
    global language
    if language == "python":
        if len(name.get()) > 3 and name.get()[-3:] == '.py':
            main_ui()
        else:
            name_invalid()
    elif language == "java":
        if len(name.get()) > 5 and name.get()[-5:] == '.java':
            main_ui()
        else:
            name_invalid()


def name_invalid():
    global language
    global instruction_label
    global window
    for a in range(3):
        instruction_label.configure(text='Invalid Filename!!', foreground='#BB5555')
        sleep(0.3)
        window.update()
        instruction_label.configure(text='Invalid Filename!!', foreground=light_gray)
        sleep(0.3)
        window.update()
    if language == "python":
        instruction_label.configure(text='Please enter a valid name for your python script', foreground=light_gray)
    elif language == "java":
        instruction_label.configure(text='Please enter a valid Java filename', foreground=light_gray)


def main_ui(prev=None):
    close_all_windows()
    root = Tk()
    root.configure(background=gray)
    root.resizable = False
    root.geometry('%dx%d+%d+%d' % (1440, 900, 0, 0))

    global window
    window = root

    global editor
    editor = ScrolledText(root, width=64, height=25, font=('Monospaced', 22), background=light_gray,
                          foreground=dark_gray, relief=SUNKEN, undo=True, wrap=WORD)
    editor.place(x=10, y=134)

    if language == "python":
        editor.insert(END, '# Your code goes here')
    elif language == "java":
        editor.insert(END, 'public class ' + name.get()[:-5] + ' {\n        public static void main(String[] args) throws Exception' +
                      '{\n                // Your code goes here\n        }\n}')

    run_button = Button(root, text='Run Code', width=10, command=run_code, background=dark_gray,
                        font=('Monospaced', 20))
    run_button.place(x=955, y=20)

    compile_button = Button(root, text='Compile Code', width=10, command=compile_code, background=dark_gray,
                            font=('Monospaced', 20))
    compile_button.place(x=1120, y=20)

    if language == "python":
        compile_button.config(state=DISABLED)

    check_button = Button(root, text="Check", width=9, command=evaluate_code, background=dark_gray,
                          font=('Monospaced', 20))
    check_button.place(x=1285, y=20)
    check_button.config(state=NORMAL if current_question is not None else DISABLED)

    global output
    output = ScrolledText(root, width=45, height=24, font=('Monospaced', 16), background=dark_gray,
                          foreground=light_gray, relief=SUNKEN, wrap=WORD)
    output.place(x=950, y=64)
    output.insert(END, '\n\tPlease press the run button to execute')

    global inputs
    inputs = ScrolledText(root, width=45, height=13, font=('Monospaced', 16), background=dark_gray,
                          foreground=light_gray, relief=SUNKEN, wrap=WORD)
    inputs.place(x=950, y=562)

    choose_question = Button(root, text='Select Question', width=16, command=select_question, background=dark_gray,
                             font=('Monospaced', 20))
    choose_question.place(x=20, y=6)

    descr = Label(root, width=60, height=5, text=current_description, background=light_gray, foreground=dark_gray,
                  font=('Monospaced', 18), wrap=True, wraplength=640)
    descr.place(x=260, y=6)

    if prev is not None:
        output.delete(1.0, END)
        output.insert(END, prev[0])

        editor.delete(1.0, END)
        editor.insert(END, prev[1])

        inputs.delete(1.0, END)
        inputs.insert(END, prev[2])

    root.mainloop()


def compile_code():
    if language == "java":
        file = open(name.get(), 'w')
        file.write(editor.get(1.0, END)[:-1])
        file.close()
        a = time.clock()
        p = Popen(['javac', name.get()], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate(''.encode('UTF-8'))
        compile_output = stdout.decode('UTF-8') + stderr.decode('UTF-8')
        output.delete(1.0, END)
        output.insert(END, compile_output)
        output.insert(END, 'Compilation ended in ' + str(time.clock() - a) + ' seconds')


def run_code():
    file = open(name.get(), 'w')
    file.write(editor.get(1.0, END)[:-1])
    file.close()
    a = time.clock()
    if language == "python":
        p = Popen(['python3', name.get()], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    elif language == "java":
        p = Popen(['java', name.get()[:-5]], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(inputs.get(1.0, END)[:-1].encode('UTF-8'))
    run_output = stdout.decode('UTF-8') + stderr.decode('UTF-8')
    output.delete(1.0, END)
    output.insert(END, run_output)
    output.insert(END, 'Program ended in ' + str(time.clock() - a) + ' seconds')


def evaluate_code():
    global database_connection
    database_connection = DatabaseConnection() if database_connection is None else database_connection
    test_cases = database_connection.get_testcases(current_question)
    results = []
    for test_case in test_cases:
        file = open(name.get(), 'w')
        file.write(editor.get(1.0, END)[:-1])
        file.close()
        if language == "python":
            p = Popen(['python3', name.get()], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        elif language == "java":
            p = Popen(['java', name.get()[:-5]], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate(test_case.inputs.encode("UTF-8"))
        if stderr.decode("UTF-8") == "":
            if test_case.output == "null":
                results.append(False)
            else:
                results.append(test_case.output == stdout.decode("UTF-8") or test_case.output == stdout.decode("UTF-8")[:-1])
        else:
            results.append(test_case.output == "null")
    output.delete(1.0, END)
    evaluation = ""
    passed = 0
    for result in range(len(results)):
        evaluation += "Test case " + str(result+1) + ": " + ("Passed" if results[result] else "Failed") + "\n"
        passed += 1 if results[result] else 0
    evaluation += "Result: Passed " + str(passed) + "/" + str(len(results)) + "\n"
    output.insert(END, evaluation)


try:
    startup()
finally:
    os.system("rm " + name.get())
    if language == "java":
        os.system("rm " + name.get()[:-4] + "class")

