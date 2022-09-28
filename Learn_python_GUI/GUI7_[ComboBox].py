from logging import root
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Combo Box")

Label(text="ที่อยู่",font=20).grid(row = 0 , column=0)
choice = StringVar(value="เลือกจังหวัดของคุณ")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("นครราชสีมา","เชียงใหม่","กาญจนบุรี","ตาก","	อุบลราชธานี")
combo.grid(row=0,column=1)

def selectCity():
    Label(text="คุณเลือก= "+choice.get(),font=30).grid(row=2,column=1)

btn = Button(text="ส่งข้อมูล",command=selectCity).grid(row=1,column=1)
# btn.grid(row=1,column=1)


root.mainloop()