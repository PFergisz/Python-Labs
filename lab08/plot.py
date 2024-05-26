#! /usr/bin/env python3
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
