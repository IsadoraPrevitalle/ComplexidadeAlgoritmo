#QUICK SORT
#ALEATORIO COM 10
import random
import sys
sys.setrecursionlimit(1000000) #Aumenta a quantidade de recursões
import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = [random.randint(1, 10) for i in range(10)] # lista de 10 elementos aleatórios
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#ALEATORIO COM 1000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = [random.randint(1, 1000) for i in range(1000)] # lista de 1000 elementos aleatórios
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

#ALEATORIO COM 10000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = [random.randint(1, 10000) for i in range(10000)] # lista de 10000 elementos aleatórios
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#ALEATORIO COM 30000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = [random.randint(1, 30000) for i in range(30000)] # lista de 30000 elementos aleatórios
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#ALEATORIO COM 50000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = [random.randint(1, 50000) for i in range(50000)] # lista de 50000 elementos aleatórios
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#ALEATORIO COM 100000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = [random.randint(1, 100000) for i in range(100000)] # lista de 100000 elementos aleatórios
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

#DECRESCENTE COM 10

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(10, 0, -1)) # lista de 10 elementos em ordem decrescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#DECRESCENTE COM 1000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(1000, 0, -1)) # lista de 1000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#DECRESCENTE COM 10000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(10000, 0, -1)) # lista de 10000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#DECRESCENTE COM 30000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(30000, 0, -1)) # lista de 30000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#DECRESCENTE COM 50000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(50000, 0, -1)) # lista de 50000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#DECRESCENTE COM 100000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(100000, 0, -1)) # lista de 100000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


#CRESCENTE COM 10

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(1, 11)) # lista de 10 elementos em ordem crescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#CRESCENTE COM 1000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(1, 1001)) # lista de 1000 elementos em ordem crescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#CRESCENTE COM 10000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(1, 10001)) # lista de 10000 elementos em ordem crescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#CRESCENTE COM 30000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(1, 30001)) # lista de 30000 elementos em ordem crescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#CRESCENTE COM 50000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(1, 50001)) # lista de 50000 elementos em ordem crescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

 
#CRESCENTE COM 100000

import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr

arr = list(range(1, 100001)) # lista de 100000 elementos em ordem crescente
start_time = time.time()
sorted_arr = quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)
