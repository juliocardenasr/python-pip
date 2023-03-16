import random

rounds        = 0
max_rounds    = 5
computer_wins = 0
user_wins     = 0

options =("piedra","papel","tijera")

rounds        = 0
max_rounds    = 5
computer_wins = 0
user_wins     = 0

while rounds < max_rounds:
    
    computer_option = random.choice(options)
    user_option = input("elija piedra, papel o tijera: ")
    user_option = user_option.lower()

    if user_option not in options:
        print("eleccion incorrecta")
    else:
        print("computador: ", computer_option)
        print("usuario   : ", user_option)
        print()
    
        if user_option == computer_option:
            print("Empate")
    
        elif user_option == "piedra":
            if computer_option == "papel":
                print("papel envuelve a piedra")
                print("el computador gana")
                computer_wins += 1
            else:
                print("piedra destroza a tijera")
                print("el usuario gana")
                user_wins += 1
                
        elif user_option == "papel":
            if computer_option == "piedra":
                print("papel envuelve a piedra")
                print("el usuario gana")
                user_wins += 1
            else:
                print("tijera corta papel")
                print("el computador  gana")
                computer_wins += 1
            
        elif user_option == "tijera":
            if computer_option == "piedra":
                print("piedra destroza a tijera")
                print("el computador gana")
                computer_wins += 1
            else:
                print("tijera corta papel")
                print("el usuario  gana")
                user_wins += 1 
                
        rounds += 1
        print()
        print('.................')
        print("partidos jugados  : ", rounds)
        print("ganados computador: ", computer_wins)
        print("ganados usuario   : ", user_wins)
        print()

print()
print()
if computer_wins > user_wins:
    print("El computador gano!!!!!!!!!!!!")
else:
    print("El usuario gano!!!!!!!!!!!!")