# ----------------------------------------
# Cálculo de Sueldo Neto en República Dominicana
# Con escala anual de ISR (DGII) + Nombre y Años en la empresa
# ----------------------------------------

# Constantes
TSS = 0.0591        # 5.91% Seguridad Social
BONIFICACION = 0.10 # 10% Bonificación
DOBLE_SUELDO = 1    # Equivalente a un sueldo adicional

print("\n--- CÁLCULO DE SUELDO NETO (RD) ---\n")

# Función para calcular ISR según escala DGII
def calcular_isr_mensual(sueldo_mensual):
    renta_anual = sueldo_mensual * 12
    
    if renta_anual <= 416220:
        isr_anual = 0
    elif renta_anual <= 624329:
        excedente = renta_anual - 416220
        isr_anual = excedente * 0.15
    elif renta_anual <= 867123:
        excedente = renta_anual - 624329
        isr_anual = 31216 + excedente * 0.20
    else:
        excedente = renta_anual - 867123
        isr_anual = 79776 + excedente * 0.25
    
    return isr_anual / 12  # convertir a mensual

# Entrada de datos
try:
    nombre = input("Ingrese el nombre del empleado: ")
    anios = int(input("¿Cuántos años lleva en la empresa?: "))

    sueldo_bruto = float(input("Digite el sueldo bruto mensual (RD$): "))
    if sueldo_bruto <= 0:
        print("Error: El sueldo debe ser mayor que cero.")
        exit()

    otros_descuentos = float(input("Digite otros descuentos (RD$, si no hay escriba 0): "))

    aplica_bonificacion = input("¿Aplica bonificación? (si/no): ").strip().lower()
    aplica_doble_sueldo = input("¿Aplica doble sueldo? (si/no): ").strip().lower()

    # Cálculos
    desc_tss = sueldo_bruto * TSS
    desc_isr = calcular_isr_mensual(sueldo_bruto)

    bonificacion = sueldo_bruto * BONIFICACION if aplica_bonificacion == "si" else 0
    doble_sueldo = sueldo_bruto * DOBLE_SUELDO if aplica_doble_sueldo == "si" else 0

    sueldo_neto = sueldo_bruto - desc_tss - desc_isr - otros_descuentos + bonificacion + doble_sueldo

    # Resultados
    print("\n--- Detalle del cálculo ---")
    print(f"Empleado: {nombre}")
    print(f"Años en la empresa: {anios}")
    print(f"Sueldo Bruto: RD${sueldo_bruto:,.2f}")
    print(f"Descuento Seguridad Social (TSS): RD${desc_tss:,.2f}")
    print(f"Descuento ISR (DGII): RD${desc_isr:,.2f}")
    print(f"Otros Descuentos: RD${otros_descuentos:,.2f}")
    print(f"Bonificación: RD${bonificacion:,.2f}")
    print(f"Doble Sueldo: RD${doble_sueldo:,.2f}")
    print("---------------------------")
    print(f"Sueldo Neto: RD${sueldo_neto:,.2f}")

except ValueError:
    print("Error: Debe ingresar valores numéricos válidos.")
