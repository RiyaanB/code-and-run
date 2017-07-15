"""
from tkinter import *
from threading import Thread

master = Tk()

listbox = Listbox(master)
listbox.pack()

l = ["one", "two", "three", "four"]
for item in l:
    listbox.insert(END, item)

class newThread(Thread):
    def run(self):        
        while True:
            if not len(listbox.curselection()) == 0:
                print(l[listbox.curselection()[0]])

newThread().start()

master.mainloop()
"""
from tkinter import *
from threading import Thread
master = Tk()

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, width=20, height=30, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

class newThread(Thread):
    def run(self):        
        while True:
            if not len(listbox.curselection()) == 0:
                print(listbox.curselection()[0])
newThread().start()
mainloop()
