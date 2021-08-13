# 2 - Faça um programa que leia 4 valores, calcule a média e imprima positivo ou negativo
# (para ser positivo a média deve ser acima de 1).

valores = []
for c in range(1, 5):
        valores.append(int(input(f'Digite um valor de 0 a 10= {c}:')))
soma = 0
for i in valores:
   soma += i
soma_valores = soma

media_valores = soma_valores / 4
print('-'*50)
print(f'A média é: {media_valores}')

if media_valores >=7:
    print('Essa média é  acima de 7 = Aprovado')
else:
    print('Essa média é  abaixo de 7 = Reprovado')