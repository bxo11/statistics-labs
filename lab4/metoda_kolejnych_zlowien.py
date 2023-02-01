import random

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import hypergeom


def plot_geom():
    M = 100  # Total number of items
    n = 50  # M
    N = 7  # t

    M = 50  # Total number of items
    n = 20  # M
    N = 9  # t

    # Draw the samples from the hypergeometric distribution
    rv = hypergeom(M, n, N)
    x = np.arange(0, 10)
    pmf_vals = rv.pmf(x)
    return pmf_vals


N = 50  # inaczej N_j / populacja
t = 20  # ilosc osobnikow zlowionych w danym pomiarze
repeats = 1000
population_list = [x for x in range(N)]
repeats_dict = {n: 0 for n in range(N)}  # calkowita ilosc wylosowanych osobnikow i powtorzenia
bayes = 0

new_pool = []
previous_pool = []
polled_again = []
prior = 0
likelihood = 0
posterior = 0
to_norm = 0
M = 0  # calkowita ilosc oznakowamych osob
m = 0  # liczba ponownie zlowionych osobnikow

m_history = []
for j in range(repeats):
    for i in range(2):
        previous_pool = new_pool
        new_pool = []
        polled_again = []
        M = 0
        m = 0
        random.shuffle(population_list)

        for e in range(t):
            x = population_list[e]  # zlowiony element
            new_pool.append(x)
            if x in previous_pool:
                polled_again.append(x)
            repeats_dict[x] += 1

        m = len(polled_again)

        for e in repeats_dict:
            if repeats_dict[e] > 0:
                M += 1

        t = 12
    m_history.append(m)

plt.hist(m_history, density=True, bins=[x for x in range(10)])
plt.title(f'')
plt.xlabel(f'')
plt.ylabel(f'')

pmf_vals = plot_geom()
plt.plot([x for x in range(len(pmf_vals))], pmf_vals, 'o--')
plt.title("Hypergeometric PMF")
plt.xlabel("Number of success (k)")
plt.ylabel("Probability")
plt.show()
