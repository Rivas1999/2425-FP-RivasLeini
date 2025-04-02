# Abrimos el archivo escrito.
with open('my_notes.txt', 'w') as archivo:
    # Escribir tres líneas de notas personales en el archivo.
    archivo.write('Primera nota: Aprendiendo a manejar archivos en Python.\n')
    archivo.write('Segunda nota: Es importante cerrar los archivos después de usarlos.\n')
    archivo.write('Tercera nota: Utilizar "with open" es una buena práctica.\n')
# El archivo se cierra automáticamente al salir del bloque 'with'.

# Abrimos el archivo en modo lectura.
with open('my_notes.txt', 'r') as archivo:
    # Leemos y mostramos cada línea del archivo.
    for linea in archivo:
        print(linea.strip())  # Usamos strip() para eliminar espacios en blanco y saltos de línea adicionales.
# El archivo se cierra automáticamente al salir del bloque 'with'.
