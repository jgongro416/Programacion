def fibonacci_hasta(limite: int, a: int = 0, b: int = 1) -> list:
    # Condición de parada y acumulación mediante cortocircuito lógico
    return (a <= limite) and ([a] + fibonacci_hasta(limite, b, a + b)) or []


def pedir_entero(mensaje: str) -> int:
    return int(input(mensaje))


def main():
    limite = pedir_entero("Introduce el número límite para la serie: ")
    serie = fibonacci_hasta(limite)
    print(f"Serie de Fibonacci hasta {limite}: {serie}")

    
if __name__=="__main__":
    main()