from numpy import genfromtxt
import math
import numpy as np


def f(x):
    return math.pow(x, 3) + (3 * math.pow(x, 2)) + (3 * x) + 1


def calculate_i(w, data_tab):
    _sum = 0
    for i in range(len(data_tab)):
        _sum += w * f(data_tab[i])
    return _sum


data = genfromtxt('RandUnif.csv', delimiter='')
btm = 2
top = 4
N = len(data)
weight = (top - btm) / N

# partition
i_value = calculate_i(weight, data)
print(f'Weight: {weight}, I: {i_value}')

# w = np.random.uniform(2, 4, 200)
# print(w)
# w.tofile('RandUnif.csv', '\n', '%s')

# r = np.random.normal(0.5, math.sqrt(0.5), 200)
# print(r)
# r.tofile('RandDist.csv', '\n', '%s')
