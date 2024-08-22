import matplotlib.pyplot as plt
from Buchungsmethoden import sortierenNachDatum , KontostandAnTag, filterNachDatum, filternNachKategorien
from datetime import datetime, time, timedelta
from jsonHelper import getListeKategorien
from calendar import monthrange


def anzeigenGraph(buchungen:list):
    x,y = returnAchsenListe (buchungen)
    plt.plot(x,y)
    plt.show()
    return


def returnAchsenListe(buchungen:list):
    x = list()
    y = list()
    sortierteBuchungen = sortierenNachDatum(buchungen)
    minDate = datetime.combine(sortierteBuchungen[0].datum, time())
    maxDate = datetime.combine(sortierteBuchungen[len(sortierteBuchungen)-1].datum, time())
    temp = minDate
    while temp <= maxDate:
        x.append (temp)
        temp += timedelta (days=1)

    for tag in x:
        yInput = KontostandAnTag (sortierteBuchungen, tag)
        y.append (yInput)
    return (x,y)


def kategorienGraphAnzeigen(buchungen:list, monat, jahr):
    fig, ax = plt.subplots()
    farben = ['black', 'red', 'yellow']
    
    monat = int(monat)
    jahr = int(jahr)
    x,y = returnAchsenKategorien(buchungen, monat, jahr)
    ax.bar(x,y, color = farben , label = x)
    ax.legend(title = 'Categorie')
    plt.show()
    return


def returnAchsenKategorien(buchungen:list, monat:int, jahr:int):
    y = list()
    x = list()
    vonDatum = datetime(jahr, monat, 1)
    bisDatum = datetime(jahr, monat, monthrange(jahr, monat)[1])
    gefilterteBuchungen = filterNachDatum(buchungen, vonDatum, bisDatum)
    kategorien = getListeKategorien()
    kategorien.remove("Gehalt")
    for kategorie in kategorien:
        gefilterteKategorie = filternNachKategorien(gefilterteBuchungen, kategorie)
        ausgaben = KontostandAnTag(gefilterteKategorie, bisDatum) * -1
        if ausgaben != 0:
            y.append(ausgaben) 
            x.append(kategorie)
    return (x,y)
     
    

