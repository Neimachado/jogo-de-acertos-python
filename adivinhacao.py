from random import random, randrange
import menu


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
    elif(nivel == 3):
        total_de_tentativas = 3
    else:
        print("Entrada inválida, digite outra opção.")
        jogar()
    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100 \n")
        print("Você digitou", chute)
   
        if int(chute) < 1 or int(chute) > 100:
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
    print("O número secreto foi {}.".format(numero_secreto))
    voltar_ao_menu = int(input("Digite 1 para voltar ao menu."))
    voltar_ao_menu = input("Digite uma tecla para voltar ao menu!")
    if voltar_ao_menu == 1:
        menu.escolhe_jogo()
    else:
        menu.escolhe_jogo()

if(__name__ == "__main__"):
    jogar()