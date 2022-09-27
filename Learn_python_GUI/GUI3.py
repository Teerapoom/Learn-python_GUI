from tkinter import *
# import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectcolor():
    color = askcolor()
    mylabel = Label(text="Hello Python",bg = color[1], font=30).pack()

def selectfile():
    # fileopen = askopenfile() #ตำเเหน่ง
    fileopen = askopenfilename()
    filecontent = open(fileopen,encoding='utf-8') 
    mylabel = Label(text=filecontent.read()).pack()

btn1 = Button(text="เลือกสี" , command= selectcolor).pack()
btn1 = Button(text="เลือกไฟล์" , command= selectfile).pack()
root.mainloop()