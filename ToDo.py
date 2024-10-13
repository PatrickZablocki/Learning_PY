def anzeigen(todo_liste):
    if not todo_liste:
        print("Die ToDo-Liste ist Leer")
    else:
        print("ToDo-Liste:")
        for idx, aufgabe in enumerate(todo_liste, 1):
            print(f"{idx}. {aufgabe}")

def aufgaben_hinzufügen(todo_liste):
    aufgabe = input("Gib die neue Aufgabe ein:")
    todo_liste.append(aufgabe)
    print(f"Aufgabe '{aufgabe}' wurde hinzugefügt.")

def aufgaben_etfernen(todo_liste):
    anzeigen(todo_liste)
    try:
        index = int(input("Welche Aufgabe möchtest du entfernen (Nummer eingeben)? ")) - 1
        if 0 <= index < len(todo_liste):
            entfernte_aufgabe = todo_liste.pop(index)
            print(f"Aufgabe '{entfernte_aufgabe}' wurde entfernt.")
        else:
            print("Ungültige Nummer.")
    except ValueError:
        print("Bitte eine gültige Zahl eingeben")

def main():
    todo_liste = []
    while True:
        print("\nWas möchtest du tun?")
        print("1. Aufgaben anzeigen")
        print("2. Aufgabe hinzufügen")
        print("3. Aufgabe entfernen")
        print("4. Beenden")
        auswahl = input("Wähle eine Option (1-4): ")

        if auswahl == "1":
            anzeigen(todo_liste)
        elif auswahl == "2":
            aufgaben_hinzufügen(todo_liste)
        elif auswahl == "3":
            aufgaben_etfernen(todo_liste)
        elif auswahl == "4":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle eine Option zwischen 1 und 4.")

if __name__ == "__main__":
    main()