#! /usr/bin/env python3
'''
Modul z funkcjami

'''

import datetime
import logging

logging.basicConfig(filename='test.log', filemode='w', format='%(asctime)s %(message)s')

logger=logging.getLogger()
logger.setLevel(0)

# logger.debug('debug')
# logger.info('info')
# logger.warning('warning')
# logger.error('error')
# logger.critical('critical')


class SizeError(Exception):
    """
    Niepoprawna dlugosc liczby
    """
    pass

class CheckError(Exception):
    '''
    Niepoprawna suma kontrolna karty
    '''
    pass
class YearError(Exception):
    '''
    Niepoprawny rok
    '''

class PeselError(Exception):
    '''
    Niepoprawny numer pesel
    '''

def check_card(x):
    '''
    Funkcja sprawdzajaca poprawnosc numeru karty
    '''
    logger.info('Wywolanie funkcji check_card')
    if len(x) != 16:
        logger.error('Size error')
        raise SizeError
    elif not x.isdigit():
        logger.error('Value error')
        raise ValueError

    numery = list(map(int, x))
    lista = [2*numery[i] if i%2 == 0 else numery[i] for i in range(16)]
    lista_2 = [(num//10 + num%10) if num >= 10 else num for num in lista]
    suma = sum(lista_2)
    if suma%10 != 0:
        logger.error('Check error')
        raise CheckError
    else:
        logger.info('Poprawne wywolanie')
        print("Numer karty jest poprawny")





def pesel_check(pesel, data, plec):
    '''
    Funkcja przyjmuje pesel date oraz plac po czym sprawdza poprawnosc peselu
    '''
    logger.info('Wywolanie funkcji pesel_check')
    if not pesel.isdigit():
        logger.error('Value error')
        raise ValueError
    if plec not in ("m", "k"):
        logger.error('Value error')
        raise ValueError

    lista_4 = list(map(int, pesel))
    if 1800 <=  data.year  <= 1899:
        lista_4[2] -= 8
    elif 2000 <= data.year  <= 2099:
        lista_4[2] -= 2
    elif 2100 <= data.year  <= 2199:
        lista_4[2] -= 4
    elif 2200 <= data.year  <= 2299:
        lista_4[2] -= 6
    else:
        logger.error('Year error')
        raise YearError

    if (lista_4[0]*10 + lista_4[1]) != data.year % 100 or (lista_4[2]*10 + lista_4[3]) != data.month or (lista_4[4]*10 + lista_4[5]) != data.day:
        logger.error('PESEL error')
        raise PeselError
    elif lista_4[9] % 2 == 1 and plec != "m" or lista_4[9] % 2 == 0 and plec != "k":
        logger.error('PESEL error')
        raise PeselError

    if 1800 <=  data.year  <= 1899:
        lista_4[2] += 8
    elif 2000 <= data.year  <= 2099:
        lista_4[2] += 2
    elif 2100 <= data.year  <= 2199:
        lista_4[2] += 4
    elif 2200 <= data.year  <= 2299:
        lista_4[2] += 6

    wykladnik = 1
    lista_5 = []

    for i in range(10):
        lista_5.append(lista_4[i]*wykladnik)
        wykladnik +=2
        if wykladnik == 5:
            wykladnik = 7
        wykladnik = wykladnik%10
    suma = 0
    for i in range(10):
        suma+= lista_5[i]
    kontr = suma%10
    kontr = 10 - kontr
    if kontr != lista_4[10]:
        logger.error('Check error')
        raise CheckError
    else:
        print("Poprawny PESEL")
    

def avg_age(file, mode):
    if mode not in ("l", "r"):
        raise ValueError
    it = 0
    suma = 0
    with open(file) as plk:
        for line in plk:
            lista_6 = line.split()
        #     if len(lista_6) != 3 and mode == "r":
        #         logger.error('Value error')
        #         raise ValueError
        #     lista_7 = [int(lista_6[i]) for i in range(3)]
        #     if lista_7[2] < 1 or lista_7[2] > 12 and mode == "r":
        #         raise ValueError
        #     if lista_7[3] < 1 or lista_7[3] > 31 and mode == "r":
        #         raise ValueError

        #     if (lista_7[0]%400 == 0 or (lista_7[0]%100 != 0 and lista_7[0]%4 == 0)) and lista_7[1] == 2:
        #         pass
        #     iterator += 1
        






        
            



