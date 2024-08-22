
from tkinter import ttk,Tk, StringVar, Toplevel, Entry, Label, Button, OptionMenu, PhotoImage
from jsonHelper import inhaberZuJsonHinzufügen, getListeKategorien
import matplotlib.pyplot as plt
from GraphUi import anzeigenGraph,kategorienGraphAnzeigen
from tkcalendar import Calendar
from datetime import datetime

alleBuchungen = None
root = Tk()
root.configure(background="white")
buchungsRoot = None

def createUI(buchungen):
    global alleBuchungen
    alleBuchungen = buchungen
    root.title("SAP Finanzen")
    icon = PhotoImage(file='saplogo.png')
    root.iconphoto (True, icon)
    root.minsize(width=50,height=100)
    quitbtn = Button(root, text="Beenden", command=root.destroy , bg="#00b9f2", fg="#00ff00", font=("Arial", 1, "bold"))
    quitbtn.grid(pady=15,padx=root.winfo_screenmmwidth()/4)
    showbuchungen = Button(root, text="Buchungen", command=ShowBuchungen , bg="#00b9f2")
    showbuchungen.grid(pady=15,padx=root.winfo_screenmmwidth()/4)
    kategorieHinzufuegenbtn = Button(root, text = "Kategorie Hinzufügen",command=kategorieHinzufuegen, bg='#00b9f2')
    kategorieHinzufuegenbtn.grid(pady=15 , padx=root.winfo_screenmmwidth()/4)
    graphbtn = Button (root, text="Grafikanzeige des Konstostandes", command=graphAnzeigen, bg="#00b9f2")
    graphbtn.grid (pady=15 , padx=root.winfo_screenmmwidth()/4)

    root.mainloop()
    return

def ShowBuchungen():
    global buchungsRoot
    buchungsRoot = OpenNewWindow("Buchungen","970x800")
    UpdateBuchungenUI()
    return

def kategorieHinzufuegen():
    kategoriewindow = OpenNewWindow("Kategorie Hinzufügen")
    entryInhaber = Entry(kategoriewindow)
    entryInhaber.grid(row=1 , column= 2)
    labelInhaber = Label( kategoriewindow, text= "Inhaber")
    kategorien = getListeKategorien()
    ausgewählteKategorie = StringVar()
    ausgewählteKategorie.set(kategorien[0])
    kategorienDrop = OptionMenu(kategoriewindow, ausgewählteKategorie, *kategorien)
    kategorienDrop.grid(row=2, column=2)
    #entryKategorie = Entry(kategoriewindow) 
    #entryKategorie.grid(row=2 , column= 2)
    labelKategorie = Label( kategoriewindow, text= "Kategorie")
    labelInhaber.grid(row=1, column=1)
    labelKategorie.grid(row=2, column=1)
    hinzufuegenbtn = ttk.Button(kategoriewindow, text="Hinzufügen", command= lambda: inhaberZuJsonHinzufügen(entryInhaber.get(), ausgewählteKategorie.get()), padding=20)
    hinzufuegenbtn.grid(row=3, column=3)

def graphAnzeigen():
    graphWindow = OpenNewWindow ()
    anzeigebtn = Button (graphWindow, text = " Wirklich anzeigen?",command= lambda:anzeigenGraph(alleBuchungen), bg='#00b9f2')
    anzeigebtn.grid (row=3, column=1)


def OpenNewWindow(title="New Window", geometry="200x200", WinRoot = root) -> Toplevel:
    """
    function: Erstellt ein neues UI Fenster und gibt die Referenz zur Instanz zurück
    returns: Instance of Toplevel Object
    """
    newWindow = Toplevel(WinRoot)
    newWindow.title(title)
    newWindow.geometry(geometry)
    newWindow.bind("<KeyRelease>", OnKeyRelease)
    newWindow.minsize(width=970,height=80)
    newWindow.update()
    return newWindow

def UpdateBuchungenUI():
    global alleBuchungen
    ausgabenProkategoriebtn = Button(buchungsRoot, text="Ausgaben pro Kategorien", command=ausgabenProKategorie)
    ausgabenProkategoriebtn.grid(row=1, column=1)
    for i in range(2, 102):
        if(scrolltracker + i > len(alleBuchungen)):
            break
        textvar = StringVar()
        textvar.set(alleBuchungen[scrolltracker+i].inhaber)
        entry = Entry(buchungsRoot, width=15, fg='blue', font=('Arial', 12, 'bold'), textvariable=textvar, state='readonly')
        entry.grid(row=i,column=4)
        textvar = StringVar()
        textvar.set(alleBuchungen[scrolltracker+i].betreff)
        entry = Entry(buchungsRoot, width=15, fg='blue', font=('Arial', 12, 'bold'), textvariable=textvar, state='readonly')
        entry.grid(row=i,column=2)
        textvar = StringVar()
        textvar.set(f"{alleBuchungen[scrolltracker + i].betrag.geldbetrag} {alleBuchungen[scrolltracker + i].betrag.waehrung}")
        entry = Entry(buchungsRoot, width=15, fg='blue', font=('Arial', 12, 'bold'), textvariable=textvar, state='readonly')
        entry.grid(row= i, column= 3)
        textvar = StringVar()
        textvar.set(alleBuchungen[scrolltracker + i].datum)
        entry = Entry(buchungsRoot, width=15, fg='blue', font=('Arial', 12, 'bold'), textvariable=textvar, state='readonly')
        entry.grid(row= i , column= 1)

    
    #entry = Entry(buchungsRoot, width=15, fg='blue', font=('Arial', 12, 'bold'), textvariable=textvar, state='readonly')
    #entry.grid(row=0,column=0)
    return

scrolltracker = 0
def OnKeyRelease(event):
    global scrolltracker
    if(event.keysym == "Up"):
        scrolltracker += 100
        ClearBuchungsUI()
        UpdateBuchungenUI()
    if event.keysym == "Down":
        if scrolltracker >= 10:
            scrolltracker -= 100
            ClearBuchungsUI()
            UpdateBuchungenUI()
    
    return

def ClearBuchungsUI():
    for widget in buchungsRoot.winfo_children():
        widget.destroy()
    return

def ausgabenProKategorie():
    ausgabenProKategoriewindow = OpenNewWindow("Ausgaben pro Kategorie")
    # entryMonat = Entry(ausgabenProKategoriewindow)
    # entryMonat.grid(row=1 , column= 2)
    # labelMonat = Label(ausgabenProKategoriewindow, text= "Monat")
    # labelMonat.grid(row=1, column=1)
    # entryJahr = Entry(ausgabenProKategoriewindow)
    # entryJahr.grid(row=2 , column= 2)
    # labelJahr = Label(ausgabenProKategoriewindow, text= "Jahr")
    # labelJahr.grid(row=2, column=1)
    cal = Calendar (ausgabenProKategoriewindow, selectmode= 'day', year=2019)
    cal.grid (row=4, column=4)


    anzeigenbtn = ttk.Button(ausgabenProKategoriewindow, text="Anzeigen", command= lambda: 
                             kategorienGraphAnzeigen(alleBuchungen, cal.get_date().split('/')[0], 
                                                     "20"+cal.get_date().split('/')[2]), padding=20)
    anzeigenbtn.grid(row=3, column=3)
    return 