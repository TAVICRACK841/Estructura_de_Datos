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

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

def menu():
    print("Introduce números separados por espacios:")
    user_input = input()
    arr = list(map(int, user_input.split()))
    while True:
        print("\nSelecciona el método de ordenamiento:")
        print("1. ShellSort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix")
        print("5. Salir")
        choice = input("Opción: ")
        if choice == '1':
            sorted_arr = shell_sort(arr.copy())
            print("Arreglo ordenado con ShellSort:", sorted_arr)
        elif choice == '2':
            sorted_arr = quicksort(arr.copy())
            print("Arreglo ordenado con Quicksort:", sorted_arr)
        elif choice == '3':
            sorted_arr = heapsort(arr.copy())
            print("Arreglo ordenado con Heapsort:", sorted_arr)
        elif choice == '4':
            sorted_arr = radix_sort(arr.copy())
            print("Arreglo ordenado con Radix:", sorted_arr)
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Para ejecutar el programa, llama a la función menu()
menu()
