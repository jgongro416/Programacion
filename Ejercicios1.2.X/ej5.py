def main():
    importenoiva=float(input("Cuanto cuesta el articulo sin iva(€): "))
    iva=int(input("Que cantidad de iva se le tiene que aplicar(%): "))
    resultado=importenoiva+(importenoiva*(iva/100))
    print(f"El producto sin iva es {importenoiva}€ añadiendole el iva de {iva}% daria un total de {resultado}€")
if __name__=="__main__":
    main()