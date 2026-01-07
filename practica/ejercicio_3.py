count = 0
while count < 3:
    try:
        if count == 0:
            a = float(input("Ingrese el primer número: "))
        elif count == 1:
            b = float(input("Ingrese el segundo número: "))
        else:
            c = float(input("Ingrese el tercer número: "))
        count += 1
    except ValueError:
        print("Entrada inválida. Ingrese un número.")

# Determinar mayor y menor sin usar funciones
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

print("El número mayor es:", mayor)
print("El número menor es:", menor)