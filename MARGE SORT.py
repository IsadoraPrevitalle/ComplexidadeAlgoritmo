#MARGE SORT

#ALEATORIA COM 10 ELEMENTOS

import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# Gerar lista aleatória de 1000 elementos
my_list = [random.randint(0, 10) for i in range(10)]

# Medir o tempo de execução do algoritmo
start_time = time.time()

# Ordenar a lista usando merge_sort
sorted_list = merge_sort(my_list)

# Calcular o tempo de execução
elapsed_time = time.time() - start_time

# Imprimir a lista ordenada e o tempo de execução
print("Lista ordenada:", sorted_list)
print("Tempo de execução:", elapsed_time, "segundos")


 
#ALEATORIAS COM 1000 ELEMENTOS

import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# Gerar lista aleatória de 1000 elementos
my_list = [random.randint(0, 1000) for i in range(1000)]

# Medir o tempo de execução do algoritmo
start_time = time.time()

# Ordenar a lista usando merge_sort
sorted_list = merge_sort(my_list)

# Calcular o tempo de execução
elapsed_time = time.time() - start_time

# Imprimir a lista ordenada e o tempo de execução
print("Lista ordenada:", sorted_list)
print("Tempo de execução:", elapsed_time, "segundos")


#ALEATORIA DE 30000 ELEMENTOS

import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# Gerar lista aleatória de 1000 elementos
my_list = [random.randint(0, 30000) for i in range(30000)]

# Medir o tempo de execução do algoritmo
start_time = time.time()

# Ordenar a lista usando merge_sort
sorted_list = merge_sort(my_list)

# Calcular o tempo de execução
elapsed_time = time.time() - start_time

# Imprimir a lista ordenada e o tempo de execução
print("Lista ordenada:", sorted_list)
print("Tempo de execução:", elapsed_time, "segundos")


#ALEATORIA DE 50000 ELEMENTOS

import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# Gerar lista aleatória de 1000 elementos
my_list = [random.randint(0, 50000) for i in range(50000)]

# Medir o tempo de execução do algoritmo
start_time = time.time()

# Ordenar a lista usando merge_sort
sorted_list = merge_sort(my_list)

# Calcular o tempo de execução
elapsed_time = time.time() - start_time

# Imprimir a lista ordenada e o tempo de execução
print("Lista ordenada:", sorted_list)
print("Tempo de execução:", elapsed_time, "segundos")


#ALEATORIA DE 100000 ELEMENTOS

import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# Gerar lista aleatória de 1000 elementos
my_list = [random.randint(0, 100000) for i in range(100000)]

# Medir o tempo de execução do algoritmo
start_time = time.time()

# Ordenar a lista usando merge_sort
sorted_list = merge_sort(my_list)

# Calcular o tempo de execução
elapsed_time = time.time() - start_time

# Imprimir a lista ordenada e o tempo de execução
print("Lista ordenada:", sorted_list)
print("Tempo de execução:", elapsed_time, "segundos")


#Decrescente COM 10 ELEMENTOS

import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(10, 0, -1)) # lista de 1000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


 
#DECRESCENTE COM 1000 ELEMENTOS

import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(1000, 0, -1)) # lista de 1000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


#DECRESCENTE DE 30000 ELEMENTOS

import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(30000, 0, -1)) # lista de 1000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

#DECRESCENTE DE 50000 ELEMENTOS

import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(50000, 0, -1)) # lista de 1000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

#DECRESCENTE DE 100000 ELEMENTOS

import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(100000, 0, -1)) # lista de 1000 elementos em ordem decrescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

#CRESCENTE COM 10 ELEMENTOS

import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(1, 11)) # lista de 10 elementos em ordem crescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


 
#CRESCENTE COM 1000 ELEMENTOS

import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(1, 1001)) # lista de 1000 elementos em ordem crescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


#CRESCENTE DE 30000 ELEMENTOS
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(1, 30001)) # lista de 30000 elementos em ordem crescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)


#CRESCENTE DE 50000 ELEMENTOS

import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(1, 50001)) # lista de 50000 elementos em ordem crescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)



#CRESCENTE DE 100000 ELEMENTOS

import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
    
arr = list(range(1, 100001)) # lista de 100000 elementos em ordem crescente
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
print(sorted_arr)

