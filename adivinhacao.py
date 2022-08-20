from random import random, randrange


def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("***********************************")
    numero_secreto = randrange(1, 101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível gostaria de jogar?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Digite o nível!"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 3
    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100 \n")
        print("Você digitou", chute)

        if(int(chute) < 1 or int(chute) > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == int(chute)
        chute_foi_maior = int(chute) > numero_secreto
        chute_foi_menor = int(chute) < numero_secreto

        if (acertou):
            print("Você acertou!!")
            print(f"Você fez {pontos} pontos!")
            break
        else:
            if(chute_foi_maior):
                print("Seu chute foi maior que o número secreto!")
            elif(chute_foi_menor):
                print("Seu chute foi menor que o número secreto!")
                pontos_perdidos = abs(numero_secreto - int(chute))
                pontos = pontos - pontos_perdidos


    print("Fim de Jogo!!!")
    print("O número secreto foi {}!! Tente novamente.".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()