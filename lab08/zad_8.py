#! /usr/bin/env python3

import numpy as np
import glob
import matplotlib.pyplot as plt
import string

#zad.1
print("zad.1")

def function_1(plik, n):
    with open(plik) as pl:
        lines=pl.readlines()
        print(lines[:n])
        print()
        print(lines[-n:])
        print()
        print(lines[::n])
        print()
        print([line.split()[n-1] for line in lines if n<=len(line.split())])
        print()
        print([line[n - 1] for line in lines if n <= len(line)])






function_1("rank/2000.txt", 2)




#zad.2
print("\nzad.2")


def function_2():
    files = glob.glob("data/data*in")

    lista = []


    for file in files:
        with open(file) as pl:
            wiersze = [float(value) for value in pl.readlines()]
            lista.append(wiersze)



    average = list(map(np.average, zip(*lista)))
    std = list(map(np.std, zip(*lista)))


    with open("wyniki.out", "w") as file:
        for i in range(len(average)):
            file.write(f"{i + 1}\t{average[i]}\t{std[i]}\n")
        
function_2()

print("Wyniki mozna znalezc w pliku wyniki.out")




#zad.3
print("\nzad.3")


def function_3(file):
    l = """#! /usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import glob

x, y_average, y_std = np.loadtxt("wyniki.out", unpack=True)

files = glob.glob("data/data*in")

for file in files:
    y = np.loadtxt(file, unpack=True)
    plt.plot(x, y, 'o')

plt.errorbar(x, y_average, marker='*', yerr=y_std)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('wykresy.pdf')
"""
    with open(file, "w") as plk:
        plk.write(l)

function_3("plot.py")

print("Nazwa tworzonej funkcji to plot.py, wykresy zostają zapisane do pliku wykresy.pdf")


#zad.4
print("\nzad.4")

files = glob.glob("rank/*.txt")

lista_4 = {}
lata = [i for i in range(2000, 2021)]

for file in files:
    with open(file) as plk:
        lines=plk.readlines()
        for line in lines:
            if len(line.split()) == 2:
                nazwisko, place = line.split()
                place = int(place)
                # poniewaz rank/ jest dodawane do nazwy
                year = int(file[5:9])

                lista_4.setdefault(nazwisko, {}).setdefault(year, place)

with open ("wyniki.txt", "w") as plk:
    naglowek = ["Nazwisko"]+[str(rok) for rok in lata]
    plk.write("\t". join(ngl for ngl in naglowek) + "\n")
    # for nazwisko, values in sorted(lista_4.items()):
    #     line_data = [nazwisko]
    #     year_rank = {lata : place for lata, place in values}
        
        # rank = []
        # for year in lata:
        #     if year in values:
        #         rank.append(year)
        #     else:
        #         rank = "-"

        # plk.write("\t".join(rank) + "\n")








#zad.5
print("\nzad.5")















