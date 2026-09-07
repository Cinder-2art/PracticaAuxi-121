#+===================================+
#|                bus                |
#+===================================+
#| - __placa: str                    |
#| - __capacidad_total: int          |
#| - __pasajeros_actuales: int       |
#| - __recaudacion: float            |
#+===================================+
#| + __init__()                      |
#| + registrarbus(): void            |
#| + subirPasajeros(): void          |
#| + cobrarPasaje(): void            |
#| + mostrarAsientosDisponibles(): void |
#+===================================+
class bus:
    def __init__(self):
        self.__placa=""
        self.__capacidad_total=30
        self.__pasajeros_actuales=0
        self.__recaudacion=0.0
    def registrarbus(self):
        self.__placa=input("placa del bus: ")
        self.__capacidad_total=int(input("capacidad total de asientos: "))
    def subirPasajeros(self):
        x=int(input("¿Cuántos pasajeros subirán?: "))
        asientos_libres = self.__capacidad_total - self.__pasajeros_actuales
        if x <= 0:
            print("Cantidad no válida.")
        elif x > asientos_libres:
            print(f"No pueden subir {x} pasajeros. Solo quedan {asientos_libres} disponibles.")
        else:
            self.__pasajeros_actuales += x
            print(f"Subieron {x} pasajeros sin novedad.")
    def cobrarPasaje(self):
        costo_pasaje=2.50
        monto=self.__pasajeros_actuales*costo_pasaje
        self.__recaudacion+=monto
        print(f"Se cobró {costo_pasaje:.2f} Bs. a {self.__pasajeros_actuales} pasajeros.")
        print(f"Recaudación acumulada: {self.__recaudacion:.2f} Bs.")
    def mostrarAsientosDisponibles(self):
        libres = self.__capacidad_total - self.__pasajeros_actuales
        print(f"Asientos ocupados: {self.__pasajeros_actuales}/{self.__capacidad_total} | Disponibles: {libres}")
if __name__ == "__main__":
    bus1=bus()
    bus1.registrarbus()
    bus1.subirPasajeros()
    bus1.cobrarPasaje()
    bus1.mostrarAsientosDisponibles()