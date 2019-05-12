from numpy import genfromtxt
import math


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
print(f'nilai weight: {weight}\nNilai I yang diperoleh: {i_value}')
