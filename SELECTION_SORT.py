# Aleatória de 10 elementos
import random
import time

random_list = random.sample(range(11), 10)
inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(random_list)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# Aleatória de 1000 elementos
import random
import time

random_list = random.sample(range(1001), 1000)
inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(random_list)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# Aleatória de 30000 elementos
import random
import time

random_list = random.sample(range(30001), 30000)
inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(random_list)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# Aleatória de 50000 elementos
import random
import time

random_list = random.sample(range(50001), 50000)
inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(random_list)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# Aleatória de 100000 elementos
import random
import time

random_list = random.sample(range(100001), 100000)
inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(random_list)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

----------------------------------------------------------------------------------------------------------------------------------------------------

# Decrescente de 10 elementos
import time

ListaDecrescente = [i for i in range(10, -1, -1)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaDecrescente)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))


----------------------------------------------------------------------------------

# Decrescente de 1000 elementos
import time

ListaDecrescente = [i for i in range(1000, -1, -1)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaDecrescente)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

----------------------------------------------------------------------------------

# Decrescente de 30000 elementos
import time

ListaDecrescente = [i for i in range(30000, -1, -1)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaDecrescente)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

----------------------------------------------------------------------------------

# Decrescente de 50000 elementos
import time

ListaDecrescente = [i for i in range(50000, -1, -1)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaDecrescente)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

----------------------------------------------------------------------------------

# Decrescente de 100000 elementos
import time

ListaDecrescente = [i for i in range(100000, -1, -1)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaDecrescente)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

----------------------------------------------------------------------------------------------------------------------------------------------------

# Ordenada de 10 elementos
ListaOrdenada = [i for i in range(11)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaOrdenada)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-----------------------------------------------------------------------------------

# Ordenada de 1000 elementos
ListaOrdenada = [i for i in range(1001)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaOrdenada)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-----------------------------------------------------------------------------------

# Ordenada de 30000 elementos
ListaOrdenada = [i for i in range(30001)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaOrdenada)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-----------------------------------------------------------------------------------

# Ordenada de 50000 elementos
ListaOrdenada = [i for i in range(50001)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaOrdenada)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-----------------------------------------------------------------------------------

# Ordenada de 100000 elementos
ListaOrdenada = [i for i in range(100001)]

inicio = time.time()
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted_list = selection_sort(ListaOrdenada)
fim = time.time()
#print(sorted_list)
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))
