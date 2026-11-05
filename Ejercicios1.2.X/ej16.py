def main():
    precioHabitual=3.49
    descuentoNFresca=round((precioHabitual*0.40),2)
    nFrescaVendidas=int(input("Cuantas barras de ayer se vendieron: "))
    total=nFrescaVendidas*descuentoNFresca
    print(f"Precio del pan: {precioHabitual}€")
    print(f"Si es de ayer: {descuentoNFresca}€")
    print(f"Has recaudado con las barras de ayer un total de {total}€")
if __name__=="__main__":
    main()