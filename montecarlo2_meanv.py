from numpy import genfromtxt
import math
from scipy.stats import norm


def f(x):
    return math.pow(x, 3) + (3 * math.pow(x, 2)) + (3 * x) + 1


def fa(tab, n):
    _sum = 0
    for i in range(len(tab)):
        _sum += f(tab[i])
    return _sum / n


def calculate_vf(tab, f_, n):
    _sum = 0
    for i in range(len(tab)):
        _sum += math.pow(f(tab[i]) - f_, 2)
    return (1/(n-1)) * _sum


data = genfromtxt('RandUnif.csv', delimiter='')
btm = 2
top = 4
N = len(data)
prob = 0.95
k = norm.ppf(prob)

f_aksen = fa(data, N)
# print("f':", f_aksen)

Vf = calculate_vf(data, f_aksen, N)
# print("Vf:", Vf)

Vf_aksen = Vf/N
# print("Vf':", Vf_aksen)

# mean-variance
lower = (top - btm) * (f_aksen - (k * Vf_aksen))
upper = (top - btm) * (f_aksen + (k * Vf_aksen))

print(f'Hasil mean-variance\n[{lower}, {upper}]')
