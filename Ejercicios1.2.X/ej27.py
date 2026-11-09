def main():
    # Entrada de datos
    nombre: str = input("Dime que productos quieres: ")
    cantidad: int = int(input("Que cantidad quieres: "))
    precioU: float = float(input("Que precio untiraio tiene: "))

    # Cálculo o proceso
    precioT: float = cantidad * precioU

    # Salida de datos
    print(f"{nombre}, cantidad{cantidad}, c/u:{precioU:09.2f}€, {precioT:011.2f}€")


if __name__=="__main__":
    main()