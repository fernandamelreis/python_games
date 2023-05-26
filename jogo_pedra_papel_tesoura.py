import random

user_points = 0
computer_points = 0

options = ['r', 't', 'p'] #lista

while True:

    user_choice = input("Escolha R para Pedra / T para Tesoura / P para Papel ou Q para SAIR:_ ").lower() #transforma a entrada do usuário em minúsculo
    if(user_choice == 'q'):
        break

    if user_choice not in options: #verificando se não está na listagem de opções
        continue

    computer_choice = random.randint(0,2)
    # 0 = R - PEDRA / 1 = T- TESOURA / 2 = P-PAPEL
    computer_option = options[computer_choice]

    print("O computador escolheu " + str(computer_option))

    if user_choice == 't' and computer_choice == 't':
        print("Empate!")
    elif user_choice == 'r' and computer_choice == 'r':
        print("Empate!")
    elif user_choice == 'p' and computer_choice == 'p':
        print("Empate!")
    elif (user_choice == 'r') and (computer_choice == 't'):
        print("Usuário ganhou!")
        user_points = user_points + 1
        computer_points = computer_points + 0
    elif (user_choice == 'p') and (computer_choice == 'r'):
        print("Usuário ganhou!")
        user_points = user_points + 1
        computer_points = computer_points + 0
    elif (user_choice == 't') and (computer_choice == 'p'):
        print("Usuário ganhou!")
        user_points = user_points + 1
        computer_points = computer_points + 0
    elif (computer_choice == 't') and (user_choice == 'p'):
        print("Computador ganhou!")
        computer_points = computer_points + 1
    elif (computer_choice == 'p') and (user_choice == 'r'):
        print("Computador ganhou!")
        computer_points = computer_points + 1
    elif (computer_choice == 'r') and (user_choice == 'p'):
        print("Computador ganhou!")
        computer_points = computer_points + 1
    else:
        print("Você perdeu!")
        computer_points = computer_points + 1

    print("-------------------")
    print("Sua pontuação é: " + str(user_points))
    print("Pontuação do computador: " + str(computer_points))
if computer_points > user_points:
    print("Derrota!!!")
elif computer_points == user_points:
    print("Empate")
else:
    print("Vitória!")

print("Goodbye my friend!")