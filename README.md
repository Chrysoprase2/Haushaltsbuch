# Haushaltsbuch
Dieses Programm gibt Buchungen aus, die es aus einer CSV-Datei einließt. 
Über eine JSON-Datei können Kategorien und Inhaber bearbeitet oder hinzugefügt werden.
In personalUI.py findet sich die neue UI, userInterface.py ist die alte UI.
- Programm beinhaltet: 
  ```
  - grafische Oberfläche
  - Hinzufügefunktion Buchungsobjekt
  - Tabellarische Auflistung aller Buchungen
  - Suchfunktion
  - Filterfunktion
  - grafische Ausgabe der Monatsbuchungen nach Kategorien
  - Graph für den Kontostandsverlauf
  ```

- kleinere Programmierübungen sind in StartUp.py nach Abschluss stehen gelassen worden

# Änderungen
- **neues UI**
  - **Tabellenauflistung**
  - **Scrollfunktionalität**
  - ein kleines **Startbild**, das als Platzhalter dient, bis ein Button geklickt wurde
    
- **Funktionalitäten:**
  - **Suchfunktion**: Teilstring wird über ein Textfeld eingegeben. Nach dem Klick auf "Suchen", wird jedes Element, das den eingegebenen String als Teilstring enthält ausgegeben. Relevante Attribute sind Datum, Inhaber und Betreff.
  - **Filterfunktion**: Möglichkeit nach Kategorien zu filtern. Kategorien sind via Radiobuttons auswählbar. Klickt man auf "Buchungen filtern", ohne einen Radiobutton gewählt zu haben, wird das Fenster gecleart. Buttons bleiben. 
