from tkinter import *   

with open("File.txt",'r') as f:
        text = f.read().splitlines()
def A():
    with open("File.txt",'a') as f:
        f.write(ent1.get() +'\n')
def B():
    with open("File.txt",'a') as f:
        f.write(ent2.get() +'\n')
def C():
    with open("File.txt",'a') as f:
        f.write(ent3.get() +'\n')
        
window = Tk()  
window.title("Анкета") 
window.geometry('500x300')
window.background='grey'
f_top = Frame(window)

lbl1=Label(window,text='Ваше имя:',font=('',30))
ent1 = Entry(window, width=20, background = 'white', foreground = 'black')
btn1=Button(window,text='<--',foreground='green',command=A).place(x=310,y=47)

lbl2=Label(window,text='Сколько вам?',font=('',30))
ent2 = Entry(window, width=20, background = 'white', foreground = 'black')
btn2=Button(window,text='<--',foreground='green',command=B).place(x=310,y=114)

lbl3=Label(window,text='Что вы любите?',font=('',30))
ent3 = Entry(window, width=20, background = 'white', foreground = 'black')
btn3=Button(window,text='<--',foreground='green',command=C).place(x=310,y=190)

lbl1.pack()
ent1.pack()
lbl2.pack()
ent2.pack()
lbl3.pack()
ent3.pack()
window.mainloop()
with open("File.txt",'r') as f:
        text = f.read().splitlines()
        print(text)