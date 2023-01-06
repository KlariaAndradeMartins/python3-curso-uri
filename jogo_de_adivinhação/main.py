print("Bem vindo no jogo de adivinhação")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range (1,total_de_tentativas + 1):
    print("Tentiva {} de {}".format(rodada,total_de_tentativas))

    chute_str = input("Digite o seu número:")
    print("Você digitou:", chute_str)

    # Conversão para inteiro leitura e sempre string
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    # declarando os criterios
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    else:
        if (maior):
            print("Seu chute foi maior que o número secreto", end="\n")
        elif (menor):
            print("Seu chute foi menor que o número secreto ", end="\n")

print("Fim do jogo", end="\n")