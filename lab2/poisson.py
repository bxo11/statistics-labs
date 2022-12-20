import math
import random

import numpy as np
from matplotlib import pyplot as plt

from utils import calculate_avg


def poisson_pmf(k, lambda_param):
    return (math.pow(lambda_param, k) * math.exp(-lambda_param)) / math.factorial(k)


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

        result -= 1
        global_results.append(result)

    return global_results

if __name__ == "__main__":
    t_list = [1, 10, 20, 90]
    lenght_list = [6,20,40,120]
    lam = 1

    for iter, t in enumerate(t_list):
        events = calculate_avg(poisson_simulation(lam, t))

        poisson_distribution = []
        for i in range(t):
            # poisson_distribution.append(
            #     ((lam*t ) ** i / (math.factorial(i)) * math.e ** (-lam * t))
            # )
            poisson_distribution.append(poisson_pmf(i, 1))

        # plt.plot([i  for i in range(t)], poisson_distribution, marker='o')
        # # plt.axvline(events, color='r')
        # plt.title(f't = {t}, porownanie rozkladu Poissona z parametrem')
        # plt.xlabel('')
        # plt.ylabel('')

        k_values = range(0, lenght_list[iter])
        pmf_values = [poisson_pmf(k, lam*t) for k in k_values]

        # Plot the PMF of the Poisson distribution
        plt.plot(k_values, pmf_values, color='r')

        events = poisson_simulation(lam, t, 1000)
        print(f'Wartość średnia dla t = {t}: {calculate_avg(events)} != { lam *t}')
        counts, values = np.histogram(events)
        probabilities = counts / len(events)
        plt.bar(values[:-1], probabilities, width=1)
        plt.title(f't = {t}, rozkład prawdopodobieństwa ilości zdarzeń')
        plt.show()
