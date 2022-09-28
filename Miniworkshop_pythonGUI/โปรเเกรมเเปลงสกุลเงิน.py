# 1 บาท = 0.027 ยูโร
# 1 บาท  = 3.80  เยน
# 1 บาท  = 0.026  ดอลล่า
# 1 บาท  = 0.024  ปอนด์

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("โปรเเกรมเเปลงสกุลเงิน")

# Input
money = IntVar()
Label(text="จำนวนเงิน (THB)",font=30,padx=10).grid(row=0,sticky=W)
et1 = Entry(font=30,width=30,textvariable=money).grid(row=0,column=1)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
