def menu():
    print("-="*32)
    print("INÍCIO".center(64))
    print("-="*32)
    print('''[1] CADASTRAR JOGADOR
[2] LISTA DE JOGADORES
[3] GERAR TIME
[4] SAIR''')
    print("-="*32)

def inteiro(prompt="Digite um número: "):
    while True:
        try:
            resultado = int(input(prompt))
            return resultado
        except ValueError:
            print('Digíte um valor válido.') 
        

i = inteiro("Selecione um índice: ")
print(i)

def indice():
    while True:
        try:
            inteiro = int(input('- Digíte o índice que deseja acessar: '))
            return inteiro
        except ValueError:
            print('Digíte um índice válido')


def cadastrar():
    print("-="*32)
    print("CADASTRO DE JOGADOR".center(64))
    print("-="*32)

    nome = input('Digíte o primeiro nome do jogador: ').upper().strip()
    sobrenome = input('Digíte o último nome do jogador: ').upper().strip()

    while True:
        try:
            idade = int(input('Digíte a idade do jogador: '))
            break
        except ValueError:
            print('!!!Digíte uma idade válida!!!')

    posicoes = ['ARMADOR', 'ALA-ARMADOR', 'ALA', 'ALA-PIVÔ', 'PIVÔ']

    for i, posicao in enumerate(posicoes):
        print(f'[{i}] {posicao}')

             
    posicao_escolha = indice()
    posicao = posicoes[posicao_escolha]

    jogador = {
        "NOME" : nome,
        "SOBRENOME" : sobrenome,
        "IDADE" : idade,
        "POSICAO" : posicao
        } 
    
    return jogador

def lista_jogadores(lista):
        print("-="*32)
        print("LISTA DE JOGADORES".center(64))
        print("-="*32)
        for i, jogador in enumerate(lista):
             print(f'[{i}] NOME COMPLETO: {jogador['NOME']} {jogador['SOBRENOME']}')
             print(f'    IDADE: {jogador['IDADE']}')
             print(f'    POSICAO: {jogador['POSICAO']}')
             print("-"*64)
        input('Pressione ENTER para retornar.')