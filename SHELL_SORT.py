# Aleatório com 10 elementos
import time
import random

Lista = random.sample(range(11), 10)
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(Lista)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# Aleatório com 1000 elementos
import time
import random

Lista = random.sample(range(1001), 1000)
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(Lista)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-----------------------------------------------------------------------


# Aleatório com 30000 elementos
import time
import random

Lista = random.sample(range(30001), 30000)
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(Lista)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# Aleatório com 50000 elementos
import time
import random

Lista = random.sample(range(50001), 50000)
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(Lista)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

---------------------------------------------------------------------------

# Aleatório com 100000 elementos
import time
import random

Lista = random.sample(range(100001), 100000)
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(Lista)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))


----------------------------------------------------------------------------------------------------------------------------------------------------

# Decrescente com 10 elementos
import time
import random

ListaDecrescente = [i for i in range(10, -1, -1)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaDecrescente)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# Decrescente com 1000 elementos
import time
import random

ListaDecrescente = [i for i in range(1000, -1, -1)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaDecrescente)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-----------------------------------------------------------------------


# Decrescente com 30000 elementos
import time
import random

ListaDecrescente = [i for i in range(30000, -1, -1)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaDecrescente)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# Decrescente com 50000 elementos
import time
import random

ListaDecrescente = [i for i in range(50000, -1, -1)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaDecrescente)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

------------------------------------------------------------------------

# Decrescente com 100000 elementos
import time
import random

ListaDecrescente = [i for i in range(100000, -1, -1)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaDecrescente)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

----------------------------------------------------------------------------------------------------------------------------------------------------

# ORDENADA com 10 elementos
import time
import random

ListaOrdenada = [i for i in range(11)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaOrdenada)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# ORDENADA com 1000 elementos
import time
import random

ListaOrdenada = [i for i in range(1001)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaOrdenada)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-----------------------------------------------------------------------


# ORDENADA com 30000 elementos
import time
import random

ListaOrdenada = [i for i in range(30001)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaOrdenada)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

-------------------------------------------------------------------------

# ORDENADA com 50000 elementos
import time
import random

ListaOrdenada = [i for i in range(50001)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaOrdenada)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))

------------------------------------------------------------------------

# ORDENADA com 100000 elementos
import time
import random

ListaOrdenada = [i for i in range(100001)]
#for de 5 rodadas para tirar a média do tempo

    #inicio contagem do tempo para ordenar
inicio = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
    #ordenando pelo algoritmo
Ordenada = shell_sort(ListaOrdenada)
    #fim contagem do tempo para ordenar
fim = time.time()
    #exibindo o tempo para ordenar a lista
print("Tempo de execução em segundos é {:.2f}".format(fim-inicio))





