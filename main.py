from random import randint
from time import sleep
from emoji import emojize


print("~~" * 20)
print("          JOGO DE ADIVINHAÇÃO")
print("~~" * 20)
sleep(1)


computador = randint(0,10)

print(emojize(":robot: Olá, sou o seu pc e pense em um número de 0 à 10"))
sleep(2)
print(emojize(":robot: Será que você consegue adivinhar? "))
sleep(1)

acertou = False
palpite = 0

while not acertou:
    jogador = int(input(emojize(":robot: Digite o valor do seu palpite: ")))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(emojize(":robot: Hum... Mais..."))
        elif jogador > computador:
            print(emojize(":robot: Hum... Menos..."))

if palpite <= 2:
    print(emojize(f":robot: Parabéns! Você acertou com {palpite} palpites."))
elif (palpite == 3) or (palpite == 4) or (palpite == 5):
    print(emojize(f":robot: Acertou com {palpite} palpites"))
    
elif (palpite >= 6):
    print(emojize(f":robot: Muito lento. Você demorou {palpite} palpites para acertar. Hahaha"))
