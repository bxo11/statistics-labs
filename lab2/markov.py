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
                max=e
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
    plt.ylabel('suma elementow macierzy P')

    plt.show()


def B():
    pass


A()