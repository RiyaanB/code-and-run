from tkinter import *
from tkinter.scrolledtext import ScrolledText
from time import sleep
import time
import subprocess
import traceback

dark_gray = "#1e1e1e"
gray = "#3f3f3f"
light_gray = "#6f6f6f"
white = "#ffffff"

instruction_label = None
var = None
py_editor = None
py_output = None
java_editor = None
java_output = None
windows = []


def startup():
    global windows
    previous_loc = None if len(windows) == 0 else (windows[-1].winfo_rootx(), windows[-1].winfo_rooty())

    for window in windows:
        window.destroy()
    windows = []
    root = Tk()
    root.configure(background=gray)
    w = 600
    h = 450
    if previous_loc is None:
        x = (root.winfo_screenwidth()/2) - (w/2)
        y = (root.winfo_screenheight()/2) - (h/2) - 100
    else:
        x, y = previous_loc
    root.geometry('%dx%d+%d+%d' % (w, h, x, y - 22))
    root.resizable(False, False)

    windows.append(root)

    welcome_label = Label(root, text="Welcome!", highlightthickness=0, font=('Monospaced', 48),
                          background=gray, foreground=light_gray)
    welcome_label.place(x=300, y=35, anchor=CENTER)

    py_image = PhotoImage(file="images/python_icon.gif")
    python_button = Button(root, height=200, width=200, image=py_image, command=chose_python)
    python_button.place(x=75, y=90)

    java_image = PhotoImage(file="images/java_icon.gif")
    java_button = Button(root, height=200, width=200, image=java_image, command=chose_java)
    java_button.place(x=325, y=90)

    question_label = Label(root, text="Which language will you use?", font=('Monospaced', 40),
                           background=gray, foreground=dark_gray)
    question_label.place(x=300, y=350, anchor=CENTER)

    exit_button = Button(root, text="Exit", width=8, command=close_all, background=dark_gray,
                         font=('Monospaced', 20))
    exit_button.place(x=300, y=415, anchor=CENTER)

    root.mainloop()


def close_all():
    global windows
    for window in windows:
        window.destroy()
    quit()


def chose_python():
    global windows
    previous = windows[-1].winfo_rootx(), windows[-1].winfo_rooty()

    for window in windows:
        window.destroy()

    print("Chose python")

    root = Tk()
    root.geometry('%dx%d+%d+%d' % (600, 450, previous[0], previous[1]-22))
    root.configure(background=gray)
    root.resizable = False
    windows = [root]

    python_dark_icon = PhotoImage(file="images/python_dark_icon.gif")
    image_label = Label(root, image=python_dark_icon)
    image_label.place(x=300, y=120, anchor=CENTER)

    global var
    var = StringVar()
    file_name = Entry(root, width=25, font=('Monospaced', 28), background=light_gray, foreground="#121212",
                      justify=CENTER, textvariable=var)
    file_name.place(x=300, y=325, anchor=CENTER)

    cancel_button = Button(root, text="Cancel", width=8, command=startup, justify=CENTER, background=dark_gray,
                           font=('Monospaced', 20))
    cancel_button.place(x=135, y=400)

    ok_button = Button(root, text="Continue", width=8, command=continue_python, background=dark_gray,
                       font=('Monospaced', 20))
    ok_button.place(x=335, y=400)

    global instruction_label
    instruction_label = Label(root, text="Please enter a valid name for your python script", font=('Monospaced', 26),
                              background=gray, foreground=light_gray)
    instruction_label.place(x=300, y=250, anchor=CENTER)

    root.mainloop()


def continue_python():
    if len(var.get()) > 3 and var.get()[-3:] == ".py":
        instruction_label.configure(text="So \"" + var.get() + "\" it is!", foreground="#FFFFFF")
        global windows
        for window in windows:
            window.destroy()
        root = Tk()
        root.configure(background=gray)
        root.resizable = False
        root.geometry('%dx%d+%d+%d' % (root.winfo_screenwidth(), root.winfo_screenheight(), 0, 0))

        global py_editor
        py_editor = ScrolledText(root, width=64, height=29, font=('Monospaced', 22), background=light_gray,
                                 foreground=dark_gray, relief=SUNKEN, undo=True, wrap=WORD)
        py_editor.place(x=10, y=10)

        run_button = Button(root, text="Run Code", width=32, command=run_python, background=dark_gray,
                            font=('Monospaced', 20))
        run_button.place(x=950, y=20)

        global py_output
        py_output = ScrolledText(root, width=45, height=38, font=('Monospaced', 16), background=dark_gray,
                                 foreground=light_gray, relief=SUNKEN, wrap=WORD)
        py_output.place(x=950, y=64)

        root.mainloop()

        windows = [root]
    else:
        instruction_label.configure(text="Invalid Filename!!", foreground="#BB5555")
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground=light_gray)
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground="#BB5555")
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground=light_gray)
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground="#BB5555")
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground=light_gray)
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Please enter a valid name for your python script", foreground=light_gray)


