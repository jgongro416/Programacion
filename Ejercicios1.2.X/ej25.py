def main():
    fecha=input("Cual es tu fecha de nacimientoo (dd/mm/aaaa): ")
    dia = fecha.split("/")[0]
    mes = fecha.split("/")[1]
    año = fecha.split("/")[2]
    print(f"Naciste el dia {dia} del mes numero {mes} del año {año}")
if __name__=="__main__":
    main()