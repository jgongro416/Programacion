def main():
    peso=float(input("Dime tu peso(kg): "))
    altura=float(input("Dime tu altura(m): "))
    indMasaCorporal=round((peso/(altura*altura)),2)
    print(f"Tu indice de masa corporal es de {indMasaCorporal}")

if __name__=="__main__":
    main()