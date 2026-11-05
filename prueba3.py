def suma(numero1, numero2):
    return numero1+numero2

def dividir(dividiendo, divisor):
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero")
    return dividiendo/divisor

def main():
    print(f"La suma de 3 + 2 es {suma(3,2)}")

if __name__=="__main__":
    main()