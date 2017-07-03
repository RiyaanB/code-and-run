from tkinter import *

dark_gray = "#1e1e1e"
gray = "#3f3f3f"
light_gray = "#6f6f6f"
white = "#ffffff"

windows = []


def startup():
    root = Tk()
    root.configure(background=gray)
    root.geometry("600x450")
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
    for window in windows:
        window.destroy()
    root = Tk()
    windows = [root]

    print("Chose python")


def chose_java():
    global windows
    for window in windows:
        window.destroy()

    root = Tk()
    windows = [root]

    print("Chose java")

startup()
