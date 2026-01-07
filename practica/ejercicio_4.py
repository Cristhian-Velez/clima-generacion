while True:
    try:
        valor = float(input("Ingrese el valor de la compra"))
        if valor <= 0:
            print ("El valor no puede ser negativo: ")
            continue
        break
    except ValueError:
        print("Entrada invalida. Ingrese otro monto de compra")

valor_real = valor
descuento = 0.0
if valor >100000:
    descuento = valor * 0.10
total = valor - descuento

print("Valor origina: ${:.2f}".format(valor_real))
print(" Descuento aplicado: ${:.2f}".format(descuento))
print("Total a pagar: ${:.2f}".format(total))
        