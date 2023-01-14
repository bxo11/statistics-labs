import copy
import math
import random

import numpy as np
from matplotlib import pyplot as plt

from utils import calculate_avg, calculate_sum

# must be float number
lambdaA = 2.
lambdaD = 5.

tasks = 1000
arrival = []
done = []
waiting = []

for i in range(tasks):
    n = random.random()
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
waiting_queue1 = []
waiting_queue2 = []
one =0
two =0
time_queue = 0
waiting_queue = []
queue_history = []
while len(arrival) > 0 or len(done) > 0:
    if a <= d and len(arrival) > 0 :
        if len(arrival) > 0:
            time_queue += waiting[one]
            one += 1
            queue += 1
            queue_history_time1.append(a)
            queue_history1.append(queue)
            task_done_history_time.append(a)
            a = arrival.pop(0)
    else:
        if queue > 0:
            time_queue -= waiting[two]
            two += 1
            queue -= 1
            task_done+=1
            queue_history_time2.append(d)
            queue_history2.append(queue)
            task_done_history_time.append(d)
            d = done.pop(0)
    waiting_queue.append(time_queue)
    queue_history.append(queue)
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

# plt.plot(task_done_history_time, task_done_history, marker='o')
# plt.xlabel('')
# plt.ylabel('Liczba wykonanych zadan')
# plt.show()

def calculate_avg_queue(sequence1, sequence2):
    suma = 0
    for i in range(len(sequence1)):
        suma += sequence1[i]*sequence2[i]
    sum = calculate_sum(sequence1)
    return suma / sum


avg_waiting = calculate_avg(waiting)
# avg_queue = (calculate_avg(queue_history1) + calculate_avg(queue_history2))/2
# waiting_queue1.extend(waiting_queue2)
# queue_history1.extend(queue_history2)
avg_queue = calculate_avg_queue(arrival_copy,waiting)
# avg_queue += calculate_avg_queue(done_copy,waiting)
print(f'Sredni czas spedzony przez zadanie w systemie: {avg_waiting}')
print(f'Sredni ilosc zadan w kolejce: {avg_queue}')
print(f'Prawo Little: {avg_waiting} = {avg_queue}')