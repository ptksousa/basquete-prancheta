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
        

def cadastrar():
    print("-="*32)
    print("CADASTRO DE JOGADOR".center(64))
    print("-="*32)

    nome = input('Digíte o primeiro nome do jogador: ').upper().strip()
    sobrenome = input('Digíte o último nome do jogador: ').upper().strip()

    idade = inteiro("Digíte a idade do jogador: ")

    posicoes = ['ARMADOR', 'ALA-ARMADOR', 'ALA', 'ALA-PIVÔ', 'PIVÔ']

    for i, posicao in enumerate(posicoes):
        print(f'[{i}] {posicao}')

    while True:
        posicao_escolha = inteiro("Escolha o índice da posição do jogador: ")
        try:
            posicao = posicoes[posicao_escolha]
            break
        except IndexError:
            print('Digíte o índice de uma posição existente.')

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