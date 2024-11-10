from tkinter import *
calcul = Tk()
calcul.title('simple calculatrice')
f = Entry(calcul,width=35,borderwidth=5)
f.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def add(num):
    tiping = f.get()
    f.delete(0, END)
    f.insert(0 ,str(tiping)+str(num))

def clear():
    f.delete(0,END)

def addition():
    anum=f.get()
    global p_num
    p_num= int(anum)
    global algo
    algo = 'Addition'
    f.delete(0,END)

def Multipl():
    anum=f.get()
    global p_num
    p_num= int(anum)
    global algo
    algo = 'Multiplication'
    f.delete(0,END)

def Divis():
    anum=f.get()
    global p_num
    p_num= int(anum)
    global algo
    algo = 'Division'
    f.delete(0,END)

def Subst():
    anum=f.get()
    global p_num
    p_num= int(anum)
    global algo
    algo = 'Substraction'
    f.delete(0,END)


def egal():
    if algo=='Addition':
        snum= f.get()
        f.delete(0,END)
        f.insert(0,p_num + int(snum))

    if algo=='Substraction':
        snum= f.get()
        f.delete(0,END)
        f.insert(0,p_num - int(snum))

    if algo=='Multiplication':
        snum= f.get()
        f.delete(0,END)
        f.insert(0,p_num * int(snum))

    if algo=='Division':
        snum= f.get()
        f.delete(0,END)
        f.insert(0,p_num / int(snum))
    


button_1= Button(calcul,text='1',padx=40,pady=20,command=lambda:add(1),bg='purple',fg='white')
button_2= Button(calcul,text='2',padx=40,pady=20,command=lambda:add(2),bg='purple',fg='white')
button_3= Button(calcul,text='3',padx=40,pady=20,command=lambda:add(3),bg='purple',fg='white')
button_4= Button(calcul,text='4',padx=40,pady=20,command=lambda:add(4),bg='purple',fg='white')
button_5= Button(calcul,text='5',padx=40,pady=20,command=lambda:add(5),bg='purple',fg='white')
button_6= Button(calcul,text='6',padx=40,pady=20,command=lambda:add(6),bg='purple',fg='white')
button_7= Button(calcul,text='7',padx=40,pady=20,command=lambda:add(7),bg='purple',fg='white')
button_8= Button(calcul,text='8',padx=40,pady=20,command=lambda:add(8),bg='purple',fg='white')
button_9= Button(calcul,text='9',padx=40,pady=20,command=lambda:add(9),bg='purple',fg='white')
button_0= Button(calcul,text='0',padx=40,pady=20,command=lambda:add(0),bg='purple',fg='white')
button_addition= Button(calcul,text='+',padx=39,pady=20,command=addition,bg='aqua',fg='black')
button_egale= Button(calcul,text='=',padx=88,pady=20,command=egal,bg='#0D98BA',fg='white')
butoton_C= Button(calcul,text='C',padx=88,pady=20,command=clear,bg='#0D98BA',fg='white')
button_Multiplication= Button(calcul,text='*',padx=40,pady=20,command=Multipl,bg='aqua',fg='black')
button_division= Button(calcul,text='/',padx=42,pady=20,command=Divis,bg='aqua',fg='black')
button_soustraction= Button(calcul,text='-',padx=42,pady=20,command=Subst,bg='aqua',fg='black')


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1) 
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_addition.grid(row=5,column=0)
button_egale.grid(row=5,column=1,columnspan=2)
butoton_C.grid(row=4,column=1,columnspan=2)

button_soustraction.grid(row=6,column=0)
button_division.grid(row=6,column=1)
button_Multiplication.grid(row=6,column=2)



calcul.mainloop()