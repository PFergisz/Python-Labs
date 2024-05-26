#! /usr/bin/env python3

import random
import string
import sys



#zad.1
print("zad.1")

args=''
args=args.join(sys.argv)
args=args.removeprefix(str(sys.argv[0]))


def fun1(equation):
    tr = str.maketrans({string.ascii_letters.replace("x", "")[i]: str(random.randint(0, 9)) for i in range(len(string.ascii_letters.replace("x", "")))})
    equation = equation.translate(tr)
    result = [(x, eval(equation)) for x in [random.random() for i in range(10)]]
    return result


print(fun1(args))




#zad.2
print("zad.2")

def lista2(*args):
    result = []
    for i in args[0]:
        for arr in args[1:]:
            if i not in arr:
                break
        else:
            result.append(i)
    return result
 

l1 = [1, 2, 3]
l2 = [1, 3, 5]
l3 = [3, 2]
print(lista2(l1, l2, l3))

l1 = [1, 2, 3]
l2 = [1, 3, 5]
l3 = [3, 2, 1]
print(lista2(l1, l2, l3))

#zad.3
print("zad.3")

def fun3(sek1, sek2, par = True):
    return [(sek1[i] if i < len(sek1) else None, sek2[i] if i < len(sek2) else None) for i in range(max(len(sek1), len(sek2)) if par else min(len(sek1), len(sek2)))] 


l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e', 'f']

print(fun3(l1, l2, False))
print(fun3(l1, l2, True))

#zad.4
print("zad.4")

def fun4(n):
    triangle = [[1]]
    triangle[0].append(0)
    for i in range(1,n):
        row=[1]
        for j in range(1,i):
            row.append(triangle[i-1][j-1]+ triangle[i-1][j-1])
        row.append(1)
        row.append(0)
        triangle.append(row)
    return triangle

n=6
result=fun4(n)
for row in result:
    print (row)


#zad.5
print("zad.5")

def fun5(a, minimum, maximum, guess):
    steps = 0
    while True:
        my_guess = random.randint(minimum, maximum) if guess == "r" else minimum + (maximum-minimum)//2
        if my_guess == a:
            return steps

        if my_guess < a:
            minimum = my_guess
        if my_guess > a:
            maximum = my_guess
        steps += 1

b = 20
print("Kroki potrzebne do znalezienia szukanej liczby przy uzyciu wartosci domyslnej: ", fun5(b, 0, 100, "r"))
print("Kroki potrzebne do znalezienia szukanej liczby bez uzycia wartosci domyslnej: ", fun5(b, 0, 100, "a"))










