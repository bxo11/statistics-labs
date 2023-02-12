import math
import random
from math import factorial

import matplotlib.pyplot as plt
import scipy


def binomial(n, kt):

    if kt < 0 or kt > n:
        return 0
    if kt == 0 or kt == n:
        return 1
    if kt == 1 or kt == n - 1:
        return n
    res = n
    for ik in range(2, kt + 1):
        res *= (n - ik + 1) / ik

    return round(res)


def getPM(m, NJ, ts, Ms):
    Mm = binomial(Ms, m)
    NJm = binomial(NJ - Ms, ts - m)
    Njt = binomial(NJ, ts)
    if Njt == 0:
        return 0
    return (Mm * NJm) / Njt


def getPN(m, NJ, t, Ma):
    b = 0
    for i in range(0, N2, 10):
        pm = getPM(m, i, t, Ma) * Ni[i]
        b += pm
    return (getPM(m, NJ, t, Ma) * Ni[NJ]) / b


def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def hypergeometric_pmf(m, Nj, t, M):
    a = scipy.special.binom(M, m)
    b = scipy.special.binom(Nj - M, t - m)
    c = scipy.special.binom(Nj, t)
    if c == 0:
        return 0
    return (a * b) / c

N = 1000  # inaczej N_j / populacja
t = 12  # ilosc osobnikow zlowionych w danym pomiarze
repeats = 10
population_list = [x for x in range(N)]
repeats_dict = {n: 0 for n in range(N)}  # calkowita ilosc wylosowanych osobnikow i powtorzenia

N2 = N * 2
Ni = []
for i in range(N2 + 1):
    Ni.append(1 / N2)

new_pool = []
previous_pool = []
polled_again = []
M = 0  # calkowita ilosc oznakowamych osob
m = 0  # liczba ponownie zlowionych osobnikow
m2 =0

for j in range(repeats):
    t = int(random.uniform(40, 60))

    previous_pool = new_pool
    new_pool = []
    polled_again = []

    m2=0
    M = 0
    random.shuffle(population_list)

    for e in range(t):
        x = population_list[e]  # zlowiony element
        new_pool.append(x)
        if repeats_dict[x] > 0:
            m2 += 1
        if x in previous_pool:
            polled_again.append(x)
            m+=1
        repeats_dict[x] += 1

    # m2+= len(polled_again)

    for e in repeats_dict:
        if repeats_dict[e] > 0:
            M += 1

    x = []
    y = []
    y2 = []
    nextNi = []
    for i in range(N2 + 1):
        nextNi.append(0)

    for i in range(0, N2, 15):
        if j == 0:
            a = Ni[i]
            a2= Ni[i]
        else:
            a = getPN(m, i, t, M)
            a2 = getPN(m2, i, t, M)
        nextNi[i] = a
        x.append(i)
        y.append(a)
        y2.append(a2)
    print(m,m2, t, M)
    Ni = nextNi
    # likelihood = hypergeometric_pmf(m, i+1, t, M)
    # posterior = likelihood * prior / to_norm
    # prior = posterior
    # if j ==repeats-1:
    # plt.plot(x, y)
    plt.plot(x, y2 ,'r')
    plt.title(j)
    plt.show()
