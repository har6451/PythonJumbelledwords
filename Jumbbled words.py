import tkinter
from tkinter import *
from tkinter import messagebox
import random

answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]


num = random.randrange(0,7,1)
root = tkinter.Tk()
root.title("Jumbbeled words by Harshit")
root.configure(background="Pink")

def harshit():
    global words , answers , num
    lbl.configure(text = words[num] )


lbl = Label(
    root,
    text="Word",
    font=("Times New Roman", 16),
)
lbl.pack()

ans1 = StringVar()
e1 = Entry(
    root,
    font=("Times New Roman", 16),
    textvariable = ans1,
)
e1.pack()

def checkanswer ():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        reset()
    else:
        messagebox.showerror("Error", "This is not Correct")
        e1.delete(0, END)
    
btn = Button(
    root,
    font=("Comic sans ms ", 12),
    text="GO",
    fg="Purple",
    relief = GROOVE,
    command  = checkanswer,  
)
btn.pack()

def reset():
    num = random.randrange(0, len(words), 1)
    lbl.config(text = words[num])
    e1.delete(0, END)

btn2 = Button(
    root,
    font=("Comic sans ms ", 12),
    fg="Blue",
    text="CHANGE",
    relief = GROOVE, 
    command = reset,
)
btn2.pack()

harshit()
root.mainloop()











