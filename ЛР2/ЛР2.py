#Мультисписок(вложенный список)

multilist = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

#Очередь

from queue import Queue
q = Queue()
q.put(1)
q.put(2)
q.put(3)

#Дек

from collections import deque
tasks = deque()
tasks.append("task1")
tasks.append("task2")
tasks.append("task3")

#Приоритетная очередь с помощью PriorityQueue 

from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'mid-priority item'))
q.put((1, 'high-priority item'))

#Приоритетная очередь с помощью heapq

import heapq
customers =
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
