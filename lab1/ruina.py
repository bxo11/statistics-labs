import random

from matplotlib import pyplot as plt

from utils import calculate_avg


def trial(prob=0.5):
    if random.random() <= prob:
        return True
    return False


def ruin(a=100, b=100, prob_a=0.5, N=1, save_balance=False):
    results = {'winsA': 0, 'winsB': 0, 'pA': prob_a, 'N': N, 'iterations': []}
    if save_balance:
        results['balance_A'] = [[] for _ in range(N)]
        results['balance_B'] = [[] for _ in range(N)]
    for n in range(N):
        A = a
        B = b
        iter = 0
        while A > 0 and B > 0:
            iter += 1
            if trial(prob_a):
                A += 1
                B -= 1
            else:
                A -= 1
                B += 1
            if save_balance:
                results['balance_A'][n].append(A)
                results['balance_B'][n].append(B)
        if A == 0:
            results['winsB'] = results['winsB'] + 1
        elif B == 0:
            results['winsA'] = results['winsA'] + 1
        results['iterations'].append(iter)
        results['pWinA'] = results['winsA'] / N
        results['pWinB'] = results['winsB'] / N
    return results


def ruin_prob(data, N, player='A'):
    return data[player] / N


def B():
    x = []
    y = []
    y2 = []
    prob_a = 0.25
    a = 10
    b = 10
    for i in range(50):
        prob_tmp = prob_a + i / 100
        r = ruin(a=a, b=b, prob_a=prob_tmp, N=1000)
        y.append(r['pWinB'])
        x.append(prob_tmp)
        l = ((1 - prob_tmp) / prob_tmp) ** a - ((1 - prob_tmp) / prob_tmp) ** (a + b)
        m = 1 - ((1 - prob_tmp) / prob_tmp) ** (a + b)
        if prob_tmp == 0.5:
            y2.append(1 - a / (a + b))
        else:
            y2.append(l / m)

    plt.plot(x, y, marker='o')
    plt.xlabel('prawdopodobieństwo wygranej w jednej rozgrywce pA')
    plt.ylabel('prawdopodobieństwa ruiny gracza A')

    plt.plot(x, y2, marker='x')

    plt.show()


def C():
    x = []
    y = []
    y2 = []
    start_a = 10
    for i in range(80):
        a_temp = start_a + i
        r = ruin(a=a_temp, b=100 - a_temp, prob_a=0.5, N=1000)
        y.append(r['pWinB'])
        plt.xlabel('poczatkowy kapital a')
        plt.ylabel('prawdopodobieństwa ruiny gracza A')
        x.append(a_temp)

        l = ((1 - 0.5) / 0.5) ** a_temp - ((1 - 0.5) / 0.5) ** (a_temp + (100 - a_temp))
        m = 1 - ((1 - 0.5) / 0.5) ** (a_temp + (100 - a_temp))
        if 0.5 == 0.5:
            y2.append(1 - a_temp / (a_temp + (100 - a_temp)))
        else:
            y2.append(l / m)

    plt.plot(x, y, marker='o')
    plt.plot(x, y2, marker='x')
    plt.show()


def D():
    x = []
    prop = [0.2, 0.5, 0.8]
    for p in prop:
        r = ruin(a=50, b=50, prob_a=p, N=20000)
        x.extend(r['iterations'])
        print(f"Srednia dlugosc rozgrywki dla p: {p} - {calculate_avg(r['iterations'])}")

    plt.hist(x, density=True, bins=50)
    plt.show()


def E():
    x = []
    y = []
    prob_a = 0.25
    for i in range(50):
        prob_tmp = prob_a + i / 100
        r = ruin(a=10, b=10, prob_a=prob_tmp, N=1000)
        y.append(max(r['iterations']))
        x.append(prob_tmp)

    plt.plot(x, y, marker='o')
    plt.ylabel('maksymalna dlugosc rozgrywek')
    plt.xlabel('prawdopodobieństwa ruiny gracza A')
    plt.show()


# niegotowe
def F():
    x = []
    prop = [0.2, 0.5, 0.8]
    n_list = [2, 10, 20, 50, 100]
    for p in prop:
        for n in n_list:
            r = ruin(a=50, b=50, prob_a=p, N=10000)
            x.extend(r['iterations'])

    plt.hist(x, density=True, bins=50)
    plt.show()


def F2():
    # Set the number of simulations to run and the number of games per simulation
    N = 2
    n = 10

    # Set the starting balances and probability of player A winning a point
    a = b = 50
    pA = 0.5

    # Run the simulations and store the results
    results = ruin(a=a, b=b, prob_a=pA, N=N, save_balance=True)

    # Extract the final balance of player A from each simulation
    final_balances = [results['balance_A'][i][-1] for i in range(N)]

    # Use Matplotlib to create a histogram of the final balances
    import matplotlib.pyplot as plt
    plt.hist(final_balances, bins=range(0, a + b + 1))
    plt.xlabel('Final balance of player A')
    plt.ylabel('Probability')
    plt.show()


def G():
    x = []
    y = []
    r = ruin(a=50, b=50, prob_a=0.2, N=1, save_balance=True)
    y.extend(r['balance_A'][0])
    x.extend([i for i in range(len(y))])

    plt.plot(x, y, marker='o')
    plt.xlabel('balans gracza A')
    plt.ylabel('prawdopodobieństwa ruiny gracza A')
    plt.show()

    #################
    x = []
    y = []
    wins = 0
    for i in range(10):
        r = ruin(a=50, b=50, prob_a=0.5, N=1, save_balance=True)
        wins += r['winsA']
        y.append(wins)
        x.append(i)

    plt.plot(x, y, marker='o')
    plt.xlabel('numer rozgrywki')
    plt.ylabel('ilosc wygranych gracza A')
    plt.show()


C()
