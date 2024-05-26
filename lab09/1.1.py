#! /usr/bin/env python3

"""modul zaimplementowanych funkcji"""



def Luhn_algorithm(nmbr):           #numer karty jest stringiem
    """Funkcja sprawdzająca poprawność numeru karty kredytowej """
    waga_dict={0:1,1:2}
    #od 15 do 0 - prawa
    if not int(nmbr):
        raise ValueError('tlyko liczby!')
        
    if len(nmbr)<16:
        raise ValueError
        
    lista=[int(val) for val in nmbr]
    for i in range(len(nmbr)):      #iterujemy : [0,15]
        indeks=15-i
        if indeks%2:                #jezeli indeks karty jest nieparzysty
            liczba=lista[i]
            if liczba>=10:
                lista[i]=int(str(liczba)[0])+int(str(liczba)[1])
            else:
                lista[i]=liczba*2   
    suma=sum(value*waga_dict[(15-indeks)%2] for indeks,value in enumerate(lista))
    if suma%10:
        raise ArithmeticError('zla suma kontrolna')
        
    return True    


def pesel_check(pesel,obj,plec):               #wszystko to sa stringi
    """Funkcja sprawdzająca poprawność numeru PESEL"""
    miesiac_dict={18:80,19:0,20:20,21:40,22:60}
    waga_dict={0:1,1:3,2:7,3:9,4:1,5:3,6:7,7:9,8:1,9:3,10:3}
    print(len(waga_dict))
    if len(pesel)!=11:
        raise ValueError('zla dlugosc peselu')
        
    if pesel[:2]!=str(obj.year)[2:]:
        raise ValueError('nie zgadz asie rok')
        
    if pesel[2:4]!=str(obj.month+int(miesiac_dict[int(str(obj.year)[2:])])):
        raise ValueError('nie zgadz asie miesiac')
        
    if int(pesel[4:6])!=obj.day:
        raise ValueError('nie zgadza sie dzie ur.')
        
    if (int(pesel[6:10])%2 and plec=='mezczyzna') or (not int(pesel[6:10])%2 and plec=='kobieta'):
        raise ValueError('nie zgadz asie plec')
        
    if sum(int(pesel[i])*waga_dict[i] for i in len(pesel))!=int(pesel[-1]):
        raise ArithmeticError

    return True    

def sredni_wiek(filename):
    with open(filename) as plik:
        for line in plik:
            dzien, miesiac,rok=line.split()


if __name__=='__main__':
    pass            
    

























import zadanka
import datetime
#help(zadanka)
#help(zadanka.card)

try:
    #zadanka.card("924803")
    #zadanka.card("1234567898765437")
    #zadanka.card("1234567891234564")
    zadanka.card("1234567891234.63")
except ValueError as ex_v:
    print('Zle dane')
except zadanka.SizeError as ex_s:
    print('Zly rozmiar')
except zadanka.CheckError as ex_ch:
    print('Zla suma kontrolna')


try:
    zadanka.pesel("02261506979", datetime.date(2002, 6, 14), "m")
except ValueError as ex_v:
    print('Zle dane')
except zadanka.PESELError as ex_p:
    print('Zly pesel')
except zadanka.CheckError as ex_ch:
    print('Zla suma kontrolna')
