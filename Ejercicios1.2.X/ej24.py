def main():
    entero=input("Dime el precio completo:  ")
    print(f"{(entero.split(",")[0])} euros con {(entero.split(",")[1])} centimos")
if __name__=="__main__":
    main()