HeapSort
______________________________
#ALEATORIA COM 10 ELEMENTOS
import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
import random

arr = [random.randint(1, 10) for i in range(10)] # lista de 10 elementos aleatórios
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


______________________________
#ALEATORIAS COM 1000 ELEMENTOS

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
import random

arr = [random.randint(1, 1000) for i in range(1000)] # lista de 1000 elementos aleatórios
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

__________________________________________
#ALEATORIA DE 30000
import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
import random

arr = [random.randint(1, 30000) for i in range(30000)] # lista de 30000 elementos aleatórios
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

___________________________________________
#ALEATORIA DE 50000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
import random

arr = [random.randint(1, 50000) for i in range(50000)] # lista de 50000 elementos aleatórios
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

______________________________________
#ALEATORIA DE 100000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
import random

arr = [random.randint(1, 100000) for i in range(100000)] # lista de 100000 elementos aleatórios
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

_______________________________________________________
#DECRESCENTE DE 10

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(10, 0, -1)) # lista de 10 elementos em ordem decrescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

_______________________________________________________
#DECRESCENTE DE 1000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(1000, 0, -1)) # lista de 1000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

_______________________________________________________
#DECRESCENTE DE 30000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(30000, 0, -1)) # lista de 30000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


_______________________________________________________
#DECRESCENTE DE 50000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(50000, 0, -1)) # lista de 50000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


_______________________________________________________
#DECRESCENTE DE 100000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(100000, 0, -1)) # lista de 100000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


________________________________________________________
________________________________________________________
________________________________________________________
#CRESCENTE DE 10

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(1, 11)) # lista de 10 elementos em ordem crescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


_______________________________________________________
#CRESCENTE DE 1000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(1, 1001)) # lista de 1000 elementos em ordem crescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

_______________________________________________________
#CRESCENTE DE 30000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(1, 30001)) # lista de 30000 elementos em ordem crescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


_______________________________________________________
#CRESCENTE DE 50000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(1, 50001)) # lista de 50000 elementos em ordem crescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

_______________________________________________________
#CRESCENTE DE 100000

import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
    
arr = list(range(1, 100001)) # lista de 100000 elementos em ordem crescente
start_time = time.time()
sorted_arr = heap_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)









