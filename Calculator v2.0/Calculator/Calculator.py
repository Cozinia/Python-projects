
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Calculus-developed by CM")
root.iconbitmap(r'C:\Users\Cozinia\source\repos\Calculator v2.0\logo.ico')
root.geometry("438x327")
root.resizable(False, False)
#initialize width & hight

#sqrt button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\sqrt(x).png')
# The (450, 350) is (height, width)
sqrt = image.resize((70, 60), Image.ANTIALIAS)
my_sqrt = ImageTk.PhotoImage(sqrt)
label_sqrt = Label(image = my_sqrt)

#exonent button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\exponent.png')
# The (450, 350) is (height, width)
exponent = image.resize((70, 60), Image.ANTIALIAS)
my_exponent = ImageTk.PhotoImage(exponent)
label_exponent = Label(image = my_exponent)

#log button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\log(x).png')
# The (450, 350) is (height, width)
log = image.resize((70, 60), Image.ANTIALIAS)
my_log = ImageTk.PhotoImage(log)

#mod button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\mod.png')
# The (450, 350) is (height, width)
mod = image.resize((70, 60), Image.ANTIALIAS)
my_mod = ImageTk.PhotoImage(mod) 

#div button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\div.png')
# The (450, 350) is (height, width)
div = image.resize((70, 60), Image.ANTIALIAS)
my_div = ImageTk.PhotoImage(div)

#add button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\add.png')
# The (450, 350) is (height, width)
add = image.resize((70, 60), Image.ANTIALIAS)
my_add = ImageTk.PhotoImage(add)

#subtract button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\subtract.png')
# The (450, 350) is (height, width)
subtract = image.resize((70, 60), Image.ANTIALIAS)
my_subtract = ImageTk.PhotoImage(subtract)

#multiply button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\multiply.png')
# The (450, 350) is (height, width)
multiply = image.resize((70, 60), Image.ANTIALIAS)
my_multiply = ImageTk.PhotoImage(multiply)

#divide button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\divide.png')
# The (450, 350) is (height, width)
divide = image.resize((70, 60), Image.ANTIALIAS)
my_divide = ImageTk.PhotoImage(divide)

#clear button
image = Image.open(r'C:\Users\Cozinia\source\repos\Calculator v2.0\Calculator\clear.png')
# The (450, 350) is (height, width)
clear = image.resize((70, 60), Image.ANTIALIAS)
my_clear = ImageTk.PhotoImage(clear)

#Input the numbers into the box
def action(number):
    current=input.get()
    input.delete(0,END)
    input.insert(0,str(current)+str(number))

 #Clear function
def clear():
     input.delete(0,END)
#add function
def add():
    num1=input.get()
    global f_num
    global sign
    sign="add"
    f_num=int(num1)
    input.delete(0,END)
    
#subtract function
def subtract():
    num1=input.get()
    global f_num
    global sign
    sign="subtract"
    f_num=int(num1)
    input.delete(0,END)
    
#multilpy function
def multilpy():
    num1=input.get()
    global f_num
    global sign
    sign="multilpy"
    f_num=int(num1)
    input.delete(0,END)
    
#divide function
def divide():
    num1=input.get()
    global f_num
    global sign
    sign="divide"
    f_num=int(num1)
    input.delete(0,END)
def sqrt():
    num1=input.get()
    
    input.delete(0,END)
    input.insert(0,sqrt(num1))
#equal function
def equal():
    num2=input.get()
    input.delete(0,END)

    if sign == "add":
        input.insert(0,f_num + int(num2))

    if sign == "subtract":
        input.insert(0,f_num - int(num2))

    if sign == "multilpy":
        input.insert(0,f_num * int(num2))
    if sign == "divide":
        input.insert(0,f_num / int(num2))
   
        

 #input box    
input=Entry(root,width=13,font=('Arial',28))
input.grid(row=0,column=0,columnspan=3)

#Define buttons
button9=Button(root,text="9",padx=40,pady=20,command=lambda: action(9),bg="black",fg="white")
button8=Button(root,text="8",padx=40,pady=20,command=lambda: action(8),bg="black",fg="white")
button7=Button(root,text="7",padx=40,pady=20,command=lambda: action(7),bg="black",fg="white")
button6=Button(root,text="6",padx=40,pady=20,command=lambda: action(6),bg="black",fg="white")
button5=Button(root,text="5",padx=40,pady=20,command=lambda: action(5),bg="black",fg="white")
button4=Button(root,text="4",padx=40,pady=20,command=lambda: action(4),bg="black",fg="white")
button3=Button(root,text="3",padx=40,pady=20,command=lambda: action(3),bg="black",fg="white")
button2=Button(root,text="2",padx=40,pady=20,command=lambda: action(2),bg="black",fg="white")
button1=Button(root,text="1",padx=40,pady=20,command=lambda: action(1),bg="#000000",fg="white")
button0=Button(root,text="0",padx=40,pady=20,command=lambda: action(0),bg="black",fg="white")

button_add=Button(root,image=my_add,padx=39,pady=20,command=lambda: add(),bg="#66ccff",fg="white")
button_subtract=Button(root,image=my_subtract,padx=40,pady=20,command=lambda: subtract(),bg="#66ccff",fg="white")
button_multilpy=Button(root,imag=my_multiply,padx=40,pady=20,command=lambda: multilpy(),bg="#66ccff",fg="white")
button_divide=Button(root,image=my_divide,padx=40,pady=20,command=lambda: divide(),bg="#66ccff",fg="white")
button_equal=Button(root,text="=",padx=87,pady=20,command=lambda: equal(),bg="#66ccff",fg="white")
button_clear=Button(root,image=my_clear,padx=30,pady=20,command=clear,bg="black",fg="white")

button_sqrt=Button(root,image=my_sqrt,padx=5,pady=2,command=lambda: sqrt(),bg="#54B1F5",fg="white")
button_exponent=Button(root,image=my_exponent,padx=5,pady=2,command=clear,bg="#54B1F5",fg="white")
button_log=Button(root,image=my_log,padx=5,pady=2,command=clear,bg="#54B1F5",fg="white")
button_mod=Button(root,image=my_mod,padx=5,pady=2,command=clear,bg="#54B1F5",fg="white")
button_div=Button(root,image=my_div,padx=5,pady=2,command=clear,bg="#54B1F5",fg="white")

#Define button's grid
button9.grid(row=1,column=0)
button8.grid(row=1,column=1)
button7.grid(row=1,column=2)

button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2)

button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)

button0.grid(row=4,column=0)
button_equal.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=4,column=3)

button_add.grid(row=0,column=3)
button_subtract.grid(row=1,column=3)
button_multilpy.grid(row=2,column=3)
button_divide.grid(row=3,column=3)

button_sqrt.grid(row=0,column=4)
button_exponent.grid(row=1,column=4)
button_log.grid(row=2,column=4)
button_mod.grid(row=3,column=4)
button_div.grid(row=4,column=4)

root.mainloop()

