from dataclasses import dataclass
from datetime import date
from Betrag import Betrag

@dataclass
class Buchung:
    datum: date
    inhaber: str
    betreff: str
    betrag: Betrag


