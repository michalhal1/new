import csv
import random

def zaczytaj_plik(sciezka):
    dane =[]
    file = open(sciezka, "r")
    return csv.reader(file)


def pobierz_etykiety(plik_csv):
    return next(plik_csv)


def pobierz_dane(plik_csv):
    dane = []
    for wiersz in plik_csv:
        dane.append(wiersz)
    return dane

# def zaczytaj(sciezka, czy_etykiety):
#     dane = []
#     file = open(sciezka, "r")
#     plik_csv = csv.reader(file)
#     etykiety = []

#     if czy_etykiety == True:
#         etykiety = next(plik_csv)

#     for wiersz in plik_csv:
#         dane.append(wiersz)
#     liczba_wierszy = len(dane)
#     file.close
#     return etykiety, dane, liczba_wierszy


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
    
    trening = []
    test = []
    walidacja = []
    random.shuffle(zaczytane)
    liczebność_a = round(a*len(zaczytane))
    liczebność_b = round(b*len(zaczytane))
    liczebność_c = round(c*len(zaczytane))
    trening = zaczytane[1:liczebność_a]
    test = zaczytane[liczebność_a:liczebność_a+liczebność_b]
    walidacja = zaczytane[liczebność_a+liczebność_b:liczebność_a+liczebność_b+liczebność_c]
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


def zapisz_liste(lista, sciezka):
    import pandas as pd
    if not isinstance(lista, pd.DataFrame):
        pd.DataFrame(lista)
    lista.to_excel(sciezka)


def uruchom_menu():


    etykiety = None
    dane_z_pliku = None
    sciezka = None
    etykiety_w_pliku = None
    uruchom = 1
    trening = []
    test=[]
    walidacja=[]
    print("Witaj w programie")
    print("Podaj scieżkę")
    sciezka = input("Ścieżka: ")
    csv_file = zaczytaj_plik(sciezka)
    etykiety_w_pliku = input("Czy w pliku sa etykiety? [T/N]: ")

    if etykiety_w_pliku == "T":
        etykiety = pobierz_etykiety(csv_file)

    dane_z_pliku = pobierz_dane(csv_file)

    while uruchom == 1:
        panel = input("Co chcesz zrobić? \n Wpisz 'A', żeby wyswietlić wtykiety \n Wpisz 'B', żeby wyświetlić dane \n Wpisz 'C', żeby podzielić dataset \n Wpisz 'D', żeby uzyskać informacją na temat liczby klas i ich liczebnośc \n Wpisz 'E', żeby wyswetlić dane dla podanej klasy \n Wpisz 'F', zeby zapisać dowolną listę \n Wpisz 'Q', żeby wyjść z konsoli \n")

        if panel == "A":
            print(etykiety)

        if panel == "B":
            wyswietl_dane(dane_z_pliku)

        if panel == "C":
            print("Podaj procentową liczebność zbioru treningowego,testowego i walidacyjnego")
            treningowy = float(input("Zbiór treningowy: "))
            testowy = float(input("Zbiór testowy: "))
            walidacyjny = float(input("Zbiór walidacyjny: "))
            trening, test, walidacja = podziel_dataset(dane_z_pliku, treningowy, testowy, walidacyjny)
            print("Zbiory danych dostępnę są jako listy o nazwach: trening, walidacja, test")


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
            print("Podaj listę, którą chcesz zapisać")
            nazwa_listy = input("Nazwa listy: ")
            print("Podaj ścieżkę do zapisu")
            scieżka_do_zapisu = input("Ścieżka: ")
            zapisz_liste(nazwa_listy, scieżka_do_zapisu)

        if panel =="Q":
            uruchom = 0
    



#x = zaczytaj_plik(r"C:\Users\micha\Downloads\iris.csv")
#y = pobierz_dane(x)
# # # # pokaz_etykiety(x)
# # # # wyswietl_dane(x)
#trening, test, walidacja = podziel_dataset(y, 0.1, 0.2, 0.7)
# # # # liczba_klas(x,4) #deklarujemy numer kolumny w której znajdują się klasie
# # # # wyswietl_klase(x,4, "versicolor")
# # # # zapisz_liste(trening, r"C:\Users\micha\OneDrive\Dokumenty\test1.xlsx")
#print(test)

uruchom_menu()