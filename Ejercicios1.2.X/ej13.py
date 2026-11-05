def main():
    dividiendo=float(input("Dime el dividiendo: "))
    divisor=float(input("Dime el divisor: "))
    conciente=dividiendo//divisor
    resto= dividiendo%divisor
    print(f"La división de {dividiendo} entre {divisor} da un cociente {conciente} y un resto {resto}")
if __name__=="__main__":
    main()