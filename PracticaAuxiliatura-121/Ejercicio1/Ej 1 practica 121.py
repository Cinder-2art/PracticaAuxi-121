class vehiculo:
    def __init__(self):
        self.__marca= ""
        self.__modelo= ""
        self.__año= 0
        self.__kilometraje= 0
        self.__color= "Rojo"
    def ingresadatos(self):
        self.__marca= input("Ingrese marca del auto: ")
        self.__modelo= input("Ingrese el modelo: ")
        self.__año= input("Ingrese año: ")
        self.__kilometraje= int(input("Ingrese el Kilometraje (Km): "))
        self.__color= input("Ingrese su color: ")
    def mostrarkilom(self):
        metros=(self.__kilometraje * 1000)
        print(f"Vehiculo {self.__marca}  {self.__modelo}:{self.__kilometraje} Km -> {metros} m")
    def cambiarColor(self):
        self.__color = input(f"Ingrese el nuevo color para el {self.__marca}: ")
        print(f"El nuevo color es: {self.__color}")
if __name__ == "__main__":
    auto1 = vehiculo()
    auto2 = vehiculo()

    print("--- LECTURA AUTO 1 ---")
    auto1.ingresadatos() 

    print("\n--- CAMBIO DE COLOR Y KILOMETRAJE AUTO 1 ---")
    auto1.cambiarColor()
    auto1.mostrarkilom()