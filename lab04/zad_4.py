#! /usr/bin/env python3

import random
import collections
import string

#zad.1
print("zad.1")

k=random.randint(1,10)
lista=[random.randrange(0, 5*k) for i in range (k)]
print(lista)


lista_kopia=lista[::]
dictionary = collections.defaultdict(int)


for i in range(100):
    random.shuffle(lista)
    
    for j in range(len(lista_kopia)):
        if lista_kopia[j] == lista[j]:
            dictionary[j] += 1
print(dictionary)

#zad.2
print("zad.2")

st=""
for i in range(k):
    st=".".join(random.choices(string.ascii_lowercase, k=k))
print(st)

#zad.3

lista_2=[random.randrange(0,20) for i in range (100)]
#print(lista_2)

#zad.3a
print("zad.3a")

dictionary_2 = {}
for i, v in enumerate(lista_2):
    dictionary_2.setdefault(v, []).append(i)
print (dictionary_2)
#zad.3b
print("zad.3b")

dictionary_3 = {}
for i in lista_2:
    dictionary_3.setdefault(i, []).append(lista_2.index(i, 0 if not dictionary_3[i] else dictionary_3[i][-1]+1))
print(dictionary_3)

#zad.4
print("zad.4")

n = random.randint(3, 6)

palindromy={k: len([0 for i in range(1000) if(str(t:=random.randint(int('1'+'0'*(n-1)), int('9'*n)))==str(t)[::-1])])}
print(palindromy)

#zad.5
print("zad.5")

dictionary_4 = {i : random.randrange(0,100) for i in range(10)}
dictionary_5 = {i : random.randrange(0,100) for i in range(10)}
dictionary_4={i:j for j,i in dictionary_4.items()}
print(dictionary_5)
dictionary_5={i:j for j,i in dictionary_5.items()}
print(dictionary_5)

dictionary_6={i: (dictionary_4[i], dictionary_5[i]) for i,v in dictionary_4.items() if i in dictionary_5}
print(dictionary_6)





