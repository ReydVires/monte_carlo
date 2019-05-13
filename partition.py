from numpy import genfromtxt
import math
# import numpy as np


def get_min(tab):
    min = tab[0]
    for i in range(len(tab)):
        if tab[i] < min:
            min = tab[i]
    return min


def get_max(tab):
    max = tab[0]
    for i in range(len(tab)):
        if tab[i] > max:
            max = tab[i]
    return max

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

# partition A
i_value = calculate_i(weight, data)
print(f'Hasil partisi random uniform bag. A: {i_value}')

data = genfromtxt('RandDist.csv', delimiter='')
btm = get_min(data)
top = get_max(data)
weight = (top - btm) / N
print(btm, top, weight)

# partition B
i_value = calculate_i(weight, data)
print(f'Hasil partisi random uniform bag. B: {i_value}')

# w = np.random.uniform(2, 4, 200)
# print(w)
# w.tofile('RandUnif.csv', '\n', '%s')

# r = np.random.normal(0.5, math.sqrt(0.5), 200)
# print(r)
# r.tofile('RandDist.csv', '\n', '%s')
