# Aleatório com 10 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [random.randint(1, 10) for i in range(10)]

print("Antes da ordenação:")
print(arr)

start_time = time.time()


bubble_sort(arr)


end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------------------------------------------

# Aleatório com 1000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [random.randint(1, 1000) for i in range(1000)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#----------------------------------------------------------------------------------------
# Aleatório com 30000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [random.randint(1, 30000) for i in range(30000)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------

# Aleatório com 50000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [random.randint(1, 50000) for i in range(50000)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------

#Aleatório com 100000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [random.randint(1, 100000) for i in range(100000)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#-------------------------------------------------------------------------------------------------------------
# Decrescente com 10 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [i for i in range(10, -1, -1)]

print("Antes da ordenação:")
print(arr)

start_time = time.time()


bubble_sort(arr)


end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------------------------------------------

# Decrescente com 1000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


ararr = [i for i in range(1000, -1, -1)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#----------------------------------------------------------------------------------------
# Decrescente com 30000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [i for i in range(30000, -1, -1)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------

# Decrescente com 50000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [i for i in range(50000, -1, -1)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------

# Decrescente com 100000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [i for i in range(100000, -1, -1)]
print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#-------------------------------------------------------------------------------------------------------------
# Crescente com 10 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [i for i in range(11)]

print("Antes da ordenação:")
print(arr)

start_time = time.time()


bubble_sort(arr)


end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#------------------------------------------------------------------------------------------------------

# Crescente com 1000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [i for i in range(1001)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#----------------------------------------------------------------------------------------
# Crescente com 30000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [i for i in range(30001)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------

# Crescente com 50000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [i for i in range(50001)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#---------------------------------------------------------------------------

# Crescente com 100000 elementos
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [i for i in range(100001)]

print("Antes da ordenação:")
print(arr)
start_time = time.time()
bubble_sort(arr)

end_time = time.time()

# Imprimindo os números ordenados
print("Depois da ordenação:")
print(arr)

# Imprimindo o tempo de execução
print("Tempo de execução:", end_time - start_time, "segundos")
#-------------------------------------------------------------------------------------------------------------
