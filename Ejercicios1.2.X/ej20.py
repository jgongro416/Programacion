def main():
    tlf=input("Dime tu numero de telefono con prefijo y la extension: ")
    numero= tlf.split("-")[1]
    print(numero)
if __name__=="__main__":
    main()