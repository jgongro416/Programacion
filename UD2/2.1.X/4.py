def pedir_entero(mensaje: str) -> int:

    return int(input(mensaje))


def main():
    numero= pedir_entero("Dime un numero entero: ")
    if  numero%2 == 0 :
        print("El numero es par")
    else:
        print("El numero es impar")



if __name__=="__main__":
    main()