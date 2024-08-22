from dataclasses import dataclass
import Node
from Buchung import Buchung 

@dataclass
class Node:
    value: Buchung
    links: Node = None 
    rechts: Node = None

    def insert(self, buchung : Buchung):
        if self.value == None:
            self.value = buchung
            return
        if self.links == None and self.value.datum >= buchung.datum:
            self.links = Node(buchung)
            return
        if self.value.datum >= buchung.datum:
            self.links.insert(buchung)
            return
        if self.rechts == None and self.value.datum < buchung.datum:
            self.rechts = Node(buchung)
            return
        if self.value.datum < buchung.datum:
            self.rechts.insert(buchung)            
        return
    
    #von links nach rechts - aufsteigend
    def toList(self, liste:list):
        if self.links != None:
            self.links.toList(liste)
        liste.append(self.value)
        self.links = None    
        if self.rechts != None:
            self.rechts.toList(liste)
            self.rechts = None   
        return liste
        
        
