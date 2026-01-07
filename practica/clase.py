estudiantes = []

def registrar_estudiantes ():
    print("\n °°°° Registrar estudiantes °°°°")
    nombre = input("Nombre: ").strip().title()
    edad = int(input("Edad: "))
    nota = float(input("Nota (0 - 5): "))
    estudiante = {"nombre": nombre, "edad": edad, "nota": nota}
    estudiantes.append(estudiante)
    print("Estudiante resgistrado satisfactoriamente")

def mostrar_estudiantes():
    print("\n °°°° Lista de estudiantes °°°°")
    if not estudiantes:
        print("No hay estudiantes registrados. ")
    else:
        for i, e in enumerate(estudiantes, 1):
            print(f"{i}. {e['nombre']} - {e['edad']} años -nota:{e['nota']}")
        
def buscar_estudiante ():
    print("\n °°°° Buscar estudiantes °°°°")
    nombre = input ("Ingrese el nombre a buscar: ").strip().lower()
    encontrados = [e for e in estudiantes if nombre in e ["nombre"].lower()]
    if encontrados:
        for e in encontrados:
            print(f"{e['nombre']} - {e['edad']} años -nota:{e['nota']}")
    else:
        print("No se encontro ningun estudiante registrado.")

def calcula_promedio():
    print("\n °°°° Promedio General °°°°")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    notas = [e["nota"] for e in estudiantes]
    promedio = sum(notas) / len (notas)
    print (f" Promedio General: {promedio:.2f}")
    
def menu ():
    while True:
        print("\n °°°° MENU PRINCIPAL °°°°")
        print("1. Registrar estudiantes. ")
        print("2. Mostrar los registros. ")
        print("3. Buscar estudiantes por nombre. ")
        print("4. Calcular promedio general")
        print("5. Salir.")

        opcion = input("Elija una opcion (1-5): ")

        if opcion == "1":
            registrar_estudiantes()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            calcula_promedio()
        elif opcion == "5":
            print("Hasta lueguito....")
            break
        else:
            print("Opcion invalida, intente nuevamente..")    
            
def main():
    menu()
if __name__ == "__main__":
    main()
