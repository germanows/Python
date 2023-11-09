import forca
import projetinho

print("*********************************")
print("******Escolha o seu Jogo!********")
print("*********************************")

print("(1) - Forca (2) - Adivinhação")

jogo = int(input("Qual jogo?"))

if (jogo == 1):
    print("\nJogando Forquinha\n")
    forca.jogar()
elif(jogo == 2):
    print("\nJogando adivinhaçãozinha\n")
    projetinho.jogar()

