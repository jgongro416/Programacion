def main():
    payasos=float(input("Cuantos payasos hay que enviar: "))
    muñecas=float(input("Cuantas muñecas hay que enviar: "))
    pTotal=(((payasos*112)+(muñecas*75))/1000)
    print(f"El paquete pesara un total de {pTotal}kg")
if __name__=="__main__":
    main()