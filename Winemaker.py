import solid2
import tkinter

Vindue = tkinter.Tk()
Vindue.geometry('500x500')

#oprettelse af labels ----------------
LabelVinHøjde = tkinter.Label(Vindue, text="Højde på vinglasset")
LabelVinHøjde.place(x=50, y=25)

LabelVinHul = tkinter.Label(Vindue, text="Dybden på kublen")
LabelVinHul.place(x=50, y=75)

LabelVinBund = tkinter.Label(Vindue, text="Størelsen på bunden")
LabelVinBund.place(x=50, y=125)


#oprettelse af induts ----------------
VinHøjde = tkinter.Entry(Vindue)
VinHøjde.place(x=50, y=50)

VinHul = tkinter.Entry(Vindue)
VinHul.place(x=50, y=100)

VinBund = tkinter.Entry(Vindue)
VinBund.place(x=50, y=150)





Vindue.mainloop()