1. Proszę napisać funkcję, która pozwoli na wypisanie: n początkowych wierszy pliku, n końcowych wierszy pliku, co n-tego wiersza pliku, n-tego słowa ze wszystkich wierszy i n-tego znaku ze wszystkich wierszy. Nazwę pliku oraz n przekazujemy jako parametr do funkcji. Każdy podpunkt==jedna linia kodu (1.5p)

2. Odczytujemy wartości ze wszystkich plików, których nazwy rozpoczynają się od data i kończą na in w katalogu bieżącym. Na wyjściu proszę utworzyć jeden plik z trzema kolumnami:
pierwsza kolumna - numer wiersza,
druga kolumna - uśredniona wartość z danego wiersza ze wszystkich plików (numpy.average),
trzecia kolumna - odchylenie standardowe wartości z danego wiersza ze wszystkich plików (numpy.std)
(2.5p)
PLIKI TESTOWE: data.zip
data0.in data1.in ... data.out
2            3               0 2.5   0.5
3            3.5            1 3.25 0.25
5            5               2 5      0


3. Proszę napisać funkcję, tworzącą plik z instrukcjami pozwalającymi na wygenerowanie wykresu plików j.w. + wynikowego (łącznie z odchyleniem standardowym)*patrz niżej, proszę skorzystać z potrójnego cudzysłowa (1p)

4. Pliki o nazwach rok.in (rank.zip) zawierają informację o pozycji na liście rankingowej pewnych osób, w kolejnych latach. Proszę utworzyć zbiorczy plik, w którym w pierwszej kolumnie znajdzie się "nazwisko", kolejne kolumny będą odpowiadały pozycji danej osoby na liście rankingowej w kolejnych latach, od 2000 do 2020 (2.5p)
2000.txt
ABC 2
DEF 1
GHJ 3
2001.txt
ABC 3
DEF 1
GHJ 2
KLM 4
rank.out
Nazwisko 2000 2001
ABC         2       3
DEF         1       1
GHJ         3       2
KLM         -       4


5. Proszę sporządzić histogram słów rozpoczynających się na daną literę alfabetu (dla całego alfabetu) ze wszystkich plików pasujących do określonego wzorca w katalogu bieżącym, opcje wyświetlenia: sortowanie alfabetyczne, bądź po liczbie słów (2.5p)
PLIKI TESTOWE: zad5A.in, zad5B.in, zad5C.in

* Matplotlib jest biblioteką do tworzenia wykresów (https://matplotlib.org/). Wykorzystamy ją do wygenerowania prostego wykresu. Poniżej minimum konieczne, aby ten cel osiągnąć:

import matplotlib.pyplot as plt
#wyrysowanie krzywej y(x), 'o' oznacza styl punktu
plt.plot(x, y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
plt.errorbar(x, y, marker='*', yerr=dy)
#opis osi
plt.xlabel('x')
#zapis do pliku, format określony przez rozszerzenie w nazwie
plt.savefig('res.pdf')

A to może się przydać do łatwego wczytywania plików (ale dzisiaj można z tego skorzystać tylko w skrypcie generującym wykresy)

import numpy
x,y=numpy.loadtxt(nazwa, unpack=True)
