import math
import random

import numpy as np
from matplotlib import pyplot as plt

from utils import calculate_avg, calculate_sum

lambdaA = 2.
lambdaD = 5.

tasks = 10
arrival = []
done = []
waiting = []

time = tasks / min(lambdaA, lambdaD)
step = time / tasks
for i in range(tasks):
    n = random.random()  # TODO: rozne czy te same n?
    tiA = -math.log(n) / lambdaA
    # n = random.random()
    tiD = -math.log(n) / lambdaD
    A = (0 if i == 0 else arrival[i - 1]) + tiA
    D = (tiA + tiD if i == 0 else max(done[i - 1], A) + tiD)
    arrival.append(A)
    done.append(D)
    waiting.append(D - A)

queue = 0

queue_history = []
task_done = 0
task_done_history = []
a = arrival.pop(0)
d = done.pop(0)
waiting_queue = []
one =0
two =0
time_queue = 0
while len(arrival) > 0 or len(done) > 0:
    if a < d and len(arrival) > 0:
        if len(arrival) > 0:
            time_queue += waiting[one]
            one +=1
            queue += 1
            a = arrival.pop(0)
    else:
        if queue > 0:
            time_queue -= waiting[two]
            two+=1
            queue -= 1
            task_done += 1
            d = done.pop(0)
    waiting_queue.append(time_queue)
    queue_history.append(queue)
    task_done_history.append(task_done)

plt.plot(np.linspace(0, time, num=len(queue_history)), queue_history, marker='o')
plt.xlabel('')
plt.ylabel('ilosc zadan w kolejce')
plt.show()

plt.plot(np.linspace(0, time, num=len(waiting)), waiting, marker='o')
plt.xlabel('')
plt.ylabel('Czas oczekiwania na wykonanie')
plt.show()

plt.plot(np.linspace(0, time, num=len(task_done_history)), task_done_history, marker='o')
plt.xlabel('')
plt.ylabel('Liczba wykonanych zadan')
plt.show()


def calculate_avg_queue(sequence1, sequence2):
    suma = 0
    for i in range(len(sequence1)):
        suma += sequence1[i]*sequence2[i]
    return suma / calculate_sum(sequence1)


avg_waiting = calculate_avg(waiting)
# avg_queue = calculate_avg(queue_history)
avg_queue = calculate_avg_queue(waiting_queue,queue_history)
print(f'Sredni czas spedzony przez zadanie w systemie: {avg_waiting}')
print(f'Sredni ilosc zadan w kolejce: {avg_queue}')
print(f'Prawo Little: {avg_waiting * lambdaA} = {avg_queue}')
