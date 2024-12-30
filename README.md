# Library_Python_Mathieu_Vanderwee


Boekenbeheer
Bekijk boeken: Toon een lijst van alle boeken in de database.
Voeg een nieuw boek toe: Voeg een nieuw boek toe door een titel, auteur en jaar op te geven.
Bewerk een boek: Bewerk de gegevens van een bestaand boek door het ID, nieuwe titel, auteur en jaar in te voeren.
Verwijder een boek: Verwijder een boek uit de database door het ID op te geven.
Gebruikersbeheer
Bekijk gebruikers: Toon een lijst van alle gebruikers in de database.
Voeg een nieuwe gebruiker toe: Voeg een nieuwe gebruiker toe door een naam en e-mailadres in te vullen.
Bewerk een gebruiker: Bewerk de gegevens van een bestaande gebruiker door het ID, nieuwe naam en e-mailadres op te geven.
Verwijder een gebruiker: Verwijder een gebruiker uit de database door het ID op te geven.
Exporteren
Exporteren naar CSV: Exporteer de gegevens van een tabel (boeken of gebruikers) naar een CSV-bestand.
Exporteren naar Excel: Exporteer de gegevens van een tabel (boeken of gebruikers) naar een Excel-bestand.

Vereisten
Python 3.x
Virtuele omgeving (aanbevolen)
De volgende Python-pakketten:
sqlite3 (standaard inbegrepen in Python)
pandas
openpyxl

Installatie-instructies
Kloon de repository
git clone <repo_url>  
cd <repo_folder>  

Maak een virtuele omgeving aan en activeer deze
python -m venv venv  
source venv/bin/activate  # Voor Mac/Linux  
venv\Scripts\activate     # Voor Windows  

Installeer de vereiste pakketten
pip install -r requirements.txt  

De database staat hier al in dus moet je niet meer van ergens halen

Voer het programma uit
python main.py  

Voorbeeldgebruik

Boekenbeheer

Voeg een boek toe:
Bij uitvoeren via het interactieve menu:
Titel: Harry Potter  
Auteur: J.K. Rowling  
Jaar: 1997  


Gebruikersbeheer

Voeg een gebruiker toe:
Bij uitvoeren via het interactieve menu:
Gebruikersnaam: John Doe  
Email: john.doe@example.com  
Exporteren naar CSV:
Geef de tabelnaam (bijvoorbeeld books of users) op in het menu.

Exporteren naar Excel:
Geef de tabelnaam (bijvoorbeeld books of users) op in het menu.
