def pedir_entero(mensaje: str) -> int:

    return int(input(mensaje))

def main():
    
    
    edad=pedir_entero("Dime tu edad: ")
    if edad>=18:
        print("Eres mayor de edad") 
    else:
        print("Eres menor de edad")


if __name__=="__main__":
    main()