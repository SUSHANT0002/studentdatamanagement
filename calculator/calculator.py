from tkinter import*
from tkinter import messagebox
import math

screen = Tk()
screen.title('calculator-1')
screen.maxsize(height=373,width=335)
screen.minsize(height=373,width=265)
screen.configure(bg='black')
screen.iconbitmap('D:\python\projects')
screen.geometry('265x373')

def click(number):
    global operator
    operator += str( number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    try:
        result =eval(operator)
        operator =str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification','Try again something is wrong here')



tex = StringVar()
operator = ''

entry1 = Entry(screen,bg='orange',font=('arial',15,"italic bold"),bd='23',justify='right',textvariable=tex  )
entry1.grid(row=0,columnspan=4)

btn7 =Button(screen,text="7",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(7),fg='green',activebackground='violet',activeforeground='orange')
btn7.grid(row=1,column=0)

btn8 =Button(screen,text="8",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(8),fg='green',activebackground='indigo',activeforeground='orange')
btn8.grid(row=1,column=1)

btn9 =Button(screen,text="9",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(9),fg='green',activebackground='blue',activeforeground='orange')
btn9.grid(row=1,column=2)

btnadd =Button(screen,text="+",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click('+'),fg='green',activebackground='green',activeforeground='orange')
btnadd.grid(row=1,column=3)


btn4 =Button(screen,text="4",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(4),fg='green',activebackground='yellow',activeforeground='orange')
btn4.grid(row=2,column=0)

btn5 =Button(screen,text="5",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(5),fg='green',activebackground='orange',activeforeground='dark blue')
btn5.grid(row=2,column=1)

btn6 =Button(screen,text="6",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(6),fg='green',activebackground='red',activeforeground='orange')
btn6.grid(row=2,column=2)

btnsub =Button(screen,text="-",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=13,pady=10,command=lambda:click('-'),fg='green',activebackground='yellow',activeforeground='orange')
btnsub.grid(row=2,column=3)


btn3 =Button(screen,text="3",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(3),fg='green',activebackground='yellow',activeforeground='orange')
btn3.grid(row=3,column=0)

btn2 =Button(screen,text="2",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(2),fg='green',activebackground='yellow',activeforeground='orange')
btn2.grid(row=3,column=1)

btn1 =Button(screen,text="1",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(1),fg='green',activebackground='yellow',activeforeground='orange')
btn1.grid(row=3,column=2)

btnmul =Button(screen,text="x",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=11,pady=10,command=lambda:click('*'),fg='green',activebackground='yellow',activeforeground='orange')
btnmul.grid(row=3,column=3)

btnclear =Button(screen,text="cl",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=clear,fg='green',activebackground='yellow',activeforeground='orange')
btnclear.grid(row=4,column=0)

btnequal =Button(screen,text="=",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=equal,fg='green',activebackground='yellow',activeforeground='orange')
btnequal.grid(row=4,column=1)

btn0 =Button(screen,text="0",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=10,pady=10,command=lambda:click(0),fg='green',activebackground='yellow',activeforeground='orange')
btn0.grid(row=4,column=2)

btndiv =Button(screen,text="/",font=('arial',15,'italic bold'),bg='light blue',bd='10',padx=13,pady=10,command=lambda:click('/'),fg='green',activebackground='yellow',activeforeground='orange')
btndiv.grid(row=4,column=3)

###############################advance fun
def prsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong here')

def prcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong here')

def prtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong here')

def prsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong here')

def prlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong here')

btnsin =Button(screen,text="sin",font=('arial',13,'italic bold'),bg='light blue',bd='12',padx=7,pady=14,command=prsin,fg='green',activebackground='yellow',activeforeground='orange')
btnsin.grid(row=0,column=4)

btncos =Button(screen,text="cos",font=('arial',13,'italic bold'),bg='light blue',bd='12',padx=7,pady=12,command=prcos,fg='green',activebackground='yellow',activeforeground='orange')
btncos.grid(row=1,column=4)

btnTan =Button(screen,text="Tan",font=('arial',13,'italic bold'),bg='light blue',bd='12',padx=6,pady=11,command=prtan,fg='green',activebackground='yellow',activeforeground='orange')
btnTan.grid(row=2,column=4)

btnsqrt =Button(screen,text="Sqrt",font=('arial',13,'italic bold'),bg='light blue',bd='12',padx=5,pady=12,command=prsqrt,fg='green',activebackground='yellow',activeforeground='orange')
btnsqrt.grid(row=3,column=4)

btnLog=Button(screen,text="Log",font=('arial',13,'italic bold'),bg='light blue',bd='12',padx=5,pady=11,command=prlog,fg='green',activebackground='yellow',activeforeground='orange')
btnLog.grid(row=4,column=4)



screen.mainloop()


