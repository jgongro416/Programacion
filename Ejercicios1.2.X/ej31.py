def pedir_entero(mensaje: str) -> int:

    return int(input(mensaje))

def divisiones(numero:int)-> list:
    return list(filter(lambda filtro: numero % filtro == 0, range(1, numero +1)))


def main():

    numero = pedir_entero("Dime un número")
    divisiones = divisiones(numero)
    print(f"Los divisores de {numero} son: {divisiones}")

    
if __name__=="__main__":
    main()