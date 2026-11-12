def pedir_entero(mensaje:str)->int:

    return int(input(mensaje))


def main():
        rentaAnual=pedir_entero("Dime cual es tu renta anual: ")
        if rentaAnual<=10000:
            print(rentaAnual*0.05)    
        if rentaAnual >10000 | rentaAnual<=20000:
            print(rentaAnual*0.15) 
        if rentaAnual >20000 | rentaAnual<=35000:
            print(rentaAnual*0.20)
        if rentaAnual >35000 | rentaAnual<=60000:
            print(rentaAnual*0.30)             
        if rentaAnual >60000:
            print(rentaAnual*0.45)            

if __name__=="__main__":
    main()