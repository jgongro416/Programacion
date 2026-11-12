def pedir_entero(mensaje: str) -> int:

    return int(input(mensaje))

def main():
    dividendo = pedir_entero("Dime el dividendo")
    divisor = pedir_entero("Dime el divisor")
    if divisor!= 0:
        print(dividendo/divisor)
    else:
        print("Error no se puede dividir entre 0")
if __name__=="__main__":
    main()