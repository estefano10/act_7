class Alquiler:
    def __init__(self,marca,modelo, año, precio_por_kilometro, seguro, dni_del_arrendatario, kilometros_recorridos, nombre):

        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_por_kilometro = precio_por_kilometro
        self.seguro = seguro
        self.dni_del_arrendatario = dni_del_arrendatario
        self.kilometros_recorridos = kilometros_recorridos
        self.nombre = nombre


def mostrar_alquiler(self):
    print(f"marca del auto: {self.marca}")
    print(f"el modelo del auto es: {self.modelo}")
    print(f"el año del auto es: {self.año}")
    print(f" el precio por kilometro es: {self.precio_por_kilometro}")
    print(f"seguro: {self.seguro}")
    print(f"dni del arrendatario: {self.dni_del_arrendatario}")
    print(f"kilometros recorridos: {self.kilometros_recorridos}")
    print(f"nombre: {self.nombre}")

    print(self.precio_por_kilometro*self.kilometros_recorridos+self.seguro)

