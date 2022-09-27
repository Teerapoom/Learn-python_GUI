from email.mime import message
from tkinter import * 

root = Tk()
root.title("my gui")

# กำหนดขนาดหน้าจอเเละตำเเหน่งหน้าจอ
root.geometry("500x500") #ขนากจอด้วย Geometry



#ใส่ข้อความในหน้าจอ pack ตรงกลาง
# myLabel1 = Label(root, text="Hello Word", fg = "red" ,font=20 , bg = "yellow").grid(row=3,column=10)
# myLabel2 = Label(root,text="Teerapoom", fg = "green",bg="red",font=30).place(x=50,y=200)
myLabel1 = Label(root, text="Hello Word", fg = "red" ,font=20 , bg = "yellow").pack()


def openWindow():
    # หน้าจอที่สอง
    myWindow = Tk()
    myWindow.title("รายงานผลการทำงาน")
    myWindow.geometry("500x300") 

def showMessage():
    # print("Hello World")
    message = txt.get() # get เป็นการดึงค่าออกมา
    # print(message)
    Label(root, text=message, fg = "red" ,font=20 , bg = "yellow").pack()

# กล่องข้อความ
txt = StringVar() # เก็บที่พิมมาเป็น str
myText = Entry(root,textvariable=txt).pack() #เรียกใช้กล่องข้อความ

# ใส่ปุ่ม
btn1 = Button(root, text="บันทึก" ,fg = "white", bg = "green", command = showMessage ).pack() # command เรียกใช้ def 
btn2 = Button(root, text="ยกเลิก" ,fg = "white", bg = "red").pack()
btn3 = Button(root, text="เปิดรายงาน" ,fg = "white", bg = "green", command = openWindow).pack() 

root.mainloop()

