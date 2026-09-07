#+===================================+
#|          CuentaBancaria           |
#+===================================+
#| - __titular: str                  |
#| - __nroCuenta: str                |
#| - __saldo: float                  |
#+===================================+
#| + __init__()                      |
#| + abrircuenta(): void             |
#| + depositar(): void               |
#| + retirar(): void                 |
#| + mostrarDatos(): void            |
#+===================================+
class cuentaBanco:
    def __init__(self):
        self.__titular=""
        self.__nroCuenta=""
        self.__saldo = 0.0
    def abrircuenta(self):
        self.__titular=input("nombre del titular: ")
        self.__nroCuenta=input("nro de cuenta: ")
        self.__saldo=float(input("saldo inicial: "))
    def depositar(self):
        monto=float(input("monto a depositar: "))
        if monto<=0:
            print("El depósito debe ser mayor a 0.")
        else:
            self.__saldo+=monto
            print(f"Depósito realizado. Saldo actual: {self.__saldo:.2f} Bs.")
    def retirar(self):
        monto = float(input("Monto a retirar: "))
        if monto > self.__saldo:
            print(f"Saldo insuficiente. Saldo disponible: {self.__saldo:.2f} Bs.")
        elif monto <= 0:
            print("El retiro debe ser mayor a 0.")
        else:
            self.__saldo-=monto
            print(f"Retiro realizado. Saldo actual: {self.__saldo:.2f} Bs.")
    def mostrarDatos(self):
        print(f"Titular: {self.__titular} | N° Cuenta: {self.__nroCuenta} | Saldo: {self.__saldo:.2f} Bs.")

if __name__ == "__main__":
    cuenta = cuentaBanco()
    cuenta.abrircuenta()
    cuenta.depositar()
    cuenta.retirar()
    cuenta.mostrarDatos()