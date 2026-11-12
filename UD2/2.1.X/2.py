def pedir_contraseña(contraseña:str)->str:

    return  str(input(contraseña))

def main():
    contraseña = pedir_contraseña("Dime una contraseña(no se distinguen entre mayusculas y minusculas): ")
    contraseña.lower
    Intento = pedir_contraseña("Introduce la contraseña: ")
    Intento.lower
    if contraseña==Intento:
        print("Contraseña correcta")
    else:
        print("Contrasela incorrecta")
if __name__=="__main__":
    main()