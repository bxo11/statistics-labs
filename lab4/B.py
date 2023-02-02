import math
import random
from math import factorial

import scipy


def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def hypergeometric_pmf(m, Nj, t, M):
    a=scipy.special.binom(M, m)
    b = scipy.special.binom(Nj - M, t - m)
    c =scipy.special.binom(Nj, t)
    return (a * b) / c


N = 1000  # inaczej N_j / populacja
t = 12  # ilosc osobnikow zlowionych w danym pomiarze
repeats = 10
population_list = [x for x in range(N)]
repeats_dict = {n: 0 for n in range(N)}  # calkowita ilosc wylosowanych osobnikow i powtorzenia
bayes = 0

new_pool = []
previous_pool = []
polled_again = []
prior = 1 / 2000
likelihood = 0
posterior = 0
to_norm = 2000
M = 0  # calkowita ilosc oznakowamych osob
m = 0  # liczba ponownie zlowionych osobnikow

aaaa= scipy.special.binom(-5, 5)

for j in range(repeats):
    t = int(random.uniform(40, 60))
    for i in range(2000):
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
        likelihood = hypergeometric_pmf(m, 2000, t, M)
        posterior = likelihood * prior / to_norm
        prior = posterior



