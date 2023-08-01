import adivinhacao  # Make sure both files are in the same directory

print("*********************************************************************")
print("************************** Escolha o seu jogo ***********************")
print("*********************************************************************")

print("(1) Força (2) Adivinhação")

jogo = int(input())

if jogo == 1:
    print('Você escolheu "Forca" (o jogo forca ainda não está implementado)')
elif jogo == 2:
    adivinhacao.adivinhacao_game()
else:
    print("Opção inválida. Escolha 1 ou 2 para selecionar um jogo.")
