
while True:
    try:
        edad = int(input("Cual es tu edad: "))
        if edad < 0:
            print("No estas autorizado para votar. ")
            continue
        break
    except ValueError:
        print ("Dato no congruente. Por favor ingrese la edad nuevamente: ")
        
if edad >= 18:
    print("Puedes votar. porfavor elije de la forma que mas te parezca:")
elif edad >= 7 and edad <= 17:
    print("Debe presentar tarjeta de identidad: ")
else:
    edad <= 7
    print("No puedes votar: ")
    