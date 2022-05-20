import csv
import random


def zaczytaj_plik(sciezka):
    dane = []
    file = open(sciezka, "r")
    return csv.reader(file)


def pobierz_etykiety(plik_csv):
    return next(plik_csv)


def pobierz_dane(plik_csv):
    dane = []
    for wiersz in plik_csv:
        dane.append(wiersz)
    return dane


def pokaz_etykiety(zaczytane):
    etykiety, dane, liczba_wierszy = zaczytane
    if not etykiety:
        print("Brak etykiet!")
    else:
        print(etykiety)


def wyswietl_dane(zaczytane, od=1, do=-1):
    for i in zaczytane[od:do]:
        print(i)


def podziel_dataset(zaczytane, a, b, c):
    random.shuffle(zaczytane)
    liczebność_a = round(a*len(zaczytane))
    liczebność_b = round(b*len(zaczytane))
    liczebność_c = round(c*len(zaczytane))
    trening = zaczytane[1:liczebność_a]
    test = zaczytane[liczebność_a:liczebność_a+liczebność_b]
    walidacja = zaczytane[liczebność_a + liczebność_b:liczebność_a+liczebność_b+liczebność_c]
    return trening, test, walidacja


def liczba_klas(zaczytane, numer_kolumny):
    list(zaczytane)
    wartosci = []
    for x in range(1, len(zaczytane)):
        wartosci.append((zaczytane[x][numer_kolumny]))
    for y in set(wartosci):
        print(y, wartosci.count(y))


def wyswietl_klase(zaczytane, numer_kolumny, nazwa):
    list(zaczytane)
    for x in range(1, len(zaczytane)):
        if zaczytane[x][numer_kolumny] == nazwa:
            print(zaczytane[x])
        # else: print("Taka nazwa klasy nie istnieje!")


def zapisz_liste(lista, sciezka):
    import pandas as pd
    lista = pd.DataFrame(list(lista))
    lista.to_excel(sciezka)


def uruchom_menu():

    etykiety = None
    dane_z_pliku = None
    sciezka = None
    etykiety_w_pliku = None
    uruchom = 1
    global trening, test,  walidacja
    print("Witaj w programie")
    print("Podaj scieżkę")
    sciezka = input("Ścieżka: ")
    csv_file = zaczytaj_plik(sciezka)

    while True:
                    
        etykiety_w_pliku = input("Czy w pliku sa etykiety? [T/N]: ")
                    
        if etykiety_w_pliku != "T" and etykiety_w_pliku != "N":
            print("Wpisz wartość T lub N")
            continue
        else:
            break
   
    if etykiety_w_pliku == "T":
        etykiety = pobierz_etykiety(csv_file)

    dane_z_pliku = pobierz_dane(csv_file)

    while uruchom == 1:
        panel = input("Co chcesz zrobić? \n Wpisz 'A', żeby wyswietlić etykiety \n Wpisz 'B', żeby wyświetlić dane \n Wpisz 'C', żeby podzielić dataset \n Wpisz 'D', żeby uzyskać informacją na temat liczby klas i ich liczebnośc \n Wpisz 'E', żeby wyswetlić dane dla podanej klasy \n Wpisz 'F', zeby zapisać listę \n Wpisz 'Q', żeby wyjść z konsoli \n")

        if panel == "A":
            print(etykiety)

        if panel == "B":
            wyswietl_dane(dane_z_pliku)

        if panel == "C":
            print("Podaj procentową liczebność zbioru treningowego,testowego i walidacyjnego")
            
            while True:
                try:
                    treningowy = float(input("Zbiór treningowy: "))
                    testowy = float(input("Zbiór testowy: "))
                    walidacyjny = float(input("Zbiór walidacyjny: "))
                except ValueError:
                    print("Wpisz wartość liczbową")
                    continue
                else:
                    break
                     
            if treningowy+ testowy + walidacyjny <= 1:
                trening, test, walidacja = podziel_dataset(dane_z_pliku, treningowy, testowy, walidacyjny)
                print("Zbiory danych dostępnę są jako listy o nazwach: trening, walidacja, test")
            else: print("Suma współczynników przekracza 1!")

        if panel == "D":
            print('Podaj liczbę kolumny, w której znajduje się klasa')
            numer_kolumny = int(input("Numer kolumny:"))
            liczba_klas(dane_z_pliku, numer_kolumny)

        if panel == "E":
            print('Podaj liczbę kolumny, w której znajduje się klasa')
            numer_kolumny = int(input("Numer kolumny:"))
            print('Wpisz nazwę klasy')
            nazwa_klasy = input('Nazwa klasy:')
            wyswietl_klase(dane_z_pliku, numer_kolumny, nazwa_klasy)

        if panel == "F":
            zbior = input(
                "Podaj listę, którą chcesz zapisać: \n Wpisz 1 - zbiór walidacyjny,\n 2 - zbiór testowy, \n 3 - zbiór treningowy")
            print(zbior)
            if zbior == '1':
                nazwa_listy = walidacja
            elif zbior == '2':
                nazwa_listy = test
            elif zbior == '3':
                nazwa_listy = trening
            else:
                print("błędna deklaracja")
            print("Podaj ścieżkę do zapisu")
            scieżka_do_zapisu = input("Ścieżka: ")
            zapisz_liste(nazwa_listy, scieżka_do_zapisu)

        if panel == "Q":
            uruchom = 0



uruchom_menu()
