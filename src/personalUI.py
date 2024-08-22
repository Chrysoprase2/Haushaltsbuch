from tkinter import Tk, StringVar, Entry, Scrollbar, Frame, Canvas, Radiobutton
from Buchung import Buchung
from datetime import datetime, time
from Buchungsmethoden import kategorienAusgabe, filternNachKategorien, JsonKategorieAuslesen
from tkinter import Tk, StringVar, Toplevel, Entry, Label, Button, OptionMenu, PhotoImage
from jsonHelper import inhaberZuJsonHinzufügen, getListeKategorien
from GraphUi import anzeigenGraph,kategorienGraphAnzeigen
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk


# json für die Kategorien - vorerst hardcoded
kategorieZuordnung = JsonKategorieAuslesen("test.json")
root = Tk()


def createUI(buchungen: list[Buchung]):
    root.title ("SAP Finanzen")
    root.minsize (1330, 1000) 
    icon = PhotoImage(file='saplogo.png')
    root.iconphoto (True, icon)
    backgroundImage = Image.open ('saplogo.png')
    backgroundImage = backgroundImage.resize((950, 600))
    backgroundPhotoImage = ImageTk.PhotoImage (backgroundImage)
    backgroundLabel = Label (root, image=backgroundPhotoImage)
    backgroundLabel.pack(side='left')
    createButtons(buchungen)
    root.mainloop()


def createButtons(buchungen: list[Buchung]):
    # main
    mainFrame = Frame (root)
    mainFrame.pack (fill = "both", expand = 1)

    # searchbar + searchbutton
    searchVar = StringVar()
    searchEntry = Entry (root, textvariable=searchVar, width=28)
    searchEntry.place (x=1100, y=50)
    searchbtn = Button (root, text="Suchen", bg="#00b9f2", command=lambda: searchBuchungen (root, buchungen, searchVar.get()), font=("Arial", 10))
    searchbtn.place (x=1100, y=80)

    #Kategorie hinzufügen
    btnKategorieHinzufuegen = Button(root, text = "Kategorie hinzufügen", bg="#00b9f2", command=lambda:kategorieHinzufuegen(), font=("Arial", 10))
    btnKategorieHinzufuegen.place(x=1100, y=150)

    # graph anzeigen
    anzeigebtn = Button (root, text="Graph anzeigen", bg="#00b9f2", command= lambda:anzeigenGraph(buchungen), font=("Arial", 10))
    anzeigebtn.place (x=1100, y=200)

    # Ausgaben nach Kategorie
    anzeigebtn = Button (root, text="Ausgaben nach Kategorie", bg="#00b9f2", command= lambda:ausgabenNachKategorie(mainFrame, buchungen), font=("Arial", 10))
    anzeigebtn.place (x=1100, y=250)

    # Buchungen anzeigen lassen
    btnBuchungenAnzeigen = Button(root, text="Buchungen anzeigen", bg="#00b9f2", command=lambda:buchungenAnzeigen(root, buchungen), font=("Arial", 10))
    btnBuchungenAnzeigen.place(x=1100, y=300)

    # Ausgaben gefiltert anzeigen
    filterbtn = Button (root, text="Ausgaben filtern", bg="#00b9f2", command= lambda:kategorienFilterAusgabe(root, buchungen, ausgewählteKategorie.get()), font=("Arial", 10))
    filterbtn.place (x=1100, y=350)

    # filterbuttons
    startY = 400
    ausgewählteKategorie = StringVar()
    ausgewählteKategorie.set ("Dies ist ein leerer String")
    kategorienListe = kategorienAusgabe (buchungen)
    for kategorie in kategorienListe:
        neuerButton = Radiobutton (root, text=kategorie, variable=ausgewählteKategorie,value=kategorie, font=("Arial", 10))
        neuerButton.place (x=1100, y=startY)
        startY +=30

    # Programm beenden
    btnBeenden = Button(root, text="Beenden",bg="red", command=root.quit, height=2, width=10, font=("Arial", 10))
    btnBeenden.place(x=1200, y=780)


