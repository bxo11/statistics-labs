import copy
import math
import random

from matplotlib import pyplot as plt

from lab3.proces_kolejkowy_B2 import calculate_avg_queue
from utils import calculate_avg

# must be float number
lambdaA = 2.
lambdaD = 2.5
avg_task_amount_in_queue = []
avg_waiting_time_in_queue = []

for repeats in range(100):
    lambdaA += repeats/100
    # lambdaD += repeats/100
    # r= lambdaA/lambdaD

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
    one = 0
    two = 0
    time_queue = 0
    waiting_queue = []
    queue_history = []
    while len(arrival) > 0 or len(done) > 0:
        if a <= d and len(arrival) > 0:
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
                task_done += 1
                queue_history_time2.append(d)
                queue_history2.append(queue)
                task_done_history_time.append(d)
                d = done.pop(0)
        waiting_queue.append(time_queue)
        queue_history.append(queue)
        task_done_history.append(task_done)

    avg_queue = calculate_avg_queue(arrival_copy, waiting)
    avg_task_amount_in_queue.append(avg_queue)

    avg_waiting_time_in_queue.append(calculate_avg(waiting))

plt.plot([x for x in range(len(avg_task_amount_in_queue))], avg_task_amount_in_queue, marker='o')
plt.title(f'')
plt.xlabel(f'')
plt.ylabel(f'')
plt.show()

plt.plot([x for x in range(len(avg_waiting_time_in_queue))], avg_waiting_time_in_queue, marker='o')
plt.title(f'')
plt.xlabel(f'')
plt.ylabel(f'')
plt.show()
