from tkinter import *
from turtle import width


root = Tk()
root.title("Calculadora simples")

#functions

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add(signal):
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    global sign
    sign = signal

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    global f_num
    if sign == "+":
        result = e.insert(0, f_num + int(second_number))
        f_num = result
    elif sign == "-":
        result = e.insert(0, f_num - int(second_number))
        f_num = result
    elif sign == "x":
        result = e.insert(0, f_num * int(second_number))
        f_num = result
    elif sign == "/":
        result = e.insert(0, f_num / int(second_number))
        f_num = result






#


e = Entry(root, borderwidth=5, font="default 15")
e.grid(row = 0, column= 0, columnspan=4, padx = 10, pady=10, sticky="we")

# buttons

button9 = Button(root, 
text="9",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(9))

button8 = Button(root, 
text="8",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(8))

button7 = Button(root,
text="7",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(7))

button6 = Button(root, 
text="6",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(6))

button5 = Button(root, 
text="5",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(5))

button4 = Button(root, 
text="4",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(4))

button3 = Button(root, 
text="3",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(3))

button2 = Button(root, 
text="2",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(2))

button1 = Button(root, 
text="1",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(1))

button0 = Button(root, 
text="0",
bd=5,
relief="raised",
font="default 20",
width=3,
height = 2,
command= lambda: button_click(0))

# end of number buttons
# start of simbols

simbol1 = Button(root,
text="x",
bd=5, 
relief="raised", 
font="default 20",
width=3,
command= lambda: button_add("x"))

simbol2 = Button(root,
text="+",
bd=5, 
relief="raised", 
font="default 20",
width=3,
height= 2,
command= lambda: button_add("+"))

simbol3 = Button(root,
text="-",
bd=5, 
relief="raised", 
font="default 20",
width=3,
command= lambda: button_add('-'))

simbol4 = Button(root,
text="/",
bd=5, 
relief="raised", 
font="default 20",
width=3,
height = 2,
command= lambda: button_add("/"))

simbol6 = Button(root,
text=",",
bd=5, 
height = 2,
relief="raised", 
font="default 20",
width=3,
command= lambda: button_click())

simbol5 = Button(root,
text="=",
bd=5, 
relief="raised", 
font="default 20",
width=3, 
height=2,
command= button_equal)

clearbutton = Button(root, 
text="Clear", 
bd=5,
relief="raised",
font="default 20", 
width=3,
command= lambda: button_clear())


#layout
button9.grid(row=2, column=0)
button8.grid(row=2, column= 1)
button7.grid(row=2, column= 2)
button6.grid(row=3, column=0)
button5.grid(row=3, column=1)
button4.grid(row=3, column= 2)
button3.grid(row=4, column= 0)
button2.grid(row = 4, column= 1)
button1.grid(row= 4, column= 2)
button0.grid(row= 5, columnspan=2, sticky="we") 
simbol5.grid(row=5, column=2, columnspan=2, sticky='we')
simbol6.grid(row=4, column=3)
simbol2.grid(row= 3, column=3)
simbol4.grid(row=2, column=3)
simbol3.grid(row=1, column= 3)
simbol1.grid(row=1, column=2)
clearbutton.grid(row=1, columnspan=2, sticky="we")

root.mainloop()