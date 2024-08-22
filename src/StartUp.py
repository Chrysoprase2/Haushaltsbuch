from datetime import datetime, time
from Buchung import Buchung
from Betrag import Betrag
from Node import Node
from personalUI import createUI
#from UI import createUI

"""
Dieses Programm gibt Buchungen aus, die es aus einer CSV-Datei einließt. 
Über eine JSON-Datei können Kategorien und Inhaber bearbeitet oder hinzugefügt werden.
Eine kleine GUI ist implementiert für:
    Oberfläche
    Tabellarische Auflistung der Buchungen
    Graph für den Kontostandsverlauf

kleinere Programmierübungen sind in StartUp.py nach Abschluss stehen gelassen worden
"""

# Gibt Liste mit Buchungen zurück 
def readCsvFile(fileName):
    pointer = open(fileName)
    pointer.readline()
    lines = pointer.readlines()
    csv = list()
    for line in lines:
        eintrag = line.split(";")
        datum = datetime.strptime(eintrag[0], "%d.%m.%Y" ).date()
        eintrag[3] = eintrag[3].split(" ")
        eintrag[3][0] = float(eintrag[3][0].replace(",","."))
        buchung = Buchung(datum, eintrag[1], eintrag[2], Betrag(eintrag[3][0], eintrag[3][1]))
        csv.append(buchung)
    return csv

def binaryTreeSortBuchungen(buchungen:list[Buchung]):
    binaryTree = Node(None)
    for buchung in buchungen:
        binaryTree.insert(buchung)
    sortierteListe = list()
    return binaryTree.toList(sortierteListe)

#Gibt eine Liste an Primzahlen aus, die alle kleiner oder gleich n sind
def primzahlenBerechnung(n : int): 
    liste = list( range(2 , n  + 1))
    if n == 2:
        return [2] 
    for i in range(n + 1):
        for j in range(2 , i):
            if i % j == 0:
                liste.remove(i)
                break
    return liste

#Gibt eine Liste an vollkommenen Zahlen aus, die alle kleiner oder gleich n sind
#vollkommene Zahl = alle Teiler der Zahl ergeben addiert wieder die Zahl
def vollkommendeZahl (n): 
    liste = list ()
    for i in range(1 , n + 1):
        result = 0
        for j in range(1, i):
           
            if i % j == 0:
                result += j
        if result == i :
            liste.append(result)  
    return liste

def startUp():
    ######### CSV Datei einlesen
    buchungen = readCsvFile("./Buchungsexport.csv")
    # timestamp1 = datetime.now()
    # sortierenNachDatum(buchungen)
    # timestamp2 = datetime.now()
    # print(timestamp2 - timestamp1)
    # print(buchungen)
    # print(sortierenNachBetrag(buchungen))
    # buchungen = readCsvFile("./Buchungsexport.csv")
    # print(buchungen.sort(key=komperator))
    # print(filterNachDatum(buchungen, datetime(2019,1,2), datetime(2019,3,4)))
    # print(KategorieZuBuchungen(buchungen))
    # serializeToJson(KategorieZuBuchungen (buchungen), "test.json")
    # kategorieZuordnung = JsonKategorieAuslesen("test.json")
    # print(filternNachKategorien(buchungen , "EssenGehen" , kategorieZuordnung))
    # timestamp1 = datetime.now()
    # binaryTreeSortBuchungen(buchungen)
    # timestamp2 = datetime.now()
    # print(timestamp2 - timestamp1)
    # print(primzahlenBerechnung(1000))
    # print(vollkommendeZahl(10000))
    # inhaberZuJsonHinzufügen(input('inhaber:'), input('kategorie'), "test.json")
    # createUI(buchungen)
    # print(KontostandAnTag(buchungen, datetime(2019, 1, 1)))
    # print(getListeKategorien())
    # anzeigenGraph (buchungen)
    # print (kategorienAusgabe(buchungen))
    createUI (buchungen)
    
    return

if __name__ == "__main__":
    startUp()