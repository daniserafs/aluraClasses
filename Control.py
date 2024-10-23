projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']

for projeto in projetos:
    if projeto:
        print(f'Projeto: {projeto}')
    else:
        print('Projeto não disponível.')

encomendas = input('Digite os números das encomendas separados por vígula: ').split(',')
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print('Uma das entradas não é um número válido.')


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['daniela', 'serafim', 'soares', 'danidinha']
anos = [1996, 2024]

arr = ['\ncrie', 1, 'lista', 'e', 'utilize', 1, 'loop', 'for', 'para', 'percorrer', 'todos', 'os', 'elementos', 'da', 'lista']

for i in arr:
    print(i)

resultado = 0
for numero in numeros:
    if (numero % 2 != 0):
        resultado += numero
print("a soma dos numeros impares é: ", resultado)

numeros.sort(reverse=True)
print(numeros)
numeros.sort()

def tabuada(x):
    for numero in numeros:
        print (f'{x} x {numero} = {numero * x}')

x = int(input('Informe o numero que você deseja a tabuada: '))
tabuada(x)