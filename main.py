# Constantes (valores aproximados)
TSS = 0.0591        # 5.91% Seguridad Social
ISR = 0.15          # 15% ISR simplificado
BONIFICACION = 0.10 # 10% Bonificación
DOBLE_SUELDO = 1    # Equivalente a un sueldo adicional

print("\n*** CÁLCULO DE SUELDO NETO (RD) ***\n")

# Entrada de datos
try:
    sueldo_bruto = float(input("Digite el sueldo bruto del empleado (RD$): "))
    if sueldo_bruto <= 0:
        print("Error: El sueldo debe ser mayor que cero.")
        exit()

    otros_descuentos = float(input("Digite otros descuentos (RD$, si no hay escriba 0): "))

    aplica_bonificacion = input("¿Aplica bonificación? (si/no): ").strip().lower()
    aplica_doble_sueldo = input("¿Aplica doble sueldo? (si/no): ").strip().lower()

    # Cálculos
    desc_tss = sueldo_bruto * TSS
    desc_isr = sueldo_bruto * ISR

    bonificacion = sueldo_bruto * BONIFICACION if aplica_bonificacion == "si" else 0
    doble_sueldo = sueldo_bruto * DOBLE_SUELDO if aplica_doble_sueldo == "si" else 0

    sueldo_neto = sueldo_bruto - desc_tss - desc_isr - otros_descuentos + bonificacion + doble_sueldo

    # Resultados
    print("\n--- Detalle del cálculo ---")
    print(f"Sueldo Bruto: RD${sueldo_bruto:,.2f}")
    print(f"Descuento Seguridad Social (TSS): RD${desc_tss:,.2f}")
    print(f"Descuento ISR: RD${desc_isr:,.2f}")
    print(f"Otros Descuentos: RD${otros_descuentos:,.2f}")
    print(f"Bonificación: RD${bonificacion:,.2f}")
    print(f"Doble Sueldo: RD${doble_sueldo:,.2f}")
    print("-----------------------------")
    print(f"Sueldo Neto: RD${sueldo_neto:,.2f}")

except ValueError:
    print("Error: Debe ingresar valores numéricos válidos.")