def kategorieHinzufuegen():

    top = Toplevel(root)
    top.title ("Kategorie hinzufügen")
    top.minsize (400, 300)

    # unterfenster fürs layout
    rahmen = Frame (master=top)
    labelAnweisung = Label (rahmen, text="Tragen Sie einen Inhaber einer bestehenden Kategorie hinzu:")
    labelAnweisung.pack (pady=10)
    rahmen1 = Frame (master=rahmen)
    rahmen2 = Frame (master=rahmen)
    rahmen1.pack (pady=10)
    rahmen2.pack(pady=10)
    rahmen.pack (pady=10, expand=True)

    # Elemente für Abfrage
    labelInhaber = Label(rahmen1, text= "Inhaber: ")
    labelInhaber.pack(side="left",pady=10)
    entryInhaber = Entry(rahmen1)
    entryInhaber.pack(side="left", pady=10)

    kategorien = getListeKategorien()
    ausgewählteKategorie = StringVar()
    ausgewählteKategorie.set(kategorien[0])
    labelKategorie = Label(rahmen2, text= "Kategorie: ")
    labelKategorie.pack(side="left", pady=10)
    kategorienDrop = OptionMenu(rahmen2, ausgewählteKategorie, *kategorien)
    kategorienDrop.config (bg="#00b9f2")
    kategorienDrop.pack(side="left", pady=10)
    hinzufuegenbtn = Button(top, text="Hinzufügen", bg="#00b9f2",  command= lambda: inhaberZuJsonHinzufügen(entryInhaber.get(), ausgewählteKategorie.get()))
    hinzufuegenbtn.pack(pady=10)


def ausgabenNachKategorie(mainFrame:Frame, buchungen:list[Buchung]):

    # öffnet neues Fenster für die Abfrage
    top = Toplevel(root)
    top.title ("Ausgaben nach Kategorie")

    cal = Calendar (top, selectmode= "day", year=2019)
    cal.pack (pady = 10)

    anzeigenbtn = Button(top, text="Anzeigen", bg="#00b9f2", command= lambda: 
                             kategorienGraphAnzeigen(buchungen, cal.get_date().split('/')[0], 
                            "20"+cal.get_date().split('/')[2]))
    anzeigenbtn.pack(pady=10)


