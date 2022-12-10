import random
import matplotlib.pyplot as plt


a = b = 50


pA = 0.5


N = 1000


results = {}


for n in range(2, 101, 10):
    # słownik do przechowywania wyników dla danej liczby rozgrywek
    results[n] = {}

    # pętla po liczbie symulacji
    for i in range(N):
        # zerowanie kapitału graczy
        a = b = 50

        # pętla po liczbie rozgrywek
        for j in range(n):
            # losowanie wyniku rozgrywki
            result = random.random()

            # jeśli wynik jest mniejszy niż prawdopodobieństwo wygranej gracza A
            if result < pA:
                # gracz A wygrywa i otrzymuje jednostkę kapitału od gracza B
                a += 1
                b -= 1
            else:
                # gracz B wygrywa i otrzymuje jednostkę kapitału od gracza A
                a -= 1
                b += 1

        # zapisanie wyniku symulacji w słowniku
        results[n][i] = a



for n, result in results.items():
# wyznaczenie wartości i częstości występowania dla danej liczby rozgrywek
    values, frequencies = zip(*result.items())

    # rysowanie histogramu
    plt.hist(values, bins=10, density=True, alpha=0.5, label=f"n={n}")

    plt.xlabel("Kapitał gracza A")
    plt.ylabel("Prawdopodobieństwo")
    plt.legend()
    plt.show()