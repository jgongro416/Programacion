def pedir_decimal(mensaje:str)->float:

    return float(input(mensaje))


def puntuacion_valida(puntuacion:float)->None:

    if puntuacion<6:
        print("No apto")
    else:
        print("No apto")

def main():


    puntuacion=pedir_decimal("Dime la puntacion: ")
    
    if puntuacion < 4 and puntuacion>=0:
        print("Inaceptable")

    if puntuacion>=4 and puntuacion<6:
        print("Aceptable")

    if puntuacion>=6:
        print("Meritorio")

    if puntuacion<0:
        print("La nota tiene que ser positiva")    

    puntuacion_valida(puntuacion)

    
if __name__=="__main__":
    main()