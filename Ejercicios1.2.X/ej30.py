def division(n, d):

    return (d * d <= n) and ((n % d == 0) or division(n, d + 1))


def es_primo(n: int) -> bool:

    return (n > 1) and not division(n, 2)


def pedir_entero(mensaje: str) -> int:

    return int(input(mensaje))


def main():

    numero = pedir_entero("Dime un numero: ")
    
    resultado = es_primo(numero)
    texto = ["NO es primo", "es primo"][resultado]
    
    print(f"El {numero} {texto}.")


if __name__ == "__main__":
    main()