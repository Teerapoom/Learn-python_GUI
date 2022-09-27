from secrets import choice
from tkinter import *
import tkinter.messagebox 

root = Tk()
root.title('My Gui')
root.geometry("500x500")

def showChoices():
    print(language1.get(),language2.get(),language3.get(),language4.get())
    Choices1 = language1.get()
    Choices2 = language2.get()
    Choices3 = language3.get()
    Choices4 = language4.get()
    if Choices1 == 1 :
        Label(text="เลือกภาษา python").pack(anchor=W)
    if Choices2 == 1 :
        Label(text="เลือกภาษา Java").pack(anchor=W)
    if Choices3 == 1 :
        Label(text="เลือกภาษา PHP").pack(anchor=W)
    if Choices4 == 1 :
        Label(text="เลือกภาษา C#").pack(anchor=W)


# 0 = ไม่ได้เลือกตัวเลือก , 1 = เลือกตัวเลือก
language1 = IntVar()
Checkbutton(text="Python",variable=language1).pack(anchor=W)

language2 = IntVar()
Checkbutton(text="Java",variable=language2).pack(anchor=W)

language3 = IntVar()
Checkbutton(text="PHP",variable=language3).pack(anchor=W)

language4 = IntVar()
Checkbutton(text="C#",variable=language4).pack(anchor=W)

Button(text="เเสดงตัวเลือก",command=showChoices).pack(anchor=W)
root.mainloop()