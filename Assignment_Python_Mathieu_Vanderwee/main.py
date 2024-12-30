import sqlite3
import csv
import pandas as pd

# Functies voor boeken
def view_books():
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        if books:
            print("Boeken in de database:")
            for book in books:
                print(f"ID: {book[0]}, Titel: {book[1]}, Auteur: {book[2]}, Jaar: {book[3]}")
        else:
            print("Geen boeken gevonden.")
    except sqlite3.Error as e:
        print(f"Fout bij het verbinden met de database: {e}")
    finally:
        conn.close()

def add_new_book(title, author, year):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, published_year) VALUES (?, ?, ?)",
            (title, author, year)
        )
        conn.commit()
        print(f"Boek '{title}' succesvol toegevoegd.")
    except sqlite3.Error as e:
        print(f"Fout bij het toevoegen van het boek: {e}")
    finally:
        conn.close()

def edit_book_with_id(book_id, new_title, new_author, new_year):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        if book is None:
            print(f"Geen boek gevonden met ID {book_id}.")
            return

        cursor.execute(
            "UPDATE books SET title = ?, author = ?, published_year = ? WHERE id = ?",
            (new_title, new_author, new_year, book_id)
        )
        conn.commit()
        print(f"Boek met ID {book_id} succesvol bijgewerkt.")
    except sqlite3.Error as e:
        print(f"Fout bij het bijwerken van het boek: {e}")
    finally:
        conn.close()

def delete_book_by_id(book_id):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()

        print(f"Boek met ID {book_id} succesvol verwijderd.")
    except sqlite3.Error as e:
        print(f"Fout bij het verwijderen van het boek: {e}")
    finally:
        conn.close()

# Functies voor gebruikers
def view_users():
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        if users:
            print("Gebruikers in de database:")
            for user in users:
                print(f"ID: {user[0]}, Naam: {user[1]}, Email: {user[2]}")
        else:
            print("Geen gebruikers gevonden.")
    except sqlite3.Error as e:
        print(f"Fout bij het ophalen van gebruikers: {e}")
    finally:
        conn.close()

def add_new_user(username, email):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email)
        )
        conn.commit()
        print(f"Gebruiker '{username}' succesvol toegevoegd.")
    except sqlite3.Error as e:
        print(f"Fout bij het toevoegen van de gebruiker: {e}")
    finally:
        conn.close()

def edit_user_with_id(user_id, new_username, new_email):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        if user is None:
            print(f"Geen gebruiker gevonden met ID {user_id}.")
            return

        cursor.execute(
            "UPDATE users SET username = ?, email = ? WHERE id = ?",
            (new_username, new_email, user_id)
        )
        conn.commit()
        print(f"Gebruiker met ID {user_id} succesvol bijgewerkt.")
    except sqlite3.Error as e:
        print(f"Fout bij het bijwerken van de gebruiker: {e}")
    finally:
        conn.close()

def delete_user_by_id(user_id):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()

        print(f"Gebruiker met ID {user_id} succesvol verwijderd.")
    except sqlite3.Error as e:
        print(f"Fout bij het verwijderen van de gebruiker: {e}")
    finally:
        conn.close()

# Exporteren naar CSV
def export_to_csv(table_name):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if rows:
            filename = f"{table_name}.csv"
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([description[0] for description in cursor.description])  # Kolomnamen
                writer.writerows(rows)
            print(f"Gegevens van '{table_name}' succesvol geëxporteerd naar {filename}.")
        else:
            print(f"Geen gegevens gevonden in de tabel '{table_name}'.")
    except sqlite3.Error as e:
        print(f"Fout bij het exporteren naar CSV: {e}")
    finally:
        conn.close()

# Exporteren naar Excel
def export_to_excel(table_name):
    try:
        conn = sqlite3.connect('library.db')

        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        if not df.empty:
            filename = f"{table_name}.xlsx"
            df.to_excel(filename, index=False)
            print(f"Gegevens van '{table_name}' succesvol geëxporteerd naar {filename}.")
        else:
            print(f"Geen gegevens gevonden in de tabel '{table_name}'.")
    except Exception as e:
        print(f"Fout bij het exporteren naar Excel: {e}")
    finally:
        conn.close()

# Interactief menu
def main_menu():
    while True:
        print("\n--- Beheer Menu ---")
        print("1. Bekijk boeken")
        print("2. Voeg een boek toe")
        print("3. Bewerk een boek")
        print("4. Verwijder een boek")
        print("5. Bekijk gebruikers")
        print("6. Voeg een gebruiker toe")
        print("7. Bewerk een gebruiker")
        print("8. Verwijder een gebruiker")
        print("9. Exporteer naar CSV")
        print("10. Exporteer naar Excel")
        print("11. Afsluiten")
        choice = input("Kies een optie (1-11): ")

        if choice == "1":
            view_books()
        elif choice == "2":
            title = input("Titel: ")
            author = input("Auteur: ")
            year = input("Jaar: ")
            add_new_book(title, author, year)
        elif choice == "3":
            book_id = int(input("Boek ID: "))
            new_title = input("Nieuwe titel: ")
            new_author = input("Nieuwe auteur: ")
            new_year = input("Nieuw jaar: ")
            edit_book_with_id(book_id, new_title, new_author, new_year)
        elif choice == "4":
            book_id = int(input("Boek ID: "))
            delete_book_by_id(book_id)
        elif choice == "5":
            view_users()
        elif choice == "6":
            username = input("Gebruikersnaam: ")
            email = input("Email: ")
            add_new_user(username, email)
        elif choice == "7":
            user_id = int(input("Gebruiker ID: "))
            new_username = input("Nieuwe gebruikersnaam: ")
            new_email = input("Nieuwe email: ")
            edit_user_with_id(user_id, new_username, new_email)
        elif choice == "8":
            user_id = int(input("Gebruiker ID: "))
            delete_user_by_id(user_id)
        elif choice == "9":
            table_name = input("Tabelnaam (books/users): ")
            export_to_csv(table_name)
        elif choice == "10":
            table_name = input("Tabelnaam (books/users): ")
            export_to_excel(table_name)
        elif choice == "11":
            print("Programma afgesloten.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main_menu()
