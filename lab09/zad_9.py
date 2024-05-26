#! /usr/bin/env python3

import datetime
import module
# help(module)


#zad.1
print("zad.1")

try:
    # module.check_card('924803')
    # module.check_card('1234567898765437')
    # module.check_card('1234567891234564')
    module.check_card('1234567891234563')

except ValueError as ex_value:
    print('Zle dane')
except module.SizeError as ex_size:
    print('Zly rozmiar')
except module.CheckError as ex_check:
    print('Zla suma kontrolna')



#zad.2
print("\nzad.2")



try:
    #przykladowy pesel z generatora
    module.pesel_check('01240239276', datetime.date(2001, 4, 2), 'm')

except ValueError as ex_value:
    print('Zle dane')
except module.PeselError as ex_pesel:
    print('PESEL error')
except module.YearError as ex_year:
    print('Year error')

















#zad.3
print("\nzad.3")


try:
    module.avg_age("daty.in", "l")
except ValueError as ex_value:
    print('Zle dane')




