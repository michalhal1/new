#1

# a = input("Wpisz zdanie\n")
# #spacje=sum(1 for item in a if item==" ")
# spacje = a.count(" ")
# print(spacje)

#2
# import sys
# print("Podaj pierwszą liczbę")
# s = sys.stdin.readline() #Wczytuje wiersz
# print("Podaj druga liczbę")
# s1 = sys.stdin.readline()
# f = int(s)*int(s1)
# # Do wydruku można użyć też komendy write np.
# sys.stdout.write(str(f))


#3 

# a = (input("Podaj liczbę"))
# b = (input("Podaj liczbę"))
# c = (input("Podaj liczbę"))

# if a.isdigit and b.isdigit and c.isdigit:
#     a = int(a)
#     b = int(b)
#     c = int(c)


# if 0 < a < 11 and (a > b or b > c):
#     print("Warunki spełnione")
# else:
#     print("Warunki niespełnione")

#4 
# i=0
# while i<=50:
#     print(i)
#     i += 1




# #5

# a = input("Podaj liczby\n")
# lista = a.split(" ")

# for i in lista:
#     print(int(i) * int(i))


#6 
# lista1 = []
# while True:
#     a= input("Podaj liczbę")
#     if a == "STOP":
#         break
#     else:      
#      lista1.append(a)

# print(lista1)

# 7

# input = input("Wpisz liczbę wielocyfrową")
# i=1
# suma = []
# while i<=len(input):
#     suma.append(int(input[i-1]))
#     i+=1

# print(sum(suma))


# #7

# input = int(input("ile linijek?"))
# a = "A"
# i=1
# if input>10:
#     input=10
# while i<=input:
#     print(a*i)
#     i += 1

#8


# for y in range(1,11):
#     for x in range(1,11):
#         print (x*y)
   
#9 

# a= int(input("Wpisz liczbę"))
# i,j,j1, n =1
# m=0
# a1=a
# lista = []
# lista1 = []

# while i<=a:
#     lista.append(i)  
#     lista1.append(int(a/2-m))
#     i+=2
#     m+=1

# while a1>1:
#     a1-=2
#     lista.append(a1)
#     lista1.append(n)
#     n+=1


# for j, j1 in zip(lista,lista1):
#     print(" " * j1 + "o" * j)

#B = [x ** 2 for x in range(10)]
#print('B')