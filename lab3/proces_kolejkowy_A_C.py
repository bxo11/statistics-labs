import copy
import math
import random

from matplotlib import pyplot as plt

# must be float number
lambdaA = 2.
lambdaD = 2.5

tasks = 100
arrival = []
done = []
waiting = []

for i in range(tasks):
    n = random.random()  # TODO: rozne czy te same n? - raczej to samo
    tiA = -math.log(n) / lambdaA
    # n = random.random()
    tiD = -math.log(n) / lambdaD
    A = (0 if i == 0 else arrival[i - 1]) + tiA
    D = (tiA + tiD if i == 0 else max(done[i - 1], A) + tiD)
    arrival.append(A)
    done.append(D)
    waiting.append(D - A)

# plt.plot(arrival, [x for x in range(tasks)], marker='o')
# plt.plot(done, [x for x in range(tasks)], marker='x')
# plt.xlabel('czas')
# plt.ylabel('numer zadania')
# plt.show()

queue = 0

queue_history1 = []
queue_history_time1 = []
queue_history2 = []
queue_history_time2 = []
task_done = 0
task_done_history = []
task_done_history_time = []
arrival_copy = copy.deepcopy(arrival)
done_copy = copy.deepcopy(done)
a = arrival.pop(0)
d = done.pop(0)
arrival.append(arrival[-1]) # duplicate last element no to lose it in the next loop
done.append(done[-1]) # duplicate last element no to lose it in the next loop
while len(arrival) > 0 or len(done) > 0:
    if a <= d and len(arrival) > 0 :
        if len(arrival) > 0:
            queue += 1
            queue_history_time1.append(a)
            queue_history1.append(queue)
            task_done_history_time.append(a)
            a = arrival.pop(0)
    else:
        if queue > 0:
            queue -= 1
            task_done+=1
            queue_history_time2.append(d)
            queue_history2.append(queue)
            task_done_history_time.append(d)
            d = done.pop(0)
    task_done_history.append(task_done)

plt.plot(queue_history_time1, queue_history1, linestyle='None', marker='o')
plt.plot(queue_history_time2, queue_history2, linestyle='None', marker='o')
plt.title(f'lambdaA = {lambdaA}, lambdaD = {lambdaD}')
plt.xlabel('t')
plt.ylabel('ilosc zadan w kolejce')
plt.show()

plt.plot(arrival_copy, waiting, marker='o')
plt.title(f'lambdaA = {lambdaA}, lambdaD = {lambdaD}')
plt.xlabel('czas wplyniecia zadania')
plt.ylabel('Czas oczekiwania na wykonanie')
plt.show()

plt.plot(task_done_history_time, task_done_history, marker='o')
plt.title(f'lambdaA = {lambdaA}, lambdaD = {lambdaD}')
plt.xlabel('t')
plt.ylabel('Liczba wykonanych zadan')
plt.show()

x_axis = arrival_copy
# x_axis = done_copy
y_axis = [(lambdaA-lambdaD)*x for x in x_axis]
plt.plot(x_axis, y_axis, marker='o')
plt.title(f'lambdaA = {lambdaA}, lambdaD = {lambdaD}')
plt.xlabel('t')
plt.ylabel('(lambdaA-lambdaD)*x')
plt.show()

# ksztalt krzywej przypomina wykres czasu oczekiwania na wykonanie
y_axis2 = [(lambdaA-lambdaD)/lambdaD*x for x in x_axis]
plt.plot(x_axis, y_axis2, marker='o')
plt.title(f'lambdaA = {lambdaA}, lambdaD = {lambdaD}')
plt.xlabel('t')
plt.ylabel('(lambdaA-lambdaD)/lambdaD*x')
plt.show()