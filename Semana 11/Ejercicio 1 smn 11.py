# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor_a_buscar):
    for i in range(len(matriz)):  # Recorremos las filas
        for j in range(len(matriz[i])):  # Recorremos las columnas
            if matriz[i][j] == valor_a_buscar:
                return f"Valor {valor_a_buscar} encontrado en la posición ({i}, {j})"
    return f"Valor {valor_a_buscar} no encontrado en la matriz"

# Valor que queremos buscar
valor = int(input("Introduce el valor que quieres buscar: "))

# Llamada a la función e impresión del resultado
resultado = buscar_valor(matriz, valor)
print(resultado)