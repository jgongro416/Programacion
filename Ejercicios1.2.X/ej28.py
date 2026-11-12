import math #para añadir la raiz cuadrada utilizada en la funcion area_calculo

def pedir_decimal(decimal)-> float:
    """
    Funcion para pedir un numero float
    """
    return float(input(decimal))


def lados_triangulos()-> float:
    """
    Funcion para pedir los datos de los lado del triangulo
    """
    
    num1 = pedir_decimal("Introduce un lado del triangulo(cm): ")
    num2 = pedir_decimal("Introduce el segundo lado del triangulo(cm): ")
    num3 = pedir_decimal("Introduce el ultimo lado del triangulo(cm): ")
    return num1, num2, num3

def area_calculo(a:float,b:float,c:float)->float:
    """
    Funcion para el calculo del semiperimetro y del area del triangulo
    """
    
    s:float=(a + b + c)/2
    area:float = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return round(area,3)



def main():

    ladoA, ladoB, ladoC = lados_triangulos() 
    area:float = area_calculo(a=ladoA,b=ladoB,c=ladoC)
    print(f"El triangulo de lado {ladoA}cm, {ladoB}cm y {ladoC}cm tiene un area de {area}cm^2 ")



if __name__=="__main__":
    main()