except zadanka.YearError as ex_y:
    print('Zly rok')











    """
Modul zawierajacy 3 funkcje:
card - sprawdzająca poprawnosc numeru karty
pesel - sprawdzajaca poprawnosc numeru pesel
avg_age - zwracajaca sredni wiek osob z pliku
"""
import logging
logging.basicConfig(filename="test.log", filemode='w', format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.debug('debug')
logger.info('info')
logger.warning('warining')
logger.error('error')
logger.critical('critical')

class SizeError(Exception):
    """
    Wyjatek zwracany przy niepopranej dlugosci
    """
    pass

class CheckError(Exception):
    """
    Wyjatek zwracany przy niepopranej sumie kontrolnej
    """
    pass

class YearError(Exception):
    """
    Wyjatek zwracany przy niepoprawnym roku urodzenia
    """
    pass

class PESELError(Exception):
    """
    Wyjatek zwracany przy niepoprawnym peselu
    """
    pass
def card(x):
    '''
    Funkcja przyjmuje numer karty i sprawdza jego poprawnosc
    '''
    if len(x) != 16:
        raise SizeError
    elif not x.isdigit():
        raise ValueError

    mapa = list(map(int, x))
    lista = [2*mapa[i] if i%2 == 0 else mapa[i] for i in range(16)]
    nowa_lista = [(liczba%10 + liczba//10) if liczba > 10 else liczba for liczba in lista]
    nowsza_lista = [nowa_lista[i]*2 if i %2 ==0 else nowa_lista[i] for i in range(16)]
    suma = sum(nowsza_lista)
    if suma%10 != 0:
        raise CheckError
    else:
        print("Numer karty jest poprawny")


import datetime

def pesel(p, d, s):
    '''
    Funkcja przyjmuje pesel date oraz plac po czym sprawdza poprawnosc peselu
    '''
    if not p.isdigit():
        raise ValueError
    if s not in ("m", "k"):
        raise ValueError

    mapa = list(map(int, p))
    
    if 1800 <=  d.year  <= 1899:
        mapa[2] -= 8
    elif 2000 <= d.year  <= 2099:
        mapa[2] -= 2
    elif 2100 <= d.year  <= 2199:
        mapa[2] -= 4
    elif 2200 <= d.year  <= 2299:
        mapa[2] -= 6
    else:
        raise YearError
    if (mapa[0]*10 + mapa[1]) != d.year % 100 or (mapa[2]*10 + mapa[3]) != d.month or (mapa[4]*10 + mapa[5]) != d.day:
        raise PESELError
    elif mapa[9] % 2 == 1 and s != "m" or mapa[9] % 2 == 0 and s != "k":
        raise PESELError
    if 1800 <=  d.year  <= 1899:
        mapa[2] += 8
    elif 2000 <= d.year  <= 2099:
        mapa[2] += 2
    elif 2100 <= d.year  <= 2199:
        mapa[2] += 4
    elif 2200 <= d.year  <= 2299:
        mapa[2] += 6
    wykladnik = 1
    lista = []
    for i in range(10):
        lista.append(mapa[i]*wykladnik)
        wykladnik +=2
        if wykladnik == 5:
            wykladnik = 7
        wykladnik = wykladnik%10
    suma = 0
    for i in range(10):
        suma+= lista[i]%10
    suma_contr = suma%10
    suma_contr = 10 - suma_contr
    if suma_contr != mapa[10]:
        raise CheckError
    else:
        print("Poprawny PESEL")
            
def avg_age(plik, mode):
    if mode not in ("l", "r"):
        raise ValueError
    iterator = 0
    suma = 0
    with open(plik) as source:
        for line in source:
            data = line.split()
            if len(data) != 3 and mode == "r":
                raise ValueError
            elif len(data) != 3 and mode == "l":
                continue
            data_liczby = [int(data[i]) for i in range(3)]
            if data_liczby[2] < 1 or data_liczby[2] > 12 and mode == "r":
                raise ValueError
            elif data_liczby[2] < 1 or data_liczby[2] > 12 == "l":
                continue
            if data_liczby[3] < 1 or data_liczby[2] > 31 and mode == "r":
                raise ValueError
            elif data_liczby[2] < 1 or data_liczby[2] > 31 == "l":
                continue
            if (data_liczby[0]%400 == 0 or (data_liczby[0]%100 != 0 and data_liczby[0]%4 == 0)) and data_liczby[1] == 2:
                pass
            iterator += 1
            


if __name__ == '__main__':
    pass









