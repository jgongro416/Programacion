import random
def numeroAleatorio()->int:

    return random.randint(0,1000)


def pedir_entero(entero:str)->int:

    return int(input(entero))


def calculo(num1:int,num2:int,numA:int)->int:
    resultado = numA + num1 + num2
    return resultado


def main():
    
    aleatorio:int = numeroAleatorio()
    valor1:int = pedir_entero("Dime un valor para sumarle o restarle al numero aleatorio: ")
    valor2:int = pedir_entero("Dime el segundo valor para sumarle o restarle al numero aleatorio: ")
    print(f"{aleatorio} + {valor1} + {valor2} = {calculo(valor1,valor2,aleatorio)}")


if __name__=="__main__":
    main()