from tkinter import *  
from tkinter.ttk import Checkbutton  
from tkinter.ttk import Radiobutton

window = Tk()  
window.title("Вопросы для 'Умных'")  
window.geometry('800x300')

def A():
    check1 = rad.get()
    check2 = radd.get()
    check3 = raddd.get()
    check4 = radddd.get()
    
    if check1 != 12:
        lbl1.configure(text='Не правильно')
    if check2 !=21:
        lbl2.configure(text='Не правильно')
    if check3 !=33:
        lbl3.configure(text='Не правильно')
    if check4 !=44:
        lbl4.configure(text='Не правильно')

lbl=Label(window,text='1+1=?')
lbl2=Label(window,text='Яблоко + яблоко=?')
lbl3=Label(window,text='У тебя 2 апельсина, а у твоего друга 1 апельсин, сколько всего у вас яблок?')
lbl4=Label(window,text='Кто умнее')

rad = IntVar()
rad.set(0)
radd = IntVar()
radd.set(0)
raddd = IntVar()
raddd.set(0)
radddd = IntVar()
radddd.set(0)

lbl1=Label(window,text='1+1=?')

rad11=Radiobutton(window,text='11',value=11,var=rad)
rad12=Radiobutton(window,text='2',value=12,var=rad)
rad13=Radiobutton(window,text='много',value=13,var=rad)
rad14=Radiobutton(window,text='пропустить',value=14,var=rad)

lbl2=Label(window,text='Яблоко + яблоко=?')

rad21=Radiobutton(window,text='2 яблока',value=21,var=radd)
rad22=Radiobutton(window,text='ананас',value=22,var=radd)
rad23=Radiobutton(window,text='я всё схамячил',value=23,var=radd)
rad24=Radiobutton(window,text='не знаю',value=24,var=radd)

lbl3=Label(window,text='У тебя 2 апельсина, а у твоего друга 1 апельсин, сколько у вас яблок?')

rad31=Radiobutton(window,text='2 апельсина',value=31,var=raddd)
rad32=Radiobutton(window,text='3 яблока',value=32,var=raddd)
rad33=Radiobutton(window,text='у нас нет яблок',value=33,var=raddd)
rad34=Radiobutton(window,text='у меня нет друзей',value=34,var=raddd)

lbl4=Label(window,text='Кто умнее?')

rad41=Radiobutton(window,text='компьютер',value=41,var=radddd)
rad42=Radiobutton(window,text='собака',value=42,var=radddd)
rad43=Radiobutton(window,text='Все тупые',value=43,var=radddd)
rad44=Radiobutton(window,text='человек',value=44,var=radddd)

btn=Button(window,text='Закончить',command=A)

rad11.grid(column=1,row=1)
rad12.grid(column=2,row=1)
rad13.grid(column=3,row=1)
rad14.grid(column=4,row=1)
rad21.grid(column=1,row=3)
rad22.grid(column=2,row=3)
rad23.grid(column=3,row=3)
rad24.grid(column=4,row=3)
rad31.grid(column=1,row=5)
rad32.grid(column=2,row=5)
rad33.grid(column=3,row=5)
rad34.grid(column=4,row=5)
rad41.grid(column=1,row=7)
rad42.grid(column=2,row=7)
rad43.grid(column=3,row=7)
rad44.grid(column=4,row=7)
lbl1.grid(column=3,row=0)
lbl2.grid(column=3,row=2)
lbl3.grid(column=3,row=4)
lbl4.grid(column=3,row=6)
btn.grid(column=3,row=9)

























window.mainloop()