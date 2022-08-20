from turtle import clear


print("***********************************")
print("Bem vindo ao jogo de adivinhação")
print("***********************************")

numero_secreto = 33
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite um número entre 1 e 100")
    print("Você digitou", chute)

    if(int(chute) < 1 or int(chute) > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = numero_secreto == int(chute)
    chute_foi_maior = int(chute) > numero_secreto
    chute_foi_menor = int(chute) < numero_secreto

    if (acertou):
        print("Você acertou!!")
        break
    else:
        if(chute_foi_maior):
            print("Seu chute foi maior que o número secreto!")
        elif(chute_foi_menor):
           print("Seu chute foi menor que o número secreto!")
 
print("Fim de Jogo!!!")

