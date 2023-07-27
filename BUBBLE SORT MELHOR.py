#aleatorio 10 variaveis
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [random.randint(1, 10) for i in range(10)]

random.shuffle(arr)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------
#aleatorio 1000 variaveis
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [random.randint(1, 1000) for i in range(1000)]

random.shuffle(arr)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------
#aleatorio 30000 variaveis
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [random.randint(1, 30000) for i in range(30000)]

random.shuffle(arr)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------
#aleatorio 50000 variaveis
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [random.randint(1, 50000) for i in range(50000)]

random.shuffle(arr)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------
#aleatorio 100000 variaveis
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [random.randint(1, 100000) for i in range(100000)]

random.shuffle(arr)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#-------------------------------------------------------------------------------
# Decrescente com 10 elementos
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [i for i in range(10, -1, -1)]

# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------
# Decrescente com 1000 elementos
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [i for i in range(1000, -1, -1)]

# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------
# Decrescente com 30000 elementos
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
arr = [i for i in range(30000, -1, -1)]


# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------
# Decrescente com 50000 elementos
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [i for i in range(50000, -1, -1)]

# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")

#------------------------------------------------------------------
# Decrescente com 100000 elementos
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [i for i in range(100000, -1, -1)]

# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------------------------
#Crecente 10 variaveis
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [i for i in range(11)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")

#----------------------------------------------------------------------------------------------------------------------------
#Crecente 1000 variaveis
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [i for i in range(1001)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")

#----------------------------------------------------------------------------------------------------------------------------

#Crecente 30000 variaveis
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [i for i in range(30001)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")

#----------------------------------------------------------------------------------------------------------------------------
#Crecente 50000 variaveis
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [i for i in range(50001)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")

#----------------------------------------------------------------------------------------------------------------------------

#Crecente 100000 variaveis
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [i for i in range(100001)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Bubble Sort com verão para vetor já ordenado
bubble_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")















