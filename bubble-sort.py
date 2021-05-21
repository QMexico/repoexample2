# Implementación del ordenamiento de burbuja

def bubbleSort(arr):
    n = len(arr)

    # Iterar sobre todos los elementos del arreglo
    for i in range(n - 1):
        # range(n) también funciona pero el ciclo se ejecutará una vez extra, no necesario

        # Los últimos i elementos estan ya en su lugar
        for j in range(0, n - i - 1):

            # iterar el arreglo de 0 a n-i-1
            # intercambiar si el elemento encontrado es mayor
            # que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# arreglo de prueba
arr = [64, 34, 25, 12, 22, 11, 90, -1, 0, -3]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
