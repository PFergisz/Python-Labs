#! /usr/bin/env python3

#zad.1
k=[8,0,17,1,10,13,19,13,10,3,11,12,]
print(k)

for i in range(len(k)-1,-1,-1):
    if k[i] == 10:
        del k[i]
        
print(k)

#zad.2
k=[8,0,17,1,10,13,19,13,10,3,11,12,]
print(k)

while 10 in k:
    k.remove(10)
print(k)

#zad.3
k=[8,0,17,1,10,13,19,13,10,3,11,12,]

for i in range(1, len(k), 2):
    print(k[i], end=", ")
print()

#zad.4
k=[8,0,17,1,10,13,19,13,10,3,11,12,]

print(k[1::2])

#zad.5

k=[8,0,17,1,10,13,19,13,10,3,11,12,]
for i in range (len(k)-1, -1, -2):
    print(k[i], end=", ")
print()

#zad.6
k=[8,0,17,1,10,13,19,13,10,3,11,12,]

print(k[-1::-2])

#zad.7
k=[8,0,17,1,10,13,19,13,10,3,11,12,]

m=[(i,j) for i,j in enumerate(k)]
print(m)

#zad.8
c=m[:]
c.sort(key=lambda x: x[1])
print(c)

#zad.9
k=[8,0,17,1,10,13,19,13,10,3,11,12,]

m=[(i,j) for i,j in enumerate(k) if not j%2]
print(m)

#zad.10

k=[8,0,17,1,10,13,19,13,10,3,11,12,]

m=[(i,j) if i<j else (j,i) for i,j in enumerate(k)]
print(m)

#zad.11

max=10
min=5

#ad a

k=[[1 if i>=(max-min)/2 and i<(max-(max-min)/2) and j>=(max-min)/2 and j<(max-(max-min)/2) else 0 for i in range(max)] for j in range(max)]
for i in k:
    print(i)
print()

#ad b
k=[[1 if i==j else 0 for i in range(max)] for j in range(max)]
for i in k:
    print(i)
print()

#ad c
k=[[1 if i+j==max-1 else 0 for i in range(max)] for j in range(max)]
for i in k:
    print(i)
print()

#ad d
k=[[1 if i+j==max-1 or i==j else 0 for i in range(max)] for j in range(max)]
for i in k:
    print(i)
print()

#ad e
k=[[1 if (i+j)%2 else 0 for i in range(max)] for j in range(max)]
for i in k:
    print(i)
print()




