from secrets import choice
from tkinter import *
import tkinter.messagebox 

root = Tk()
root.title('Data Entry')
root.geometry("500x500")

Label(text="ชื่อ").grid(row=0)
Label(text="นามสกุล").grid(row=1)
Label(text="เบอร์ติดต่อ").grid(row=2)

et1 = Entry()
et1.grid(row=0,column=1)
et1.insert(0,"Teerapoom")

et2 = Entry()
et2.grid(row=1,column=1)
et2.insert(0,"Ku")

et3 = Entry()
et3.grid(row=2,column=1)
et3.insert(0,"065-3615xxx")

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)

Button = Button(text="ล้างข้อมูล",command=deleteText).grid(row=3,column=1)



root.mainloop()