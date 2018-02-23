from tkinter import *
from tkinter import messagebox
import time
import webbrowser



def go_to_sleep(t):
	time.sleep(t*60)

def startFunction(event=None):
    work_time = workVar.get()
    break_time = workVar.get()
    how_many = howVar.get()
    i = 1

    while i <= how_many:
        print()
        webbrowser.open("work.html")
        print("WORK >> Start time: " + time.ctime())        
        go_to_sleep(work_time)
        print("WORK >> End time: " + time.ctime())
        print()
    	webbrowser.open("break.html")
        print("BREAK >> Start time: " + time.ctime())
        go_to_sleep(break_time)
        print("BREAK >> End time: " + time.ctime())
        i += 1


root = Tk()

workVar = IntVar()
breakVar = IntVar()
howVar = IntVar()


label1 = Label(root, text="Work Time*:")
label1.pack(side=LEFT)
workTimeEntry = Entry(root, textvariable=workVar)
workTimeEntry.pack(side=LEFT)


label2 = Label(root, text="Break Time*:")
label2.pack(side=LEFT)
breakTimeEntry = Entry(root, textvariable=breakVar)
breakTimeEntry.pack(side=LEFT)

label4 = Label(root, text="Repetition Times:")
label4.pack(side=LEFT)
howTimeEntry = Entry(root, textvariable=howVar)
howTimeEntry.pack(side=LEFT)

startButton = Button(root, text="Go!!!", )
startButton.bind("<Button-1>", startFunction)
startButton.pack()

label3 = Label(root, text="* Time in minutes")
label3.pack(side=LEFT)

root.mainloop()
