#! /usr/bin/env python3

import time
import sys
import random
import math




#zad.1
print("zad.1")


powt = 1000
N = 10000

def forStatement():
    lista = []
    for i in range(N):
        lista.append(i)
    return lista

def listComprehension():
    lista = [(i) for i in range(N)]
    return lista 

def mapFunction():
    lista = map(lambda x: (x), range(N))
    return list(lista)

def generatorExpression():
    lista = ((i) for i in range(N))
    return list(lista)

def tester(fn):
    actual_time=time.time_ns()
    for i in range(powt):
        fn()
    return time.time_ns() - actual_time

print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

print("\n\nObliczone wartości zostały dodane jako komentarz w kodzie programu")

# 1)
# Dodawanie elementu
# forStatement         => 186641860
# listComprehension    => 145682680
# mapFunction          => 354037
# generatorExpression  => 501341

# 2)
# Dodawanie elementu podniesionego do kwadratu
# forStatement         => 384711746
# listComprehension    => 346885800
# mapFunction          => 353181
# generatorExpression  => 503227

# 3)
# Sumowanie elementów z wykorzystaniem pętli for
# forStatement         => 424369536
# listComprehension    => 381508504
# mapFunction          => 249400976
# generatorExpression  => 246210826

# 4)
# Sumowanie z wykorzystaniem funkcji sum
# forStatement         => 217659704
# listComprehension    => 173854181
# mapFunction          => 357223691
# generatorExpression  => 257778002

# 5)
# Konwersja obiektu map i generatora do listy
# forStatement         => 187946493
# listComprehension    => 147779672
# mapFunction          => 349542728
# generatorExpression  => 252164501



#zad.2
print("\nzad.2")

def Monte_Carlo(N):
    return 4*len(list(filter(lambda x: x[0]**2 + x[1]**2 <= 1, ((random.random(), random.random()) for i in range(N)))))/N 


print("Wyznaczona wartosc PI wynosi: ", Monte_Carlo(N))







#zad.3
print("\nzad.3")

def function_3(lista_x, lista_y):
    x_avg=sum(lista_x)/len(lista_x)
    y_avg=sum(lista_y)/len(lista_y)

    D = sum(map(lambda x: (x - x_avg)**2, lista_x))
    
    a = sum(map(lambda x,y: y*(x-x_avg), lista_x, lista_y))/D
    b = y_avg - a*x_avg
    
    delta_y = math.sqrt(sum(map(lambda x,y: (y - (a*x + b))**2, lista_x, lista_y))/(len(lista_x)-2))
    delta_a = delta_y/math.sqrt(D)
    delta_b = delta_y * math.sqrt(1/len(lista_x) + (x_avg**2)/D)
    return a, b, delta_a, delta_b

n = 100
lista_y = [2*i+1+random.random() for i in range(n)]

print("a, b, delta_a, delta_b:")
print(function_3(range(n), lista_y))






#zad.4
print("\nzad.4")

def myreduce(func, lista):
    r = lista[0]
    for x in lista[1:]:
        r = func(r, x)
    return r

print("Wynik funkcji dla dodawania: ", myreduce(lambda x,y: x+y, [1, 2, 3, 4]))
print("Wynik funkcji dla mnozenia:  ", myreduce(lambda x,y: x*y, [1, 2, 3, 4]))



#zad.5
print("\nzad.5")

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

max_in_row = list(map(max, matrix_1))
print(max_in_row)

max_in_col = list(map(max, zip(*matrix_1)))
print(max_in_col)


matrix_2 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

def sum_of_mat(*mat):
	return [[sum(col) for col in zip(*rows)] for rows in zip(*mat)]

print(sum_of_mat(matrix_1, matrix_2))




