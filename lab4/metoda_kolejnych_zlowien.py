import random

N = 100  # inaczej N_j
t = 20
look_repeat = 5
population_list = [x for x in range(N)]
repeats_dict = {}  # calkowita ilosc wylosowanych osobnikow i powtorzenia # suma wartosci jest = M
bayes = 0
for n in range(N):
    repeats_dict[n] = 0

new_pool = []
previous_pool = []
polled_again = []
prior = 0
likelihood = 0
posterior = 0
to_norm = 0
for i in range(look_repeat):
    previous_pool = new_pool
    new_pool = []
    random.shuffle(population_list)
    for id in range(t):
        x = population_list[id]  # zlowiony element
        new_pool.append(x)
        repeats_dict[x] = repeats_dict[x] + 1

    polled_again = []
    for element in previous_pool:
        if element in new_pool:
            polled_again.append(element)
    # print(polled_again)

# for i in repeats_dict:
#     if repeats_dict[i]>0: print(repeats_dict[i])
# print(x)
