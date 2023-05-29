import random
from emoji import emojize
from time import sleep

user_points = 0
computer_points = 0

options = ['r', 't', 'p'] #lista

print("~~" * 30)
print(emojize(":scissors:  JOGO PEDRA, PAPEL, TESOURA"))
print("~~" * 30)
sleep(1)


while True:

    user_choice = input(emojize(":scissors:  Escolha R para Pedra / T para Tesoura / P para Papel ou Q para SAIR:_ ")).lower() #transforma a entrada do usuário em minúsculo
    if(user_choice == 'q'):
        break

    if user_choice not in options: #verificando se não está na listagem de opções
        continue

    computer_choice = random.randint(0,2)
    # 0 = R - PEDRA / 1 = T- TESOURA / 2 = P-PAPEL
    computer_option = options[computer_choice]

    print(emojize(":robot: O computador escolheu ") + str(computer_option))

    if user_choice == 't' and computer_choice == 't':
        print(emojize(":robot: Empate!"))
    elif user_choice == 'r' and computer_choice == 'r':
        print(emojize(":robot: Empate!"))
    elif user_choice == 'p' and computer_choice == 'p':
        print(emojize(":robot: Empate!"))
    elif (user_choice == 'r') and (computer_choice == 't'):
        print(emojize(":heart: Usuário ganhou!"))
        user_points = user_points + 1
        computer_points = computer_points + 0
    elif (user_choice == 'p') and (computer_choice == 'r'):
        print(emojize(":heart: Usuário ganhou!"))
        user_points = user_points + 1
        computer_points = computer_points + 0
    elif (user_choice == 't') and (computer_choice == 'p'):
        print(emojize(":heart: Usuário ganhou!"))
        user_points = user_points + 1
        computer_points = computer_points + 0
    elif (computer_choice == 't') and (user_choice == 'p'):
        print(emojize(":robot: Computador ganhou!"))
        computer_points = computer_points + 1
    elif (computer_choice == 'p') and (user_choice == 'r'):
        print(emojize(":robot: Computador ganhou!"))
        computer_points = computer_points + 1
    elif (computer_choice == 'r') and (user_choice == 'p'):
        print(emojize(":robot: Computador ganhou!"))
        computer_points = computer_points + 1
    else:
        print(emojize(":robot: Você perdeu!"))
        computer_points = computer_points + 1

    print("-------------------")
    print("Sua pontuação é: " + str(user_points))
    print("Pontuação do computador: " + str(computer_points))
if computer_points > user_points:
    print(emojize(":robot: Derrota!"))
elif computer_points == user_points:
    print(emojize(":robot: Empate"))
else:
    print(emojize(":heart: Vitória!"))

print(emojize(":banana: Goodbye my friend!"))
