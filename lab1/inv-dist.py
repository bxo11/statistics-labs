import random

import matplotlib.pyplot as plt
from math import *
import numpy as np

from utils import calculate_avg, calculate_variance


def cauchy_gen():
    while True:
        x = random.uniform(-pi / 2, pi / 2)
        y = random.uniform(0, 1)
        cauchy = tan(x)
        if y <= (1 / (1 + cauchy ** 2)):
            return cauchy


points_anount = 100
x = np.linspace(-5, 5, points_anount)
y = []
wariancja = 1
wartosc_oczekiwana = 0
for p in x:
    mianownik = wariancja * sqrt(2 * pi)
    wyk = -((pow(p - wartosc_oczekiwana, 2)) / (2 * pow(wariancja, 2)))
    y.append((1 / mianownik) * exp(wyk))

hist_data = []
for i in range(points_anount):
    hist_data.append(cauchy_gen())

print(f'Srednia: {calculate_avg(hist_data)}')
print(f'Wariancja: {calculate_variance(hist_data)}')
plt.hist(hist_data, density=True, bins=15)
plt.plot(x, y, marker='o')
plt.show()
