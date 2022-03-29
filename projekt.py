def zaczytaj(sciezka, czy_etykiety):
    dane = []
    import csv
    file = open(sciezka, "r")
    plik_csv = csv.reader(file)
    etykiety = []

    if czy_etykiety == True:
        etykiety = next(plik_csv)

    for wiersz in plik_csv:
        dane.append(wiersz)
    liczba_wierszy = len(dane)
    file.close
    return etykiety, dane, liczba_wierszy


def pokaz_etykiety(zaczytane):
    etykiety, dane, liczba_wierszy = zaczytane
    if not etykiety:
        print("Brak etykiet!")
    else:
        print(etykiety)


def wyswietl_dane(zaczytane, od=1, do=-1):
    etykiety, dane, liczba_wierszy = zaczytane
    for i in dane[od:do]:
        print(i)


def podziel_dataset(zaczytane, a, b, c):
    etykiety, dane, liczba_wierszy = zaczytane
    import random
    random.shuffle(dane)
    liczebność_a = round(a*len(dane))
    liczebność_b = round(b*len(dane))
    liczebność_c = round(c*len(dane))
    trening = dane[1:liczebność_a]
    test = dane[liczebność_a:liczebność_b]
    walidacja = dane[liczebność_b:liczebność_c]
    return trening, test, walidacja


def liczba_klas(zaczytane, numer_kolumny):
    etykiety, dane, liczba_wierszy = zaczytane
    list(dane)
    wartosci = []
    for x in range(1, len(dane)):
        wartosci.append((dane[x][numer_kolumny]))
    for y in set(wartosci):
        print(y, wartosci.count(y))


def wyswietl_klase(zaczytane, numer_kolumny, nazwa):
    etykiety, dane, liczba_wierszy = zaczytane
    list(dane)
    for x in range(1, len(dane)):
        if dane[x][numer_kolumny] == nazwa:
            print(dane[x])


def zapisz_liste(lista, sciezka):
    import pandas as pd
    if not isinstance(lista, pd.DataFrame):
        pd.DataFrame(lista)
    lista.to_excel(sciezka)




x = zaczytaj(r"C:\Users\micha\Downloads\iris.csv", True)
pokaz_etykiety(x)
wyswietl_dane(x)
trening, test, walidacja = podziel_dataset(x, 0.1, 0.2, 0.7)
liczba_klas(x,4) #deklarujemy numer kolumny w której znajdują się klasie 
wyswietl_klase(x,4, "versicolor")
zapisz_liste(trening, r"C:\Users\micha\OneDrive\Dokumenty\test1.xlsx")

