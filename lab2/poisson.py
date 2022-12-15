import math
import random

import numpy as np
from matplotlib import pyplot as plt

from utils import calculate_avg


def poisson_simulation(lam, t, N=1):
    global_results = []
    for n in range(N):
        result = 0
        t_start = 0

        while t_start < t:
            u = random.random()
            ti = -math.log(u) / lam
            t_start = t_start + ti
            result = result + 1

        global_results.append(result)

    return global_results


t_list = [1, 10, 20, 90]
lam = 1

for t in t_list:
    events = calculate_avg(poisson_simulation(lam, t))

    poisson_distribution = []
    for i in range(t * lam + 1):
        poisson_distribution.append(
            (lam * t) ** i / (math.factorial(i) * math.e ** (-lam * t))
        )

    plt.plot([i + 1 for i in range(t * lam + 1)], poisson_distribution, marker='o')
    plt.axvline(events, color='r')
    plt.xlabel('')
    plt.ylabel('')
    plt.show()

for t in t_list:
    events = poisson_simulation(lam, t, 10000)
    print(f'Wartość średnia dla t = {t} różni się od oczekiwanej: {calculate_avg(poisson_simulation(lam, t))} != {lam * t}')
    counts, values = np.histogram(events)
    probabilities = counts / len(events)
    plt.bar(values[:-1], probabilities, width=1)
    plt.title(t)
    plt.show()
