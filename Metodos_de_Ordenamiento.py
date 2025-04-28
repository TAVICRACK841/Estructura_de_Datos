'''BURBUJA'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("METODO DE BURBUJA")
entrada = input("Ingresa números separados por coma para ordenarlos (burbuja): ")
lista = list(map(int, entrada.split(',')))
resultado = bubble_sort(lista)
print("Lista ordenada con burbuja:", resultado)

'''POR INSERCÓN'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print("METODO POR INSERCIÓN")
entrada = input("Ingresa números separados por coma para ordenarlos (inserción): ")
lista = list(map(int, entrada.split(',')))
resultado = insertion_sort(lista)
print("Lista ordenada con inserción:", resultado)

'''POR SELECCIÓN'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("METODO POR SELECÓN")
entrada = input("Ingresa números separados por coma para ordenarlos (selección): ")
lista = list(map(int, entrada.split(',')))
resultado = selection_sort(lista)
print("Lista ordenada con selección:", resultado)
