projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['daniela', 'serafim', 'soares', 'danidinha']
anos = [1996, 2024]

def mostrar_projetos():
    for projeto in projetos:
        if projeto:
            print(f'Projeto: {projeto}')
        else:
            print('Projeto não disponível.')

def mostrar_encomendas():
    encomendas = input('Digite os números das encomendas separados por vírgula: ').split(',')
    try:
        for encomenda in encomendas:
            print(int(encomenda))
    except ValueError:
        print('Uma das entradas não é um número válido.')

def mostrar_lista():
    arr = ['\ncrie', 1, 'lista', 'e', 'utilize', 1, 'loop', 'for', 'para', 'percorrer', 'todos', 'os', 'elementos', 'da', 'lista']

    for i in arr:
        print(i)

def soma_impares():
    resultado = 0
    for numero in numeros:
        if (numero % 2 != 0):
            resultado += numero
    print("a soma dos numeros impares é: ", resultado)

def reorganizar_lista():
    numeros.sort(reverse=True)
    print(numeros)
    numeros.sort()

def tabuada(x):
    for numero in numeros:
        print (f'{x} x {numero} = {numero * x}')

def mostrar_soma():
    soma = 0
    novos_numeros = [23, 21, 43, 42]
    for numero in novos_numeros:
        soma += numero
    print("a soma de todos os numeros é: ", soma)

def mostrar_media():
    aux = 0
    
    try:
        for numero in numeros:
            aux += numero
            
        print('a média é: ', aux/len(numeros))
        print(aux)
    except ZeroDivisionError:
        print('Divisao por zero nao existe')

def atualizar_livro():
    livro = {
        'titulo':'Aprendendo Python',
        'autor' : 'Frabrícico Silva',
        'ISBN' : '12345',
        'preco' : 59.90,
        'em_estoque':True

    }
    
    print(livro)
    livro['preco'] = 69.90
    print(livro)

atualizar_livro()
mostrar_projetos()
mostrar_encomendas()
mostrar_lista()
soma_impares()
reorganizar_lista()
x = int(input('\nInforme o numero que você deseja a tabuada: '))
tabuada(x)
mostrar_soma()
mostrar_media()