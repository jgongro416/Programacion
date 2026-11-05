def main():
    pagoFinal=float(input("Cual ha sido el precio que has pagado por el articulo(€): "))
    iva=int(input("Cuanto era el IVA del producto que has pagado(%): "))
    productoSinIVA=pagoFinal-(pagoFinal*(iva/100))
    print(f"Has pagado un total de {pagoFinal}€ teniendo el producto un iva del {iva}% siendo el coste sin IVA de {productoSinIVA}")
if __name__=="__main__":
    main()