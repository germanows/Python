def jogar():

    enforcou = False
    acertou = False
    erros = 0

    print("\n*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    print(chute)
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas                
        print(letras_acertadas)
    if(acertou):
        print("boa filha da puta!!!!!!!!!!!!!!")
    else:
        print("errou feio seu burro kkkkkkkkk") 
    print("Fim do Jogo")    


if(__name__ == "__main__"):
    jogar()