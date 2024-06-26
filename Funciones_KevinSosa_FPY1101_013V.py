import os
lectores=[]
libros_existentes=["ALAS DE HIERRO","LA SOMBRA DE LA SIRENA","El Principito","El Libro De la Selva","Harry Potter"]
def limpiar_pantalla():
    os.system('cls' if os.name== 'nt'else'clear')
def registrar_lector():
    limpiar_pantalla()
    print("---Registrar libro---")
    nombre=input("Ingrese Nombre y Apellido: ")
    rut=int(input("ingrese su rut"))
    libro=input("ingresa el nombre del libro que llevarse(ALAS DE HIERRO,LA SOMBRA DE LA SIRENA,El Principito,El Libro De la Selva,Harry Potter): ")
    while libro not in libros_existentes:
        print("Libro no valido,Los libros existentes son", libros_existentes)
        libro=input("Ingrese el libro nuevamente: ")
    año=input("ingrese el año del libro: ")
    sku=input("Ingrese el sku (6 primeras letras del título del libro, las 3 primeras letras del autor, año de publicación)")
    lectores.append({
        "nombre": nombre,
        "rut":rut,
        "libro": libro,
        "año":año,
        "sku":sku
    })
    print("Libro registrado exitosamente. ")
    input("Presione enter para continuar.")
def prestar_libro():
    limpiar_pantalla()
    print("---Prestar Libro---")
    nombre=input("Ingrese Nombre y Apellido: ")
    rut=int(input("ingrese su rut"))
    libro=input("ingresa el nombre del libro")
    año=input("ingrese el año del libro: ")
    sku=input("Ingrese el sku (6 primeras letras del título del libro, las 3 primeras letras del autor, año de publicación)")
    lectores.append({
        "nombre": nombre,
        "rut":rut,
        "libro": libro,
        "año":año,
        "sku":sku
    })
    print("Libro Prestado exitosamente. ")
    input("Presione enter para continuar.")



def Listar_todos_los_libros():
    limpiar_pantalla()
    print("---lista de libros ocupados---")    
    if not lectores:
        print("Estan todos los libros con disponibilidad")
    else:
        for idx,lector in enumerate(lectores,start=1):
            print(f"lector {idx}: ")
            print(f"Nombre:{lector['nombre']}")
            print(f"Rut:{lector['rut']}")
            print(f"Libro:{lector['libro']}")
            print(f"año:{lector['año']}")
            print(f"Sku:{lector['sku']}")
            print(f"------------------------")
    input("Presione enter para continuar...")
def Imprimir_reporte_de_préstamos():
    limpiar_pantalla()
    print("---Reporte De Prestamos---")
    print("libros ocupados")
    for idx, libro in enumerate(libros_existentes,start=1):
        print(f"{idx}.{libro}")
    opcion=int(input("seleccione el numero de libro ocupado que desea imprimir(0 para imprimir todos): "))
    if opcion==0:
        for libro in libros_existentes:
            Imprimir_reporte_de_préstamos(libro)
    elif opcion in range(1,len(libros_existentes)+1):
        Imprimir_reporte_de_préstamos(libros_existentes[opcion-1])
    else:
        print("Opcion no valida")
def Imprimir_reporte_de_préstamos(libro):
    filename=f"libros ocupados_{libro.lower().remplace('','_')}.txt"
    with open(filename, 'w') as file:
          file.write(f"libros ocupados-libros:{libro}\n") 
          for lector in lectores:
              if lector["libro"]==libro:
                  file.write("-------------------\n")
                  file.write(f"Nombre{lector}['nombre']\n")
                  file.write(f"Rut{lector}['rut']\n")
                  file.write(f"Libro{lector}['libro']\n")
                  file.write(f"Año{lector}['año']\n")
                  file.write(f"Sku{lector}['sku']")
    print(f"Se ha generado el archivo'{filename}'correctamente.")
    input("Presiona enter para continuar")
def main():
    while True:
        limpiar_pantalla()
        print("----Biblioteca Sosa----")
        print("1.Registrar libro")
        print("2.Prestar libro")
        print("3.Listar todos los libros")
        print("4.Imprimir reporte de préstamos")
        print("5.Salir del Programa")
        opcion=input("Selecciona una opcion")
        if opcion == '1':
            registrar_lector()
        elif opcion=='2':
            prestar_libro()
        elif opcion=='3':
            Listar_todos_los_libros()
        elif opcion=='4':
            Imprimir_reporte_de_préstamos()
        elif opcion=='5':
            print("Saliendo Del Programa Adios..")
            print("Desarrollado Por Kevin Sosa\nRut: 22.086.276-3 ")        
            break
        else:
            print("opcion no valida, intente nuevamente")
            input("Presione enter para continuar...")
__name__=='__main__'
main()            
                