from tkinter import *  
from tkinter.ttk import Checkbutton  
from tkinter.ttk import Radiobutton
  
def a():
    lbl.configure(text=rad.get())

def b():
    lbl.configure(text=chk.get())
  
window = Tk()  
window.title("Добро пожаловать в приложение Python")  
window.geometry('400x250')  
chk = IntVar()  
chk.set(0) 
chk1 = Checkbutton(window, text='Выбрать',var=chk)  
chk1.grid(column=0, row=1)  
  
rad = IntVar()  
rad.set(0)
rad1 = Radiobutton(window, text='Первый', value=1,variable=rad)  
rad2 = Radiobutton(window, text='Второй', value=2,variable=rad)  
rad3 = Radiobutton(window, text='Третий', value=3,variable=rad)
btn=Button(window,text='click',command=a)
lbl=Label(window)
rad1.grid(column=0, row=0)  
rad2.grid(column=1, row=0)  
rad3.grid(column=2, row=0) 
btn.grid(column=0, row=2)
lbl.grid(column=1, row=2)






window.mainloop()