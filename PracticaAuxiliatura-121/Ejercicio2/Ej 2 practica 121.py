class compu:
    def __init__(self):
        self.__marca="Asus"
        self.__procesador="intel"
        self.__ram=16 
        self.__almacenamiento=512
    def leerdatos(self):
        self.__marca=input("Ingrese marca: ")
        self.__procesador=input("Ingresar procesador: ")
        self.__ram=int(input("Ram: "))
        self.__almacenamiento=int(input("Almacenamiento: "))
    def checarRAM(self):
        x=int(input("Valor de RAM a Comparar: "))
        if self.__ram ==x:
            print(f"la RAM {self.__ram} es igual a {x} Gb")
        else:
            print(f"la RAM {self.__ram} NO es igual a {x} Gb")
    def almacenamiento(self):
        return self.__almacenamiento
    def mostrarDatos(self):
        print(f"Marca: {self.__marca} | RAM: {self.__ram}GB | Disco: {self.__almacenamiento}GB")
if __name__ =="__main__":
    pc1 = compu()
    pc2 = compu()
    print("--- INGRESO DE DATOS PARA PC 2 ---")
    pc2.leerdatos()
    print("\n--- VERIFICAR RAM EN PC 1 ---")
    pc1.checarRAM()
    print("\n--- COMPUTADORA CON MAYOR ALMACENAMIENTO ---")
    if pc1.almacenamiento() > pc2.almacenamiento():
        print("PC 1 tiene mayor almacenamiento:")
        pc1.mostrarDatos()
    elif pc2.almacenamiento() > pc1.almacenamiento():
        print("PC 2 tiene mayor almacenamiento:")
        pc2.mostrarDatos()
    else:
        print("Ambas tienen mismo almacenamiento.")
