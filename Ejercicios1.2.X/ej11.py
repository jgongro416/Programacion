def main():

    n = int(input("Introduce un entero positivo n: "))
    suma = (n * (n + 1)) // 2
    print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")

if __name__=="__main__":
    main()