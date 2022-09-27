from logging import root
from tkinter import *
root = Tk()
root.title("โปรเเกรมคำนวณพื้นที่สามเหลี่ยม")

# พื้นที่สามเหลี่ยม = 1/2 x ฐาน x สูง.

Label(text="ฐาน",font=30).grid(row=0,sticky=W)
base = IntVar()
et1 = Entry(width=30,font=30,textvariable=base)
et1.grid(row=0,column=1)

Label(text="สูง",font=30).grid(row=1,sticky=W)
high = IntVar()
et2 = Entry(width=30,font=30,textvariable=high)
et2.grid(row=1,column=1)

Label(text="พื้นที่สามเหลี่ยม",font=30).grid(row=2,sticky=W)
et3 = Entry(width=30,font=30)
et3.grid(row=2,column=1)

def calculate():
    et3.delete(0,END)
    B = base.get()
    H = high.get()
    sum = 0.5*B*H
    et3.insert(0,sum)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)

btn1 = Button(text="คำนวณ",command=calculate).grid(row=3,column=1,sticky=W)
btn2 = Button(text="ลบข้อมูล",command=deleteText).grid(row=3,column=1,sticky=E)



root.mainloop()