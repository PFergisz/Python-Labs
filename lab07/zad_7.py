#! /usr/bin/env python3

import random
import math

#zad.1
print("zad.1")

# zad. 1a
print("podpunkt a")
print("petla z wynikiem zakomentowana")
def gen_1():
    x=0
    while 1:
        yield x
        x+=1

# for i in gen_1():
#     print(i)


# zad. 1b
print("\npodpunkt b")

def gen_2(seq):
    for el in seq:
        if (sum(i for i in range(1, el) if el%i==0) == el and sum != 0):
            yield el

lista = [(i) for i in range(100)]

for i in gen_2(lista):
    print(i, end=' ')

# zad. 1c
print("\n\npodpunkt c")

def gen_3(seq, num):
    for el in seq:
        if el>num:
            return
        yield el
    
for i in gen_3(lista, 11):
    print(i, end=' ')


#zad. 1d
print("\n\npodpunkt d")

for el in gen_2(gen_3(gen_1(), 10000)):
    print(el, end=' ')


#zad.2
print("\nzad.2")

def gen_4():
    u_0 = 0
    x_0 = 1 
    a = 0.05
    # u_i = u_0
    x_i = x_0 - a
    while 1:
        x_i += a
        u_0 = u_0 + a / x_i
        yield(x_i, u_0-0.05, math.log(x_i))
        if x_i > 1.5:
            return

for el in gen_4():
    print(el)




#zad.3
print("\nzad.3")

def gen_5(num):
    k=0
    sin=0
    while 1:
        sin+=((-1)**k)/(math.factorial(1+2*k))*(num**(1+2*k))
        yield (k, math.sin(num), sin)
        k+=1

        if math.fabs(math.sin(num)-sin)<(10**(-8)):
            return 


for el in gen_5(5):
    print(el)


#zad.4
print("\nzad.4")

def gen_6(*args):
    if len(args) == 1:
        start, stop = 0, args[0]
        if args[0] < 0:
            step = -1
        else:
            step = 1

    elif len(args) == 2:
        start, stop = args[0], args[1]
        if args[1] < args[0]:
            step = -1
        else:
            step = 1
    
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    
    else:
        return "Error - funkcja przyjmuje od 1 do 3 parametrów"
    
    
    return (start + step * x for x in range(math.ceil((stop - start) / step)))

print(list(gen_6(10)))
print(list(gen_6(-10)))
print(list(gen_6(1,10)))
print(list(gen_6(10,1)))
print(list(gen_6(1,10,2)))
print(list(gen_6(1,10,-2)))
print(list(gen_6(10,1,2)))
print(list(gen_6(10,1,-2)))


#zad.5
print("\nzad.5")

def gen_7():
    while 1:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if(math.fabs(y-x)>0.4):
            yield y
        x, y = y, x
        if y < 0.1:
            return 

for el in gen_7():
    print(el)



