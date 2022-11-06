from tkinter import *   

def A():
    lbl.configure(text= 'red', foreground = 'red')
def B():
    lbl.configure(text= 'orange', foreground = 'orange')
def C():
    lbl.configure(text= 'yellow', foreground = 'yellow')
def D():
    lbl.configure(text= 'green', foreground = 'green')
def E():
    lbl.configure(text= 'blue', foreground = 'blue')
  
window = Tk()  
window.title("Заданиe1") 
window.geometry('500x500')
window.background='black'
f_top = Frame(window)

lbl=Label(window, text='?', font=('', 30))

btn1=Button(window, width=7, height=2,text='', bg='red', command=A).place(x=110,y=60)
btn2=Button(window, width=7, height=2,text='', bg='orange', command=B).place(x=165,y=60)
btn3=Button(window, width=7, height=2,text='', bg='yellow', command=C).place(x=220,y=60)
btn4=Button(window, width=7, height=2,text='', bg='green', command=D).place(x=275,y=60)
btn5=Button(window, width=7, height=2,text='', bg='blue', command=E).place(x=330,y=60)

l1 = Label(f_top, width=7, height=4,
           bg='red', text="")
l2 = Label(f_top, width=7, height=4,
           bg='orange', text="")
l3 = Label(f_top, width=7, height=4,
           bg='yellow', text="")
l4 = Label(f_top, width=7, height=4,
           bg='green', text="")
l5 = Label(f_top, width=7, height=4,
           bg='blue', text="")

lbl.pack(side=TOP,pady=10)
f_top.pack()


l1.pack(side=LEFT,pady=30)
l2.pack(side=LEFT,pady=30)
l3.pack(side=LEFT,pady=30)
l4.pack(side=LEFT,pady=30)
l5.pack(side=LEFT,pady=30)

window.mainloop()