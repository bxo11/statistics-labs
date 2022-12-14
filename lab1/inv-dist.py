import random

import matplotlib.pyplot as plt
from math import *
import numpy as np

from utils import calculate_avg, calculate_variance

# def cauchy_gen():
#     while True:
#         x = random.uniform(-pi / 2, pi / 2)
#         y = random.uniform(0, 1)
#         cauchy = tan(x)
#         if y <= (1 / (1 + cauchy ** 2)):
#             return cauchy

def cauchy_gen2(x0, gamma):
    u = np.random.uniform(0,1)
    x = x0 + gamma * np.tan(np.pi*(u-1/2))
    return x

points_anount = 500
x = np.linspace(-5, 5, points_anount)
y = []
y0 = 0
gamma = 0.5
for p in x:
    mianownik = pi*gamma*(1+((p-y0)/gamma)**2)
    y.append(1/mianownik)

hist_data = []

for i in range(points_anount):
    # hist_data.append(cauchy_gen())
    hist_data.append(cauchy_gen2(y0, gamma))



print(f'Srednia: {calculate_avg(hist_data)}')
print(f'Wariancja: {calculate_variance(hist_data)}')

hist_data = [number for number in hist_data if number < 5]
hist_data = [number for number in hist_data if number > -5]

plt.hist(hist_data, density=True, bins=50)
plt.plot(x, y, marker='o')
plt.show()
