import random as rd

#A= [1/x for x in range(1,10)]
#print(A)

# x = [[rd.randint(1, 10) for i in range(4)] for j in range(4)]
# print(x)

# y = [x[i][i] for i in range(4)]
# print(y)

# słowniki i zamiana klucza z wartością
# produkty = {"jaja": "szt",
# "pomidory": "kg",
# "mleko": "l",
# "chleb": "szt"}


# filtrowanie = [key for key, value in produkty.items() if value == "szt"]

# print(filtrowanie)


# def podaj_imie(arg_pozycyjny):    
#     return 'Witaj ' + arg_pozycyjny

# print(podaj_imie('Michal'))


# def funckja_n(arg_pozycyjny, arg_domyslny=4):
#     for i in range(arg_pozycyjny):
#         print(str(arg_pozycyjny) * arg_pozycyjny)


# funckja_n(3)



# # symbol * oznacza dowolną ilość argumentów przechowywanych w krotce
# def ciag(* liczby):
#       # jeżeli nie ma argumentów to
#     if len(liczby) == 0:
#         return 0.0
#     else:
#         iloczyn = 0.0
#     # sumujemy elementy ciągu
#     for i in liczby:
#         iloczyn = iloczyn+1 * i  
#     # zwracamy wartość sumy
#     return iloczyn

# # wywołanie gdy brak argumentów
# print(ciag(6))
# # podajemy argumenty
# print(ciag(1,2,3,4,5,6,7,8))


# def zakupy(** zakupy):
#      print(sum(zakupy.values()))       

# zakupy(slodycze=2, rozrywka=4)

# plik matma.py
"""deklaracja funkcji w prostym module"""


import matma 
print(matma.dodaj(1, 2))

