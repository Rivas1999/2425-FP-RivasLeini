# Crear el diccionario inicial con la informacion Personal
informacion_personal = {
    "nombre": "Leini Rivas ",
    "edad": 25,
    "ciudad": "Huaquillas",
    "profesion": "Ingeniera"
}

# Acceder y modificar el valor asociado a la clave "ciudad"
informacion_personal["ciudad"] = "Huaquillas"  # Modificamos la ciudad a una diferente

# Agregar una nueva clave-valor para actualizar la profesión
informacion_personal["profesion"] = "Ingeniera de Sistemas"  # Actualizamos la profesión
# Imprimir el diccionario resultante después de los cambios
print(informacion_personal)
# Verificar si la clave "telefono" existe, y si no, agregarla con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0979535903"  # Agregamos la clave-valor "telefono"
# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)  # Usamos pop para eliminar "edad"
# Imprimir el diccionario resultante después de todas las modificaciones
print(informacion_personal)