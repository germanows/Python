import random

def inicializa_letras(palavra_secreta):
    
    return ["_" for letra in palavra_secreta]

def jogar():

    mensagem_abertura()
    palavra_secreta = vagabunda()
    letras_acertadas = inicializa_letras(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    
    while (not enforcou and not acertou):

        chute = bicuda()

        if(chute in palavra_secreta):
            bicuda_certeira(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas                
        print(letras_acertadas)
    if(acertou):
        print("boa filha da puta!!!!!!!!!!!!!!")
    else:
        print("errou feio seu burro kkkkkkkkk")   


if(__name__ == "__main__"):
    jogar()

def mensagem_abertura():

    print("\n*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

def vagabunda():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    arquivo.close()    

    rando = random.randrange(0,len(palavras))
    palavra_secreta = palavras[rando].upper()
    return palavra_secreta

def bicuda():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return bicuda

def bicuda_certeira(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
            index += 1