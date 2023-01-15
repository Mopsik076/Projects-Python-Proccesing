from tkinter import *
from tkinter.ttk import Checkbutton  
from tkinter.ttk import Radiobutton

window = Tk()  
window.title("")  
window.geometry('300x300')

c= Canvas (width=800, height=300, bg='skyblue')
c.focus_set()
c.pack()

sun = c.create_oval(250,50,310,-10, fill='yellow')
grass = c.create_rectangle(0,250,300,300,  fill='green')
cube = c.create_rectangle(40,260,260,70, fill='tan1')
roof = c.create_polygon(35,70,265,70,150,10, fill='red')





class move:
    oval = c.create_oval(200,270,100,170,fill='white',outline='black', width='2')
    oval = c.create_oval(190,200,110,120,fill='white',outline='black', width='2')
    oval = c.create_oval(180,140,120,80,fill='white',outline='black', width='2')

    oval = c.create_oval(140,110,130,100,fill='black',outline='black', width='2')
    oval = c.create_oval(170,110,160,100,fill='black',outline='black', width='2')

    oval = c.create_line(110,160,80,80, width='4', fill='tan4')
    oval = c.create_line(190,160,220,80, width='4', fill='tan4')

line = c.create_line(20,260,20,100, width='4', fill='grey40')
cube = c.create_rectangle(10,100,30,20, fill='grey40', outline='grey20')

oval2 = c.create_oval(12,30,28,45,fill='red',outline='black', width='2')
oval2 = c.create_oval(12,50,28,65,fill='yellow',outline='black', width='2')
oval2 = c.create_oval(12,70,28,85,fill='green',outline='black', width='2')

c.bind('<Right>', lambda event: c.move(move,15,0))
c.bind('<Left>', lambda event: c.move(move,-15,0))




c.update()
window.mainloop()