def buchungenAnzeigen(mainFrame:Frame, buchungen:list[Buchung]):

    # leert das Fenster
    clearFrame(mainFrame)

    # canvas
    myCanvas = Canvas (mainFrame)
    myCanvas.pack (side = "left", fill = "both", expand = 1)

    # scrollbar
    my_scrollbar = Scrollbar(mainFrame, orient="vertical", command=myCanvas.yview)
    my_scrollbar.pack(side="right", fill="y")

    #configure canvas
    myCanvas.configure (yscrollcommand=my_scrollbar.set)
    myCanvas.bind ('<Configure>', lambda e: myCanvas.configure (scrollregion=myCanvas.bbox ("all")))

    # second frame / inneres Fenster, das gescrollt wird. muss min. so groß wie das Primärfenster sein, um zu scrollen
    secondFrame = Frame(myCanvas, width = 1200, height = 1000)
    
    # secondFrame an canvas binden
    myCanvas.create_window((0, 0), window=secondFrame, anchor="nw")

    # scrollevent an canvas binden / nicht an secondFrame binden!
    myCanvas.bind_all("<MouseWheel>", lambda event: scrollEvent(event, myCanvas))

    #counter und Variablen für Platzierung auf Y- und X-Achse
    i = 0
    frameHeight = 1000  #Counter für die Anpassung des secondFrame (Fenster, in dem gescrollt werden soll)
    offset = 20
    offsetX = 60

    # Title labels
    textvarDatumTitel = StringVar(secondFrame)
    textvarDatumTitel.set("Datum")
    entryDatumTitel = Entry(secondFrame, textvariable=textvarDatumTitel, width = 30, state="readonly", font=("Arial", 10, "bold"))
    entryDatumTitel.place(y=10, x= 0*offsetX)

    textvarInhaberTitel = StringVar(secondFrame)
    textvarInhaberTitel.set("Inhaber")
    entryInhaberTitel = Entry(secondFrame, textvariable=textvarInhaberTitel, width = 100, state="readonly", font=("Arial", 10, "bold"))
    entryInhaberTitel.place(y=10, x=3*offsetX)

    textvarBetreffTitel = StringVar(secondFrame)
    textvarBetreffTitel.set("Betreff")
    entryBetreffTitel = Entry(secondFrame, textvariable=textvarBetreffTitel, width = 70, state="readonly", font=("Arial", 10, "bold"))
    entryBetreffTitel.place(y=10, x=50+8*offsetX)

    textvarBetragTitel = StringVar(secondFrame)
    textvarBetragTitel.set("Betrag")
    entryBetragTitel = Entry(secondFrame, textvariable=textvarBetragTitel, width = 12, state="readonly", font=("Arial", 10, "bold"))
    entryBetragTitel.place(y=10, x=100+14*offsetX)


    for buchung in buchungen: 
        # Eintrag für jedes Buchungselement vornehmen
        textvarDatum = StringVar()
        datum = datetime.combine(buchung.datum, time())
        textvarDatum.set(datum.strftime("%d.%m.%Y"))
        entryDatum = Entry(secondFrame, textvariable=textvarDatum, width = 30, state="readonly")
        entryDatum.place(y=30+i*offset, x= 0*offsetX)

        textvarInhaber = StringVar(secondFrame)
        textvarInhaber.set(buchung.inhaber)
        entryInhaber = Entry(secondFrame, textvariable =textvarInhaber, width = 100, state="readonly")
        entryInhaber.place(y=30+i*offset, x= 3*offsetX)

        textvarBetreff = StringVar(secondFrame)
        textvarBetreff.set(buchung.betreff)
        entryBetreff = Entry(secondFrame, textvariable=textvarBetreff,width=70, state="readonly")
        entryBetreff.place(y=30+i*offset, x= 50+8*offsetX)

        textvarBetrag = StringVar(secondFrame)
        textvarBetrag.set(f"{buchung.betrag.geldbetrag} {buchung.betrag.waehrung}")
        entryBetrag = Entry(secondFrame, textvariable=textvarBetrag, width = 12, state="readonly")
        entryBetrag.place(y=30+i*offset, x=100+14*offsetX)

        # Frame anpassen: i mit jeder Iteration erhöhen
        frameHeight+= 17
        i+=1

        # limit auf 300 Einträge wegen Performance - bei Bedarf anpassen
        if i == 200:
            break

    secondFrame.configure (height=frameHeight)
    createButtons(buchungen)

# filternNachKategorien gibt dict aus (kategorie, list(Buchungen)), um an Kategorieoptionen zu kommen
# Kategorie filtern nach eingegebener Kategorie im Radiobutton, dann buchungenAnzeigen() anwenden
# angezeigte Kategorien sind aus dem dict geholt -> keine unbekannten Kategorien möglich
def kategorienFilterAusgabe(mainFrame: Frame, buchungen: list[Buchung], kategorie:str):
    verarbeitungsListe = filternNachKategorien(buchungen ,kategorie , kategorieZuordnung)
    buchungenAnzeigen (mainFrame, verarbeitungsListe)
    createButtons(buchungen)


def searchBuchungen(mainFrame: Frame, buchungen: list[Buchung], searchTerm: str):

    referenceList = list[Buchung]()
    for buchung in buchungen:
        referenceList.append (buchung)

    resultList = []
        
    for buchung in referenceList: 
        if searchTerm.lower() in buchung.inhaber.lower():
            resultList.append (buchung)
        if searchTerm.lower() in buchung.betreff.lower():
            resultList.append (buchung)
        if searchTerm.lower() in buchung.datum.strftime("%d.%m.%Y"):
            resultList.append (buchung)
    

    buchungenAnzeigen(mainFrame, resultList)
    createButtons(buchungen)


def scrollEvent (event, canvas:Canvas):
    canvas.yview_scroll (-1*int((event.delta/120)), "units")


def clearFrame(mainFrame:Frame):
    for widget in mainFrame.winfo_children():
        widget.destroy()

