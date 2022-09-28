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
et1 = Entry(font=30,width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(text="เลือกสกุลเงิน",font=30,padx=10).grid(row=1,sticky=W)
combo = ttk.Combobox(width=30,font=30,textvariable=choice)
combo["value"] = ("EUR","JPY","USD","GBP")
combo.grid(row=1,column=1)

# Output
Label(text="ผลการคำนวณ",font=30,padx=10).grid(row=1,sticky=W)
et2 = Entry(width=30,font=30)
et2.grid(row=2,column=1)

def calculate():
    amount = money.get()
    currency = choice.get()
    
    if currency == "EUR":
        et2.delete(0,END)
        result = ((amount*0.027),"EUR(ยูโร)")
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result = ((amount*3.80),"JPY(เยน)")
        et2.insert(0,result)
    elif currency == "USD":
        et2.delete(0,END)
        result = ((amount*0.026),"USD(ดอลล่า)")
        et2.insert(0,result)
    elif currency == "GBP":
        et2.delete(0,END)
        result = ((amount*0.024),"GBP(ปอนด์)")
        et2.insert(0,result)
    else:
        et2.delete(0,END)
        result = ("ไม่พบข้อมูล")
        et2.insert(0,result)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)


btn = Button(text="คำนวณ",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W)
btn = Button(text="ลบข้อมูล",font=30,width=15,command=deleteText).grid(row=3,column=1,sticky=E)


root.mainloop()
