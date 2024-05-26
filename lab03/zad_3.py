#! /usr/bin/env python3

import string

#zad.1
print("zad.1")

import sys

if len(sys.argv)<2:
    print("Brak argumentow wywolania")
    sys.exit()

st=''.join(sys.argv[1:])
print(st)

#zad.2
print("\nzad.2")

lower_letters=[x for x in st if x.islower()]
print(lower_letters)

upper_letters=[x for x in st if x.isupper()]
print(upper_letters)

digits=[x for x in st if x.isdigit()]
print(digits)

non_letters=[x for x in st if not x.isalpha()]
print(non_letters)

#zad.3
print("\nzad.3")

no_repetitions=[]
for x in lower_letters:
    if x not in no_repetitions:
        no_repetitions.extend(x)
    
print(no_repetitions)

letters_tuple=[(i, lower_letters.count(i)) for i in no_repetitions]

print(letters_tuple)

#zad.4
print("\nzad.4")
print(sorted(letters_tuple,key=lambda x: x[1], reverse=True))

#zad.5
print("\nzad.5")

a=0
for i in 'aeiouy':
    a+=st.lower().count(i)

b=0
for i in string.ascii_letters:
    b+=st.lower().count(i)
b-=a

print(a,b)

function_tuple=[(x,a*int(x)+b) for x in digits]
print(function_tuple)

#zad.6
print("\nzad.6")

average_x=sum(int(x) for x in digits)/len(digits)


d=sum((float(x) - average_x)**2 for x in digits)


a=sum(int(x)*(int(i)-average_x) for i,x in function_tuple)/d
print(a)

average_y=sum(int(x) for i,x in function_tuple)/len(function_tuple)

b=average_y-a*average_x
print(b)





