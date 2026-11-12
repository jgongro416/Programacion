def tipoPizza()->str:


    print("Seleccion el tipo de Pizza que deseas")
    print("1. Normal")
    print("2. Vegetariana")
    pizza=int(input())
    if pizza==1:
        tipo="Normal"
    if pizza==2:
        tipo="Vegetariana"
    if pizza !=1 and pizza !=2:
        print("Pon una opcion disponible")
    return tipo


def pizzaNormal()->str:
    print("Seleccion los ingredientes de la pizza")
    print("1. Peperoni")
    print("2. Salmon")
    print("3. Jamon")
    ingrediente=int(input())
    if ingrediente==1:
        tipo="Peperoni"
    if ingrediente==2:
        tipo="Salmon"
    if ingrediente==3:
        tipo="Jamon"
    if ingrediente !=1 and ingrediente !=2 and ingrediente !=3:
        print("Pon una opcion disponible")
    return tipo


def pizzaVegetariana()->str:
    print("Seleccion los ingredientes de la pizza")
    print("1. Tofu")
    print("2. Pimiento")
    print("3. Piña")
    ingrediente=int(input())
    if ingrediente==1:
        tipo="Tofu"
    if ingrediente==2:
        tipo="Pimiento"
    if ingrediente==3:
        tipo="Piña"
    if ingrediente !=1 and ingrediente !=2 and ingrediente !=3:
        print("Pon una opcion disponible")
    return tipo



def main():
    tipo:str=tipoPizza()
    if tipo=="Normal":
        ingrediente=pizzaNormal()
    if tipo=="Vegetariana":
        ingrediente=pizzaVegetariana()
    print(f"Has pedido una pizza tipo {tipo} con {ingrediente}")


    
if __name__=="__main__":
    main()