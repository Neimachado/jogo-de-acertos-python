import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")
    jogo1 = input("Digite 1 para Forca e 2 para Adivinhacao!! \n")
    
    if  jogo1.isnumeric() == False or int(jogo1) < 1 or int(jogo1) > 2 or jogo1 == "":
        print("Você deve digitar um número entre 1 e 2")
        escolhe_jogo()
    jogo = int(jogo1)

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar() 
        
if(__name__ == "__main__"):
    escolhe_jogo()
    