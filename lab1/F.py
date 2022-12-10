import random
from collections import defaultdict

from matplotlib import pyplot as plt

# liczba symulacji
N = 1000

# kapitał początkowy dla gracza A i B
a = b = 50

# prawdopodobieństwo wygranej gracza A w jednej rozgrywce
pA = 0.5

# tablica z liczbami rozgrywek n, dla których będą wykonane symulacje
ns = [2, 10, 20, 50, 100]

# słownik, w którym kluczem jest liczba rozgrywek, a wartością słownik zawierający
# liczbę wystąpień danego kapitału po n rozgrywkach
results = defaultdict(lambda: defaultdict(int))

# pętla po liczbach rozgrywek
for n in ns:
  # pętla po symulacjach
  for i in range(N):
    # symulacja gry
    for j in range(n):
      # losowanie wyniku rozgrywki
      if random.random() < pA:
        # gracz A wygrywa
        b -= 1
      else:
        # gracz B wygrywa
        a -= 1

    # zapisanie wyniku symulacji
    results[n][a] += 1

    # przywrócenie kapitału graczy na początkowe wartości
    a = b = 50

# wyświetlenie histogramu prawdopodobieństwa P(M) dla każdej liczby rozgrywek
# plt.hist(results, density=True, bins=50)
# plt.show()

for n in ns:
  print(f"Histogram dla n = {n}:")
  for k, v in results[n].items():
    print(f"P({k}) = {v/N}")
  print()