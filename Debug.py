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
