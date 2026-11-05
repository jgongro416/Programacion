def main():
    suma =int(0)
    numero=float(input("Dime el primer numero: "))
    suma =+numero
    numero=float(input("Dime el segundo numero: "))
    suma =+suma+numero
    numero=float(input("Dime el tercer numero: "))
    suma =+suma+numero
    print(f"La suma de los numeros da un total de {suma}")
if __name__=="__main__":
    main()