import copy
import random

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
    e = 10 ** (-5)

    for n in range(3):
        for m in range(3):
            P = [[0.64, 0.32, 0.04], [0.4, 0.5, 0.1], [0.25, 0.50, 0.25]]
            P_prev = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
            x = []
            y = []
            while (abs(matrix_max(P) - matrix_max(P_prev)) > e):
                y.append(P[n][m])
                P_prev = P
                P = matrix_multi(P)
            x.extend([i for i in range(len(y))])

            plt.plot(x, y, marker='o')
            plt.title(f'P[{n}][{m}]')
            plt.xlabel('N')
            plt.ylabel(f'roznica wartosci elementu macierzy')

            for pi in P[0]:
                y = [pi for i in range(len(y))]
                plt.plot(x, y, marker='x')

            plt.show()


def B():
    P = [[0.64, 0.32, 0.04], [0.4, 0.5, 0.1], [0.25, 0.50, 0.25]]
    N = 10 ** 4
    values = [0, 1, 2]

    P_new = []
    for node in values:
        visits = [0, 0, 0]
        for i in range(N):
            choice = node
            weights = P[choice]
            choice = random.choices(values, weights)[0]
            visits[choice] += 1
        # print(f'start: {node} = {visits[0] / N} {visits[1] / N} {visits[2] / N}')
        P_new.append([x / N for x in visits])

    for i in range(4):
        P_new = matrix_multi(P_new)
        P = matrix_multi(P)

    print('P')
    for i in range(3):
        print(f'{P[i][0]} {P[i][1]} {P[i][2]}')

    print('\nP_new')
    for i in range(3):
        print(f'{P_new[i][0]} {P_new[i][1]} {P_new[i][2]}')

    print('\nporownanie wartosci pi:')
    for i in range(3):
        print(f'{P_new[i][0]-P[i][0]} {P_new[i][1]-P[i][1]} {P_new[i][1]-P[i][2]}')


def CD():
    users = 100
    # start_logged_in_users = random.randint(0, users)
    start_logged_in_users = 0

    login_probability = 0.2

    logout_probability = 0.5
    # logout_probability = 1 - (0.008 * start_logged_in_users + 0.1)

    N = 10 ** 4

    visits = [0 for _ in range(users)]

    logged_in_users = start_logged_in_users
    for n in range(N):
        temp_logged = logged_in_users
        for user in range(users - temp_logged):
            if random.random() < login_probability:
                logged_in_users += 1

        for user in range(temp_logged):
            if random.random() < logout_probability:
                logged_in_users -= 1

        visits[logged_in_users] += 1

    top_five = []
    temp_values = copy.deepcopy(visits)
    for i in range(5):
        maximum = max(temp_values)
        top_five.append(maximum)
        temp_values.remove(maximum)
    plt.plot([i for i in range(5)], [x / N for x in top_five], marker='o')
    plt.title(f'Wykres zbieznosci dla 5 najwiekszych wartosci, start logged users: {start_logged_in_users}')
    plt.xlabel('')
    plt.ylabel('')

    plt.show()

    plt.plot([i for i in range(users)], [x / N for x in visits], marker='o')
    plt.title(f'Wykres koncowych wartosci dla wszystkich pi, start logged users: {start_logged_in_users}')
    plt.xlabel('N')
    plt.ylabel('')

    plt.show()


# A()
# B()
CD()
