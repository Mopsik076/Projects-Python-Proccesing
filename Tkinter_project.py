from tkinter import *
from tkinter.ttk import Checkbutton  
from tkinter.ttk import Radiobutton

window = Tk()  
window.title("")  
window.geometry('800x300')

c= Canvas (width=800, height=300, bg='white')
c.focus_set()
c.pack()

oval = c.create_oval(50,50,100,100,fill='black')

c.bind('<Up>', lambda event: c.move(oval,0,-15))
c.bind('<Right>', lambda event: c.move(oval,15,0))
c.bind('<Down>', lambda event: c.move(oval,0,15))
c.bind('<Left>', lambda event: c.move(oval,-15,0))




































c.update()
window.mainloop()