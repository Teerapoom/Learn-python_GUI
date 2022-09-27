from tkinter import *
import tkinter.messagebox


root = Tk()
root.title("My GUI")
root.geometry("500x500")

# สร้างเมนู
myMenu = Menu()
root.config(menu = myMenu)

def showWindow():
    window = Tk()
    window.title("หน้าต่างใหม่")
    window.geometry("200x200")
    window.mainloop()

def aboutProgram():
    tkinter.messagebox.showinfo("รายละเอียดโปรเกรม","Teerapoom")

def exitProgram():
    confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรเเกรมหรือไม่ ?")
    if confirm == "yes":
        root.destroy()

# เพิ่มเมนูย่อย (Menu Item)
menuitem = Menu()
menuitem.add_command(label="New Window",command = showWindow) # command => เรียกฟังชั่น
menuitem.add_command(label="Open")
menuitem.add_command(label="Save")
menuitem.add_command(label="About",command = aboutProgram)
menuitem.add_command(label="Exit",command = exitProgram)

# เพิ่มเมนูหลัก
myMenu.add_cascade(label="File",menu=menuitem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="Viwe")


root.mainloop()