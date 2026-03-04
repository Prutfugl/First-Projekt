import solid2
import tkinter
from tkinter import ttk

Vindue = tkinter.Tk()
Vindue.geometry('500x500')



#Funktion til at lave vinglas -----------------
def LavVinGlas():
    VinHojde = float(EnVinHojde.get())
    VinHul = float(EnVinHul.get())
    VinBund = float(EnVinBund.get())
    VinNavn = EnVinNavn.get()

    minModel1 = solid2.sphere(20)

    minModel2 = solid2.cube([40,50,100], center=True)
    minModel2 = solid2.translate([0,0,VinHul])(minModel2)

    minModel3 = solid2.sphere(19)

    minModel = minModel1 - minModel2- minModel3
    minModel = solid2.translate([0,0,20])(minModel)

    minModel4 = solid2.cylinder(h=VinHojde, r=5,center=True)
    minModel4 = solid2.translate([0,0,-8])(minModel4)

    minModel5 = solid2.cylinder(h=5,r1=VinBund,r2=5)
    minModel5 = solid2.translate([0,0,-20])(minModel5)

    Text = solid2.text(text=VinNavn, size=5)
    Text = solid2.translate([-8,-3,-20])(Text)
    Text = solid2.mirror([0,1,0])(Text)
    #Text = solid2.linear_extrude(height=5)(Text)

    finalModel = minModel + minModel4 + minModel5 - Text

    if(VinHojde >= 20 or VinHojde <= 5):
        FejlBesked.config(text="Fejl, højde skal være mellem 5 og 20",fg="red")
    elif(VinHul >= 19 or VinHul <= 5):
        FejlBesked.config(text="Fejl, hul skal være mellem 5 og 19",fg="red")
    elif(VinBund >= 20 or VinBund <= 5):
        FejlBesked.config(text="Fejl, bund skal være mellem 5 og 20",fg="red")
    else:
        solid2.scad_render_to_file(finalModel, 'C:/Users/luso/Downloads/VinGlas.scad')
        FejlBesked.config(text="Vinglas lavet, tjek din download mappe",fg="green")
    


#oprettelse af labels ----------------
LabelVinHøjde = tkinter.Label(Vindue, text="Højde på vinglasset")
LabelVinHøjde.place(x=50, y=25)

LabelVinHul = tkinter.Label(Vindue, text="Dybden på kublen")
LabelVinHul.place(x=50, y=100)

LabelVinBund = tkinter.Label(Vindue, text="Størelsen på bunden")
LabelVinBund.place(x=50, y=175)

LabelVinNavn = tkinter.Label(Vindue, text="Indgraver dit navn i koppen")
LabelVinNavn.place(x=300, y=25)

FejlBesked = tkinter.Label(Vindue, text= " ")
FejlBesked.place(x=50, y=350)

#oprettelse af induts ----------------
EnVinHojde = tkinter.Entry(Vindue)
EnVinHojde.place(x=50, y=50)

EnVinHul = tkinter.Entry(Vindue)
EnVinHul.place(x=50, y=125)

EnVinBund = tkinter.Entry(Vindue)
EnVinBund.place(x=50, y=200)

EnVinNavn = tkinter.Entry(Vindue)
EnVinNavn.place(x=300, y=50)


#oprettelse af knap ----------------
KnapLav = tkinter.Button(Vindue, text="Lav vinglas", command=LavVinGlas)
KnapLav.place(x=50, y=275)

ttk.Separator(Vindue, orient="horizontal").place(x=0, y=250, relwidt=50)




Vindue.mainloop()