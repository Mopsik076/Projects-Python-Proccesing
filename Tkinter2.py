from tkinter import *   
  
window = Tk()  
window.title("Виджеты") 
window.geometry('500x500')
window.background='black'
f_top = Frame(window)

l1 = Label(f_top, width=7, height=4,
           bg='red', text="1")
l2 = Label(f_top, width=7, height=4,
           bg='orange', text="2")
l3 = Label(f_top, width=7, height=4,
           bg='yellow', text="3")
l4 = Label(f_top, width=7, height=4,
           bg='green', text="4")
l5 = Label(f_top, width=7, height=4,
           bg='blue', text='5')

f_top.pack()

l1.pack(side=LEFT, padx=5, pady=100)
l2.pack(side=LEFT, padx=5, pady=100)
l3.pack(side=LEFT, padx=5, pady=100)
l4.pack(side=LEFT, padx=5, pady=100)
l5.pack(side=LEFT, padx=5, pady=100)

btn = Button(bg='grey').place(relx=0.5, rely=0.5)

window.mainloop()