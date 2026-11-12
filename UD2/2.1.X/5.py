def pedir_entero(mensaje: str) -> int:

    return int(input(mensaje))


def pedir_decimal(mensaje: str) -> float:

    return float(input(mensaje))


def main():


    edad = pedir_entero("Dime tu edad: ")    
    salario = pedir_decimal("Dime tu salario: ")
    if edad>16 and salario>=1000:
        print("Tienes que tributar")
    else :
        print("No tienes que tributar")


if __name__=="__main__":
    main()