def chose_java():
    global windows
    previous = windows[-1].winfo_rootx(), windows[-1].winfo_rooty()

    for window in windows:
        window.destroy()

    print("Chose Java")

    root = Tk()
    root.geometry('%dx%d+%d+%d' % (600, 450, previous[0], previous[1]-22))
    root.configure(background=gray)
    root.resizable = False
    windows = [root]

    java_icon = PhotoImage(file="images/java_icon.gif")
    image_label = Label(root, image=java_icon)
    image_label.place(x=300, y=120, anchor=CENTER)

    global var
    var = StringVar()
    file_name = Entry(root, width=25, font=('Monospaced', 28), background=light_gray, foreground="#121212",
                      justify=CENTER, textvariable=var)
    file_name.place(x=300, y=325, anchor=CENTER)

    cancel_button = Button(root, text="Cancel", width=8, command=startup, justify=CENTER, background=dark_gray,
                           font=('Monospaced', 20))
    cancel_button.place(x=135, y=400)

    ok_button = Button(root, text="Continue", width=8, command=continue_java, background=dark_gray,
                       font=('Monospaced', 20))
    ok_button.place(x=335, y=400)

    global instruction_label
    instruction_label = Label(root, text="Please enter a valid name for your main Java class", font=('Monospaced', 26),
                              background=gray, foreground=light_gray)
    instruction_label.place(x=300, y=250, anchor=CENTER)

    root.mainloop()


def run_python():
    file = open(var.get(), "w")
    file.write(py_editor.get(1.0, END)[:-1])
    file.close()
    a = time.clock()
    try:
        output = subprocess.check_output(["python3", var.get()]).decode("UTF-8")
    except subprocess.CalledProcessError:
        output = traceback.format_exc()
    py_output.delete(1.0, END)
    py_output.insert(END, output)
    py_output.insert(END, "Program ended in " + str(time.clock()-a) + " seconds")


def continue_java():
    if len(var.get()) > 5 and var.get()[-5:] == ".java":
        instruction_label.configure(text="So \"" + var.get() + "\" it is!", foreground="#FFFFFF")
        global windows
        for window in windows:
            window.destroy()
        root = Tk()
        root.configure(background=gray)
        root.resizable = False
        root.geometry('%dx%d+%d+%d' % (root.winfo_screenwidth(), root.winfo_screenheight(), 0, 0))

        global java_editor
        java_editor = ScrolledText(root, width=64, height=29, font=('Monospaced', 22), background=light_gray,
                                   foreground=dark_gray, relief=SUNKEN, undo=True, wrap=WORD)
        java_editor.place(x=10, y=10)

        run_button = Button(root, text="Run Code", width=32, command=run_java, background=dark_gray,
                            font=('Monospaced', 20))
        run_button.place(x=950, y=20)

        global java_output
        java_output = ScrolledText(root, width=45, height=38, font=('Monospaced', 16), background=dark_gray,
                                   foreground=light_gray, relief=SUNKEN, wrap=WORD)
        java_output.place(x=950, y=64)

        root.mainloop()

        windows = [root]
    else:
        instruction_label.configure(text="Invalid Filename!!", foreground="#BB5555")
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground=light_gray)
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground="#BB5555")
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground=light_gray)
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground="#BB5555")
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Invalid Filename!!", foreground=light_gray)
        sleep(0.3)
        windows[-1].update()
        instruction_label.configure(text="Please enter a valid name for the main java class", foreground=light_gray)


def run_java():
    file = open(var.get(), "w")
    file.write(java_editor.get(1.0, END)[:-1])
    file.close()
    a = time.clock()
    try:
        subprocess.check_output(["javac", var.get()]).decode("UTF-8")
        output = subprocess.check_output(["java", var.get()[:-5]]).decode("UTF-8")
    except subprocess.CalledProcessError:
        output = traceback.format_exc()
    java_output.delete(1.0, END)
    java_output.insert(END, output)
    java_output.insert(END, "Program ended in " + str(time.clock()-a) + " seconds")


startup()
