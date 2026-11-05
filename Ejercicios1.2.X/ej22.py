def main():
    frase=input("Dime una frase: ")
    letra=input("Dime una  letra para poner en mayuscula: ")
    print(frase.replace(letra,letra.upper()))
if __name__=="__main__":
    main()