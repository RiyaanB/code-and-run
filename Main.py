from tkinter import *
from time import sleep

dark_gray = "#1e1e1e"
gray = "#3f3f3f"
light_gray = "#6f6f6f"
white = "#ffffff"

instruction_label = None
var = None
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
    welcome_label.place(x=300, y=50, anchor=CENTER)

    py_image = PhotoImage(file="python_icon.gif")
    python_button = Button(root, height=200, width=200, image=py_image, command=chose_python)
    python_button.place(x=75, y=115)

    java_image = PhotoImage(file="java_icon.gif")
    java_button = Button(root, height=200, width=200, image=java_image, command=chose_java)
    java_button.place(x=325, y=115)

    question_label = Label(root, text="Which language will you use?", font=('Monospaced', 40),
                           background=gray, foreground=dark_gray)
    question_label.place(x=300, y=375, anchor=CENTER)

    root.mainloop()


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

    python_dark_icon = PhotoImage(file="python_dark_icon.gif")
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
    for window in windows:
        window.destroy()

    root = Tk()
    windows = [root]

    print("Chose java")

startup()
