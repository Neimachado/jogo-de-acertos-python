print("***********************************")
print("Bem vindo ao jogo de adivinhação")
print("***********************************")

numero_secreto = 33
total_de_tentativas = 3
rodada = 1


while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite um valor")
    print("Você digitou", chute)

    acertou = numero_secreto == int(chute)
    chute_foi_maior = int(chute) > numero_secreto
    chute_foi_menor = int(chute) < numero_secreto

    if (acertou):
        print("Você acertou!!")
    else:
        if(chute_foi_maior):
            print("Seu chute foi maior que o número secreto!")
        elif(chute_foi_menor):
           print("Seu chute foi menor que o número secreto!")
    rodada = rodada + 1

print("Fim de Jogo!!")