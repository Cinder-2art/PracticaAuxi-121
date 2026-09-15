###
#+-----------------------------------+
#|               Auto                |
#+-----------------------------------+
#| - marca: str                      |
#| - color: str                      |
#|  - gasolina: float                |
#+-----------------------------------+
#| + __init__(marca, color, gasolina)|
#| + defecto(): Auto             | 
#| + marca_y_color(m, c): Auto   | 
#| + __pos__(): Auto                 | 
#| + __sub__(otro_auto): float       | 
#| + mostrar(): void                 |
#+-----------------------------------+
###
class Auto:
    def __init__(self, marca: str, color: str, gasolina: float):
        self.marca = marca
        self.color = color
        self.gasolina = float(gasolina)

    @classmethod
    def defecto(cls):
        return cls("Toyota", "Blanco", 10.0)
    @classmethod
    def marca_y_color(cls, marca: str, color: str):
        return cls(marca, color, 20.0)
    def __pos__(self):
        self.gasolina += 5.0
        return self
    def __add__(self, nuevo_color: str):
        if isinstance(nuevo_color, str):
            self.color = nuevo_color
    def __sub__(self, otro_auto):
        if isinstance(otro_auto, Auto):
            return self.gasolina + otro_auto.gasolina
    def mostrar(self):
        print(f"Auto [{self.marca}] | Color: {self.color} | Gasolina: {self.gasolina} L")


if __name__ == "__main__":
    auto1 = Auto.defecto()            
    auto2 = Auto.marca_y_color("Nissan", "Negro")

    print("=== ESTADO INICIAL ===")
    auto1.mostrar()
    auto2.mostrar()

    print("\n=== c) SOBRECARGA ++ (+auto1) -> Incrementar 5L de gasolina ===")
    +auto1
    auto1.mostrar()

    print("\n=== d) SOBRECARGA + (auto2 + 'Azul') -> Cambiar color ===")
    auto2 = auto2 + "Azul"
    auto2.mostrar()

    print("\n=== e) SOBRECARGA - (auto1 - auto2) -> Total de gasolina ===")
    total_gasolina = auto1 - auto2
    print(f"Total de gasolina entre los dos autos: {total_gasolina} Litros")