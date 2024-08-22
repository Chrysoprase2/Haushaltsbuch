from tkinter import Tk, ttk, StringVar, Entry, Scrollbar, Frame, Canvas
from Buchung import Buchung
from datetime import datetime, time

root = Tk()
scrollTracker = 0


def createUI(buchungen:list[Buchung]):
    root.title("Haushaltsbuch")

    root.minsize(100 ,50)
    root.configure(background="#ffcc00") 

    # main
    main_frame = Frame(root)
    main_frame.pack(fill="both", expand=1)

    # canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side="left", fill="both", expand=1)

    # scrollbar
    my_scrollbar = Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
    my_scrollbar.pack(side="right", fill="y")

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind(
        '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
    )

    second_frame = Frame(my_canvas, width = 100, height = 100)
    

    my_canvas.create_window((100, 50), window=second_frame, anchor="nw")

    #root.bind("<MouseWheel>", OnScroll)
    # frame=Frame(root)
    # canvas=Canvas(frame, scrollregion=(0,0,500,500))
    # vbar=Scrollbar(frame,orient="vertical")
    # vbar.pack(side="right",fill="y")
    # vbar.config(command=canvas.yview)
    # canvas.config(width=300,height=300)
    # canvas.config(yscrollcommand=vbar.set)
    # canvas.pack(side="left",expand=True,fill="both")

    #Programm beenden
    btnBeenden = ttk.Button(second_frame, text="Beenden", command=root.quit)
    btnBeenden.place(x=30, y=6)

    
    #Buchungen anzeigen, funktioniert nicht
    #btnBuchunganzeichnen = ttk.Button(root, text = "Buchung", command= lambda:buchungenAnzeigen(buchungen))
    #btnBuchunganzeichnen.grid(row=10, column=0)
    #buchungenAnzeigen(buchungen)
    #Kategorie hinzufügen, funktioniert nicht
    btnKategorieHinzufuegen = ttk.Button(second_frame, text = "Kategorie hinzufügen")
    btnKategorieHinzufuegen.place(x=20, y=6)

    i = 0
    offset = 30
    for buchung in buchungen:   
        textvarDatum = StringVar()
        datum = datetime.combine(buchung.datum, time())
        textvarDatum.set(datum.strftime("%d.%m.%Y"))
        entryDatum = Entry(second_frame, textvariable=textvarDatum, state="readonly")
        entryDatum.place(y=i*offset, x=0*offset)
        textvarInhaber = StringVar(second_frame)
        textvarInhaber.set(buchung.inhaber)
        entryInhaber = Entry(second_frame, textvariable =textvarInhaber, state="readonly")
        entryInhaber.place(y=i*offset, x=1*offset)
        textvarBetreff = StringVar(second_frame)
        textvarBetreff.set(buchung.betreff)
        entryBetreff = Entry(second_frame, textvariable=textvarBetreff,width=80, state="readonly")
        entryBetreff.place(y=i*offset, x=2*offset)
        textvarBetrag = StringVar(second_frame)
        textvarBetrag.set(f"{buchung.betrag.geldbetrag} {buchung.betrag.waehrung}")
        entryBetrag = Entry(second_frame, textvariable=textvarBetrag, state="readonly")
        entryBetrag.place(y=i*offset, x=3*offset)
        
        i+=1

        if i == 100:
            break



    root.mainloop()

# def OnScroll(event):
#     global scrollTracker
#     scrollTracker += event.delta
#     print (scrollTracker)
#     return


def buchungenAnzeigen(buchungen:list[Buchung]):
    buchung = buchungen[0]

    textvar = StringVar(root, buchung.inhaber)
    textvar.set(buchung.inhaber)
    entry = ttk.Entry(root, textvariable =textvar, state="readonly")
    entry.grid(row=0, column=0)


    return

