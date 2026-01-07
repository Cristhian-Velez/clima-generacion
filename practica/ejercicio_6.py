clave_correccta = "velez"
intentos = 0
acceso = False

while intentos < 3 and not acceso:
    entrada = input("Ingrese la contraseña: ")
    if entrada == clave_correccta:
        acceso = True
    else:
        intentos = intentos + 1
        print("Contraseña incorrecta. Intentos restantes:", 3 - intentos)
        
if acceso:
    print("Acceso concedido. ")
else:
    print("Acceso bloqueado")
        
 