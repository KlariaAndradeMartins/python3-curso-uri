linha1 = input().split(' ')
linha2 = input().split(' ')

cdg1, qtd1, valor1 = linha1
cdg2, qtd2, valor2 = linha2

total = ((int(qtd1) * float(valor1)) + int(qtd2) * float(valor2))

print(f'VALOR A PAGAR: R$ {total:.2f}')