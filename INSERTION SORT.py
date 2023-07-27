#Aleatorio 10 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Gerando 1000 números aleatórios
arr = [random.randint(1, 10) for i in range(10)]

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------
#Aleatorio 1000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Gerando 1000 números aleatórios
arr = [random.randint(1, 1000) for i in range(1000)]

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------
#Aleatorio 30000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Gerando 1000 números aleatórios
arr = [random.randint(1, 30000) for i in range(30000)]

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------
#Aleatorio 50000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Gerando 1000 números aleatórios
arr = [random.randint(1, 50000) for i in range(50000)]

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------
#Aleatorio 100000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Gerando 1000 números aleatórios
arr = [random.randint(1, 100000) for i in range(100000)]

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------
#Decrecente 10 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [i for i in range(10, -1, -1)]

# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------
#Decrecente 1000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [i for i in range(1000, -1, -1)]

# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------
#Decrecente 30000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [i for i in range(30000, -1, -1)]

# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------
#Decrecente 50000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [i for i in range(50000, -1, -1)]

# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------
#Decrecente 100000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [i for i in range(100000, -1, -1)]

# Ordenando em ordem decrescente
arr.sort(reverse=True)

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#--------------------------------------------------------------------------------------------------------
#crecente 10 variaveis
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [i for i in range(11)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------------------------------------
#crecente 1000 variaveis
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [i for i in range(1001)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------------------------------------
#crecente 30000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [i for i in range(30001)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------------------------------------
#crecente 50000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [i for i in range(50001)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------------------------------------
#crecente 100000 variaveis
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [i for i in range(100001)]

# Ordenando em ordem crescente
arr.sort()

# Imprimindo os números aleatórios gerados
print("Antes da ordenação:")
print(arr)

# Medindo o tempo de execução
start_time = time.time()

# Ordenando usando Insertion Sort
insertion_sort(arr)

# Medindo o tempo após a ordenação
end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------------------------------------