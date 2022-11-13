from tkinter import *
import math

expression = ''

#str(eval())
def press(num):
    global expression
    
    expression = expression + str(num)
    print(expression)

def equal():
    global expression
    
    ans = str(eval(expression))
    print(ans)

window = Tk()  
window.title("Виджеты") 
window.geometry('250x300')
window['bg']='#125'
f_top = Frame(window)

l=Label(window,text='',)
l.pack()

b1 =Button(window,text='1',bg='orange',command=lambda:press(1)).place(x=100,y=30)
b2 =Button(window,text='2',bg='orange',command=lambda:press(2)).place(x=120,y=30)
b3 =Button(window,text='3',bg='orange',command=lambda:press(3)).place(x=140,y=30)
b4 =Button(window,text='4',bg='orange',command=lambda:press(4)).place(x=100,y=60)
b5 =Button(window,text='5',bg='orange',command=lambda:press(5)).place(x=120,y=60)
b6 =Button(window,text='6',bg='orange',command=lambda:press(6)).place(x=140,y=60)
b7 =Button(window,text='7',bg='orange',command=lambda:press(7)).place(x=100,y=90)
b8 =Button(window,text='8',bg='orange',command=lambda:press(8)).place(x=120,y=90)
b9 =Button(window,text='9',bg='orange',command=lambda:press(9)).place(x=140,y=90)
b0 =Button(window,text='0',bg='orange',command=lambda:press(0)).place(x=120,y=120)

a = Button(window,text='+',bg='orange',command=lambda: press('+')).place(x=170,y=30)
#a1 = Button(window,text='+',bg='orange',command=lambda: equal()).place(x=170,y=60)
b = Button(window,text='-',bg='orange',command=lambda: press('-')).place(x=170,y=60)
c = Button(window,text='*',bg='orange',command=lambda: press('*')).place(x=170,y=90)
d = Button(window,text=':',bg='orange',command=lambda: press('/')).place(x=170,y=120)
e = Button(window,text='=',bg='orange',command=lambda: equal()).place(x=170,y=150)


















window.mainloop()