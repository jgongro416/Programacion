def main():
    capitalIncial=float(input("Cuando dinero vas a ingresar: "))
    primeraño=round((capitalIncial*1.04),2)
    print(f"En un año conseguira un total de: {primeraño}€")
    segundoaño=round((primeraño*1.04),2)
    print(f"En el segundo año conseguira un total de: {segundoaño}€")
    terceraño=round((segundoaño*1.04),2)
    print(f"En el tercer año conseguira un total de:  {terceraño}€")
if __name__=="__main__":
    main()