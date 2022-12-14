import copy
import random
from math import sqrt

from matplotlib import pyplot as plt


def matrix_sum(matrix):
    sum = 0
    for ee in matrix:
        for e in ee:
            sum += e
    return sum


def matrix_max(matrix):
    max = 0
    for ee in matrix:
        for e in ee:
            if e > max:
                max = e
    return max


def matrix_multi(matrix):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(len(matrix)):

        for j in range(len(matrix[0])):

            for k in range(len(matrix)):
                result[i][j] += matrix[i][k] * matrix[k][j]

    return result


def A():
    P = [[0.64, 0.32, 0.04], [0.4, 0.5, 0.1], [0.25, 0.50, 0.25]]
    P_prev = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    e = 10 ** (-5)
    x = []
    y = []
    while (abs(matrix_max(P) - matrix_max(P_prev)) > e):
        y.append(matrix_max(P))
        P_prev = P
        P = matrix_multi(P)
    x.extend([i for i in range(len(y))])

    plt.plot(x, y, marker='o')
    plt.xlabel('N')
    plt.ylabel('roznica sum elementow macierzy P')

    for pi in P[0]:
        y = [pi for i in range(len(y))]
        plt.plot(x, y, marker='x')

    plt.show()


def B():
    P = [[0.64, 0.32, 0.04], [0.4, 0.5, 0.1], [0.25, 0.50, 0.25]]
    N = 10 ** 4
    values = [0, 1, 2]

    for node in values:
        visits = [0, 0, 0]
        for i in range(N):
            choice = node
            weights = P[choice]
            choice = random.choices(values, weights)[0]
            visits[choice] += 1
        print(f'start: {node} = {visits[0] / N} {visits[1] / N} {visits[2] / N}')


def CD():
    users = 100
    start_logged_in_users = random.randint(0, 100)
    login_probability = 0.2
    logout_probability = 0.5
    # logout_probability = 1 - (0.008 * start_logged_in_users + 0.1)
    N = 10 ** 4

    visits = [0 for u in range(users)]

    logged_in_users = start_logged_in_users
    for n in range(N):
        for user in range(users - logged_in_users):
            if random.random() < login_probability:
                logged_in_users += 1

        for user in range(logged_in_users):
            if random.random() < logout_probability:
                logged_in_users -= 1

        visits[logged_in_users] += 1

    top_five = []
    temp_values = copy.deepcopy(visits)
    for i in range(5):
        maximum = max(temp_values)
        top_five.append(maximum)
        temp_values.remove(maximum)
    plt.plot([i for i in range(5)], top_five, marker='o')
    plt.title(f'start: {start_logged_in_users}')
    plt.xlabel('')
    plt.ylabel('')

    plt.show()

    plt.plot([i for i in range(users)], visits, marker='o')
    plt.title(f'start: {start_logged_in_users}')
    plt.xlabel('N')
    plt.ylabel('')

    plt.show()


CD()
