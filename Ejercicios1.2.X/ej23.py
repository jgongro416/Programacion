def main():
    correo=input("Dime tu correo electronico:  ")
    print(f"{(correo.split("@")[0])}@ceu.es")
if __name__=="__main__":
    main()