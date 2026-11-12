def pedir_nombre_sexo(mensaje:str)->str:

    return  str(input(mensaje))


def pedir_entero(mensaje: str) -> int:

    return int(input(mensaje))



def main():

    cantidadIntegrantes:int = pedir_entero("Cuantas personas sois en total: ")
    nombre:str=""
    while cantidadIntegrantes!= 0:
        nombreEj=pedir_nombre_sexo("Dime que nombre tiene el integrante: ")
        sexoEJ=pedir_nombre_sexo("Dime que genero es(F/M): ")
        if sexoEJ=="F" and nombreEj>="m" or sexoEJ=="M" and nombreEj<"n":
            grupoA=+ nombreEj+", "
        if sexoEJ=="F" and nombreEj<"m" or sexoEJ=="M" and nombreEj>="n":
            grupoB=+ nombreEj+", "
        cantidadIntegrantes-=1
    print(grupoA)
    print(grupoB)    

    
if __name__=="__main__":
    main()