from actividad_siete.clases import Alquiler

def ingresar_datos():

    marca = input("ingrese la marca del vehiculo: ")
    modelo = input("ingrese el modelo del vehiculo: ")
    año = int(input("ingrese el año del vehiculo: "))
    seguro = float(input("ingrese el seguro: "))
    precio = float(input("ingrese el precio por kilometro: "))
    dni = input("ingrese el dni del arrendatario: ")
    kilometros = int(input("ingrese los kilometros recorridos del vehiculo: "))
    nombre = input("ingrese el nombre del arrendatario")

    alquiler1 = Alquiler(marca=marca, modelo=modelo, año=año, seguro=seguro, precio_por_kilometro=precio,
                         dni_del_arrendatario=dni, kilometros_recorridos=kilometros, nombre=nombre)

    return alquiler1


def opciones_menu():

    print("ingrese 1 para cargar un alquiler")
    print("ingrese 2 para mostrar la lista de alquileres")
    print("ingrese 0 para finalizar")

    opcion = int(input("ingrese una opcion: "))
    return opcion

def menu():
    lista_alquileres = []
    opcion = opciones_menu()

    while opcion!=0:
        if opcion==1:
             alquiler = ingresar_datos()
             lista_alquileres.append(alquiler)
        elif opcion==2:
            for item in lista_alquileres:
                item.mostrar_alquiler()

        opcion = opciones_menu()


menu()

