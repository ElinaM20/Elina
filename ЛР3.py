#Бинарная куча с использованием heapq

import heapq
someNumbers = [8, 3, 5, 1, 6, 2, 4, 7] # создание списка с исходными данными для кучи
heapq.heapify(someNumbers) # превращение списка в кучу
heapq.heappush(someNumbers, 0) # добавление нового элемента в кучу
someValue = heapq.heappop(someNumbers) # извлечение минимального элемента из кучи

#Бинарная/биноминальная куча в виде собственного класса

class BinaryHeap
def __init__(self):
 self.heap = [3](https://tr-page.yandex.ru/translate?lang=enru&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fdsa%2Fbinary-heap-in-python%2F)
def insert(self, key):
 self.heap.append(key)
 self._heapify_up(len(self.heap) - 1)
def delete_min(self):
 self.heap.pop()
 self._heapify_down(0)
def get_min(self):
 if self.is_empty():
 return None
 return self.heap
def is_empty(self):
 return len(self.heap) == 0

#Алгоритм для печати ряда Фибоначчи до заданного количества элементов

def fibonacci_for_loop(n):
a, b = 0, 1
for _ in range(n):
print(a, end=' ')
a, b = b, a + b

#Алгоритм для рекурсивного вычисления n-го числа ряда Фибоначчи

def fibonacci(n):
if n in (1, 2):
return 1
return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))

#Хеш-таблица как класс

lass HashTable:
 def __init__(self, size):
 self.size = size
 self.table = [None]*size
 def _hash(self, key):
 return ord(key[0]) % self.size
class HashTable:
 def __init__(self, size):
 self.size = size
 self.table = [None]*size
 def _hash(self, key):
 return ord(key[0]) % self.size
 def set(self, key, value):
 hash_index = self._hash(key)
 self.table[hash_index] = (key, value)
 def get(self, key):
 hash_index = self._hash(key)
 if self.table[hash_index] is not None:
 return self.table[hash_index][1]
 raise KeyError(f'Key {key} not found')
 def remove(self, key):
 hash_index = self._hash(key)
 if self.table[hash_index] is not None:
 self.table[hash_index] = None
 else:
 raise KeyError(f'Key {key} not found')

#Хеш-таблица с собственной реализацией

def hash_function(key):
 hash_code = 0
 for char in key:
 hash_code += ord(char)
 return hash_code % array_size
class HashTable:
 def __init__(self, size):
 self.array_size = size
 self.array = [None] * size
 def put(self, key, value):
 # Insert key-value pair
 def get(self, key):
 # Retrieve value by key
 def remove(self, key):
 # Remove key-value pair
 def hash_function(self, key):
 # Generate hash code
def put(self, key, value):
 index = self.hash_function(key)
 if self.array[index] is None:
 self.array[index] = HashTableEntry(key, value)
 else:
 entry = self.array[index]
 entry.value = value
 entry.key = key
class HashTableEntry:
 def __init__(self, key, value):
 self.key = key
 self.value = value
def get(self, key):
 index = self.hash_function(key)
 if self.array[index] is None:
 raise KeyError()
 entry = self.array[index]
 if entry.key == key:
 return entry.value
5
 raise KeyError()
def remove(self, key):
 index = self.hash_function(key)
 if self.array[index] is None:
 raise KeyError()
 entry = self.array[index]
 if entry.key == key:
 self.array[index] = None
 else:
 raise KeyError()
def put(self, key, value):
 index = self.hash_function(key)
 if self.array[index] is None:
 self.array[index] = LinkedList()
 self.array[index].append(HashTableEntry(key, value))
def put(self, key, value):
 index = self.hash_function(key)
 while self.array[index] is not None:
 index = (index + 1) % array_size
 self.array[index] = HashTableEntry(key, value)
def put(self, key, value):
 index = self.hash_function_1(key)
 increment = self.hash_function_2(key)
 while self.array[index] is not None:
 index = (index + increment) % array_size
 self.array[index] = HashTableEntry(key, value)
def rehash(self):
 old_array = self.array
 old_capacity = len(old_array)
 new_capacity = 2 * old_capacity
 self.array = [None] * new_capacity
 for entry in old_array:
 if entry is not None:
 index = self.hash_function(entry.key)
 self.array[index] = entry
