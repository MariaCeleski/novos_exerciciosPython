#4 Crie uma função para desenhar uma linha, usando o caractere '_' (underline).
# O tamanho da linha deve ser definido na chamada da função.

def imprime_linha():
    print('_' * 50)

imprime_linha()
print('FUNÇÃO COM O TAMANHO DA LINHA')
imprime_linha()

alternativa ='SIM'

while alternativa == 'SIM':
    quantidade= int(input('Qual a quantidade de linhas?'))
    print('linhas',quantidade*'-')
    alternativa=str(input('Quer continuar?sim ou não?')).upper()

imprime_linha()
print('Fim da Função - byeeeeeeeeeeee')
imprime_linha()


