#EJERCICIOS DE PREPARACION
#UN PROGRAMA QUE SOLICITE EL PESO EN (KG) Y LA ALTURA (M) DE UAN PERSONA#
#VALIDAR QUE SEAN NUMEROS POSITIVOS, CALCULE EL INDICE DE MASA CORPORAL (IMC) Y MOSTRAR EL VALOR
#CON DOS DECIMALES

while True:
    entrada = input("Ingrese el peso en kilogramos. (el. 70.5): ")
    try:
        peso = float(entrada)
        if peso <= 0:
            print("El peso debe ser mayo que 0. ")
            continue
        break
    except ValueError:
        print("Entrada invalida. Ingrese un numero.")    
    
#PEDIR ALTURA VALIDA

while True:
    entrada = input("Ingrese su altura en metros. (ej. 1.70):")
    try:
        altura = float(entrada)
        if altura <= 0 :
            print("La altura debe ser mayor que 0")
            continue
        break
    except ValueError:
        print("Entrada invalida. Ingrese un numero.")
    
    #VALIDACION RAZONABLE DE ALTURA
    
if altura <= 0.5:
    print("Atencion: la altura ingresada es muy baja. verifique la unidad en (metros). ")

#CALCULO IMC

imc = peso / (altura * altura)
print("IMC calculado: {:.2f}".format(imc))

#CLASIFICACION 

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc < 25.0:
    print("Clasificación: Normal")
elif imc < 30.0:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificaión: Obesidad")