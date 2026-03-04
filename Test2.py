import tkinter
import math
from tkinter import ttk

def function():
    a = float(indput1.get())
    b = float(indput2.get())
    c = float(indput3.get())
    X1 = (-b + math.sqrt(b*b - 4*a*c)) / 2*a
    X2 = (-b - math.sqrt(b*b - 4*a*c)) / 2*a
    label6.config(text=X1)
    label7.config(text=X2)

vindue = tkinter.Tk()
vindue.geometry('500x500')
vindue.config(bg="pink")

#Oprettelse af frames
frame2 = tkinter.Frame(vindue, width=100, height=25, bd=3, relief="sunken")
frame2.place(x=330, y=100)

frame1 = tkinter.Frame(vindue, width=100, height=25, bd=3, relief="sunken")
frame1.place(x=330, y=150)

#Oprettelse af labels
label1 = tkinter.Label(vindue, text="A",bg="pink")
label1.place(x=50, y=100)

label2 = tkinter.Label(vindue, text="B",bg="pink")
label2.place(x=50, y=150)

label3 = tkinter.Label(vindue, text="C",bg="pink")
label3.place(x=50, y=200)

label4 = tkinter.Label(vindue, text="X1 =",bg="pink")
label4.place(x=300, y=100)

label5 = tkinter.Label(vindue, text="X2 =",bg="pink")
label5.place(x=300, y=150)

label6 = tkinter.Label(frame2, text = "")
label6.place(x=0, y=0)

label7 = tkinter.Label(frame1, text = "")
label7.place(x=0, y=0)

#Oprettelse af indput
indput1 = tkinter.Entry(vindue)
indput1.place(x=70, y=100)

indput2 = tkinter.Entry(vindue)
indput2.place(x=70, y=150)

indput3 = tkinter.Entry(vindue)
indput3.place(x=70, y=200)

#Oprettelse af knap
knap1 = tkinter.Button(vindue, text="Beregn", command=function)
knap1.place(x=100, y=230)

#Oprettelse af seperator
seperator = ttk.Separator(vindue, orient="vertical")
seperator.place(x=250, y=0, height=500)


vindue.mainloop()