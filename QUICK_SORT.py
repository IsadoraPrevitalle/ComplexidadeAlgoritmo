# Aleatório com 10 elementos
Lista = random.sample(range(11), 10)
inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(Lista)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

---------------------------------------------------------------------------

# Aleatório com 1000 elementos
Lista = random.sample(range(1001), 1000)
inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(Lista)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

---------------------------------------------------------------------------

# Aleatório com 30000 elementos
Lista = random.sample(range(30001), 30000)
inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(Lista)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

---------------------------------------------------------------------------

# Aleatório com 100000 elementos
Lista = random.sample(range(100001), 100000)
inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(Lista)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

----------------------------------------------------------------------------------------------------------------------------------------------------


# Decrescente com 10 elementos

import time
ListaDecrescente = [i for i in range(10, -1, -1)]
teste = [ListaDecrescente]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

---------------------------------------------------------------------------

# Decrescente com 1000 elementos

import time
ListaDecrescente = [i for i in range(1000, -1, -1)]
teste = [ListaDecrescente]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

---------------------------------------------------------------------------

# Decrescente com 30000 elementos

import time
ListaDecrescente = [i for i in range(30000, -1, -1)]
teste = [ListaDecrescente]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

---------------------------------------------------------------------------

# Decrescente com 50000 elementos

import time
ListaDecrescente = [i for i in range(50000, -1, -1)]
teste = [ListaDecrescente]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

---------------------------------------------------------------------------

# Decrescente com 100000 elementos

import time
ListaDecrescente = [i for i in range(30000, -1, -1)]
teste = [ListaDecrescente]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

----------------------------------------------------------------------------------------------------------------------------------------------------

# Crescente com 10 elementos

import time
ListaOrdenada = [i for i in range(11)]
teste = [ListaOrdenada]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

---------------------------------------------------------------------------

# Crescente com 1000 elementos

import time
ListaOrdenada = [i for i in range(1001)]
teste = [ListaOrdenada]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

---------------------------------------------------------------------------

# Crescente com 30000 elementos
import time
import sys
sys.setrecursionlimit(1000000) #Aumenta a quantidade de recursões

ListaOrdenada = [i for i in range(30001)]
teste = [ListaOrdenada]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

---------------------------------------------------------------------------

# Crescente com 50000 elementos

import time
ListaOrdenada = [i for i in range(50001)]
teste = [ListaOrdenada]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

---------------------------------------------------------------------------

# Crescente com 100000 elementos

import time
ListaOrdenada = [i for i in range(100001)]
teste = [ListaOrdenada]

inicio = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_list = quick_sort(teste)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.4f}".format(fim-inicio))

---------------------------------------------------------------------------



