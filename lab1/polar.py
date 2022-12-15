import random

import matplotlib.pyplot as plt
from math import *
import numpy as np

from utils import calculate_avg, calculate_variance
def polar():
    while (1):
        x1 = random.uniform(-1, 1)
        x2 = random.uniform(-1, 1)
        R = x1 * x1 + x2 * x2
        if R < 1 and R != 0:
            break
    y1 = sqrt(-2 * log(R) / R) * x1
    y2 = sqrt(-2 * log(R) / R) * x2
    return y1


# def polar_method_normal_distribution():
#     while True:
#         u1, u2 = 0, 0
#         while u1 == 0:
#             u1 = random.random()
#         while u2 == 0:
#             u2 = random.random()
#         z0 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
#         yield z0

if __name__ == "__main__":
    points_anount = 500
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
        hist_data.append(polar())

    # for value in polar_method_normal_distribution():
    #     if len(hist_data)>points_anount:
    #         break
    #     hist_data.append(value)

    print(f'Srednia: {calculate_avg(hist_data)}')
    print(f'Wariancja: {calculate_variance(hist_data)}')
    plt.hist(hist_data, density=True, bins=25)
    plt.plot(x, y, marker='o')
    plt.show()
