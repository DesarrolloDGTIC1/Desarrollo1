print('SECCION 8 - PRACTICA 05 - Adivina el numero ')

# Crear un juego donde el sistema genere un numero aleatorio y el jugador intente adivinar el numero aleatorio.
# Para crear este juego ten encueta los siguientes datos
# Difícil 5 intentos o vidas
# Intermedio 7 intentos o vidas
# Fácil 10 intentos o vidas
# De acuerdo como va intentado el juego le debe dar una pista si el número es más grande o más pequeño.
# También tiene que indicarle las vidas que le quedan.

import random , os

def menu():
    
    while True:
        print("Bievenido al menu de adivina el numero")
        print("--------------------------------")
        print("1) Facil (10 intentos)")
        print("2) Intermedio (7 intentos)")
        print("3) Dificil (5 intentos)")
        print("4) Salir")

        opc= int(input("Escoja la dificultad : "))

        os.system('cls')

        if opc == 1:
            adivina(10)
        elif opc == 2:
            adivina(7)
        elif opc == 3:
            adivina(5)
        elif opc == 4:
            print("Saliendo..")
            break
        else:
            print("Ha introducido una opcion invalida, intente de nuevo..")
        
        

def adivina(intentos):

    Numrandom = random.randint(1,100)

    while intentos > 0:

        intentos-=1
    
        numero=int(input("Ingrese el numero ") )

        if Numrandom > numero:
            print(f'Sigue intentando, es un numero mayor al {numero}')
        elif Numrandom < numero:
            print(f'Sigue intentando, es un numero menor al {numero}')
        elif Numrandom == numero:
            os.system('cls')
            print(" ¡¡¡¡  Felicidades !!!! Has adivinado el numero..")
            break

        print(f'-- Actualmente tiene {intentos} intentos ---')

    print(f'El numero generado es {Numrandom}')

def main():

    menu()

if __name__ == '__main__':
    main()



    
