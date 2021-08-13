#Resolução exercício 1 da SA2
#1 - Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista; b) maior valor da lista; c) menor valor da lista; d) soma de todos os elementos da lista;
# e) lista em ordem crescente; f) lista em ordem decrescente.


lista = [5, 7, 2, 9, 4, 1, 3]


#Exercício A
def total_elementos(list):
    count = 0
    for element in list:
        count += 1
    return count

print(f'O tamanho da lista é de: {total_elementos(lista2)} elementos')

#Exercício B
um = 5
dois = 7
tres = 2
quatro = 9
cinco = 4
seis = 1
sete = 3
maior = um
if (dois>maior):
	maior=dois
if (tres>maior):
        maior=tres
if (quatro>maior):
	maior=quatro
if (cinco>maior):
	maior=cinco
if (seis>maior):
	maior=seis
if (sete>maior):
	maior=sete
print('O maior numero da lista é: ', maior)

#Exercício C
um = 5
dois = 7
tres = 2
quatro = 9
cinco = 4
seis = 1
sete = 3
menor = um
if (dois<menor):
	maior=dois
if (tres<menor):
        menor=tres
if (quatro<menor):
	menor=quatro
if (cinco<menor):
	menor=cinco
if (seis<menor):
	menor=seis
if (sete<menor):
	menor=sete
print('O menor numero da lista é:', menor)


#Exercício D
lista1 = [5, 7, 2, 9, 4, 1, 3]
soma = 0
for i in lista1:
    soma = soma + i

print('A soma dos valores da lista é: ', soma)

#Exercício E
primeiro = 5
segundo = 7
terceiro = 2
quarto = 9
quinto = 4
sexto = 1
setimo = 3

if sexto<terceiro<setimo<quinto<primeiro<segundo<quarto:
	print('Lista em ordem crescente',sexto,terceiro,setimo,quinto,primeiro,segundo,quarto)

#Exercício F
if quarto>segundo>primeiro>quinto>setimo>terceiro>sexto:
    print('Lista em ordem decrescente', quarto, segundo, primeiro, quinto, setimo, terceiro, sexto)
