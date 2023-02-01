import random

N = 100  # inaczej N_j / populacja
t = 12 # ilosc osobnikow zlowionych w danym pomiarze
repeats = 5
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
m = 0 # liczba ponownie zlowionych osobnikow

for i in range(repeats):
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

print(f'')
