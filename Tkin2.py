from tkinter import *  
from tkinter.ttk import Checkbutton  
from tkinter.ttk import Radiobutton


window = Tk()  
window.title("Лицензия соглашения")  
window.geometry('400x100')

def dalee():
    choice = rad.get()
    if choice == 1:
        lbl.configure(text='Вы приняли соглошение')
    
    elif choice == 2:
        lbl.configure(text='Вы не приняли соглошение')
    
    else:
        lbl.configure(text='Примите соглошение')

lbl=Label(window,text='|Пользовательское соглашение|')
btn=Button(window,text='Далее',command=dalee)
rad=IntVar()
rad.set(0)
rad1=Radiobutton(window,text='Принимаю',value= 1 ,var=rad)
rad2=Radiobutton(window,text='Не принимаю',value= 2 ,var=rad)
rad1.grid(column=1,row=1)
rad2.grid(column=2,row=1)
btn.grid(column=3,row=1)
lbl.grid(column=2,row=0)

window.mainloop()