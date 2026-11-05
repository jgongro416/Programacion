def main():
    frase=input("Dime una frase: ")
    print(f"".join(frase.split()[::-1]))

if __name__=="__main__":
    main()