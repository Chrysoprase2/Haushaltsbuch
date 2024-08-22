from datetime import datetime, time
from Buchung import Buchung
from jsonHelper import JsonKategorieAuslesen

#ordnet einer Kategorie die Inhaber (in einer Liste) zu
def KategorieZuBuchungen(buchungen:list[Buchung]):
    kategorieZuBuchungen = dict()
    for buchung in buchungen:
        kategorieUndBetreff = buchung.betreff.split("=-")
        kategorie = kategorieUndBetreff[0].removeprefix("-=")
        if kategorie not in kategorieZuBuchungen.keys():
            kategorieZuBuchungen[kategorie] = list()

        if buchung.inhaber not in kategorieZuBuchungen[kategorie]:
                kategorieZuBuchungen[kategorie].append(buchung.inhaber)
    
    return kategorieZuBuchungen


#aufsteigend
def sortierenNachDatum(buchungen:list[Buchung]):
    bubbled = True
    while bubbled:
        bubbled = False
        for i in range(len(buchungen)-1):
            if buchungen[i].datum > buchungen[i+1].datum:
                bubbled = True
                buchung = buchungen[i]
                buchungen[i] = buchungen[i+1]
                buchungen[i+1] = buchung

    return buchungen


#absteigend
def sortierenNachBetrag(buchungen:list[Buchung]):
    bubbled = True
    while bubbled:
        bubbled = False
        for i in range(len(buchungen)-1):
            if buchungen[i].betrag.geldbetrag < buchungen[i+1].betrag.geldbetrag:
                bubbled = True
                buchung = buchungen[i]
                buchungen[i] = buchungen[i+1]
                buchungen[i+1] = buchung

    return buchungen


def filterNachDatum(buchungen:list[Buchung], vonDatum:datetime, bisDatum:datetime):
    gefilterteBuchungen = list()
    for i in range(len(buchungen)-1):
        if buchungen[i].datum >= vonDatum.date() and buchungen[i].datum <= bisDatum.date():
            gefilterteBuchungen.append(buchungen[i])

    return gefilterteBuchungen


def filternNachKategorien(buchungen:list[Buchung], kategorie : str , kategorieZuordnung : dict = JsonKategorieAuslesen()):
    gefilterteBuchungenZuKategorien = list()
    for buchung in buchungen : 
        if kategorie in kategorieZuordnung.keys():
            if buchung.inhaber in kategorieZuordnung[kategorie]: 
                gefilterteBuchungenZuKategorien.append(buchung)
    return gefilterteBuchungenZuKategorien


def kategorienAusgabe (buchungen:list[Buchung]):
    kategorienDict = JsonKategorieAuslesen()
    kategorienListe = list(kategorienDict.keys())
    sortierteKategorien = sorted (kategorienListe)
    return sortierteKategorien


def KontostandAnTag(buchungen:list[Buchung], datum:datetime):
    if len(buchungen) < 1:
        return 0.0
    sortiererteBuchungen = sortierenNachDatum(buchungen)
    gefilterteBuchungen = filterNachDatum(sortiererteBuchungen, datetime.combine(sortiererteBuchungen[0].datum, time()), datum)
    kontostand = 0.0
    for buchung in gefilterteBuchungen:
        kontostand += buchung.betrag.geldbetrag
    return kontostand