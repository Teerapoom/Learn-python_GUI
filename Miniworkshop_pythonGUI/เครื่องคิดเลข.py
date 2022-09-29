from tkinter import *
root = Tk()
root.title("เครื่องคิดเลข")

# เเสดงผล 5 x 4
display = Entry(font=('aroal',30,'bold'),fg="white",bg="green")
display.grid(columnspan=4)

# รับค่าผ่านปุ่น


# row1
btn7 = Button(fg="black",font=("aroal",30,'bold'),text="7",padx=30,pady=15).grid(row=1,column=0)
btn8 = Button(fg="black",font=("aroal",30,'bold'),text="8",padx=30,pady=15).grid(row=1,column=1)
btn9 = Button(fg="black",font=("aroal",30,'bold'),text="9",padx=30,pady=15).grid(row=1,column=2)
btnc = Button(fg="black",bg="orange",font=("aroal",30,'bold'),text="c",padx=35,pady=15).grid(row=1,column=3)

# row2
btn4 = Button(fg="black",font=("aroal",30,'bold'),text="4",padx=30,pady=15).grid(row=2,column=0)
btn5 = Button(fg="black",font=("aroal",30,'bold'),text="5",padx=30,pady=15).grid(row=2,column=1)
btn9 = Button(fg="black",font=("aroal",30,'bold'),text="6",padx=30,pady=15).grid(row=2,column=2)
btnplus = Button(fg="black",bg="orange",font=("aroal",30,'bold'),text="+",padx=40,pady=15).grid(row=2,column=3)

# row3
btn1 = Button(fg="black",font=("aroal",30,'bold'),text="1",padx=30,pady=15).grid(row=3,column=0)
btn2 = Button(fg="black",font=("aroal",30,'bold'),text="2",padx=30,pady=15).grid(row=3,column=1)
btn3 = Button(fg="black",font=("aroal",30,'bold'),text="3",padx=30,pady=15).grid(row=3,column=2)
btnminus = Button(fg="black",bg="orange",font=("aroal",30,'bold'),text="-",padx=40,pady=15).grid(row=3,column=3)

# row4
btndot = Button(fg="black",font=("aroal",30,'bold'),text=".",padx=30,pady=15).grid(row=4,column=0)
btn0 = Button(fg="black",font=("aroal",30,'bold'),text="0",padx=30,pady=15).grid(row=4,column=1)
btndivision = Button(fg="black",bg="orange",font=("aroal",30,'bold'),text="/",padx=35,pady=15).grid(row=4,column=2)
btnmultiply = Button(fg="black",bg="orange",font=("aroal",30,'bold'),text="x",padx=35,pady=15).grid(row=4,column=3)


# row5
btnqual = Button(fg="black",bg="green",font=("aroal",30,'bold'),text="=",padx=95,pady=15).grid(row=5,column=0,columnspan=2)
btnopne = Button(fg="black",bg="orange",font=("aroal",30,'bold'),text="(",padx=35,pady=15).grid(row=5,column=2)
btnclose = Button(fg="black",bg="orange",font=("aroal",30,'bold'),text=")",padx=35,pady=15).grid(row=5,column=3)



root.mainloop()