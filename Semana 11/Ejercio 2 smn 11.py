# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [34, 12, 50],
    [21, 45, 23],
    [99, 18, 67]
]

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()  # Salto de línea para mejor visualización

# Función que aplica el algoritmo Bubble Sort en una fila específica
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiamos los valores
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Mostramos la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Fila que queremos ordenar (0, 1 o 2 para la matriz de 3x3)
fila_a_ordenar = int(input("Introduce el número de la fila que quieres ordenar (0, 1 o 2): "))

# Ordenamos la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print(f"Matriz con la fila {fila_a_ordenar} ordenada:")
imprimir_matriz(matriz)
