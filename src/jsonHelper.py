import json

#fügt neuen Inhaber in Json Datei hinzu
# gibt True zurück, wenn das Hinzufügen funktioniert hat
def inhaberZuJsonHinzufügen (inhaber:str, kategorie:str, path:str = "test.json"):
    referenzDict = JsonKategorieAuslesen(path)
    if kategorie == "" or inhaber == "":
        return False
    if kategorie not in referenzDict.keys():
        referenzDict[kategorie] = list()

    if inhaber not in referenzDict[kategorie]:
        referenzDict[kategorie].append (inhaber)
        serializeToJson(referenzDict, path)
    return True

#Überschreibt Json Datei
def serializeToJson (KategorieZuBuchungen, path:str):
    pointer = open (path, mode='w+')
    pointer.write (json.dumps (KategorieZuBuchungen))
    return

#Gibt Dictonarie zurück, welches einer Katogorie eine Liste von Inhabern zuordnet
def JsonKategorieAuslesen (path:str = "test.json")->dict:
    pointer = open (path)
    line=pointer.readline()
    kategorieDict = json.loads (line)
    return kategorieDict


def getListeKategorien ():
    kategorieDict = JsonKategorieAuslesen()
    return list(kategorieDict.keys())
