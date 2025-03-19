# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Programa principal

# Primera llamada: solo monto total
monto1 = 200
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Compra 1: Monto total = {monto1}, Descuento = {descuento1}, Monto final = {monto_final1}")

# Segunda llamada: monto total y porcentaje de descuento proporcionado
monto2 = 300
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
monto_final2 = monto2 - descuento2
print(f"Compra 2: Monto total = {monto2}, Descuento = {descuento2}, Monto final = {monto_final2}")