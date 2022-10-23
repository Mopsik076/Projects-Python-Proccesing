from tkinter import *   

a='red'

def A():
    lbl.configure(text= a, foreground = a)
  
window = Tk()  
window.title("Заданиe1") 
window.geometry('500x500')
window.background='black'
f_top = Frame(window)

lbl = Label(window, text='?', font = ('!', 30))
lbl.pack()
btn=Button(window, text='',bg='red',font=(30), command=A)
btn.pack()

window.mainloop()