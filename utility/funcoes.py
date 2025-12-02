def menu():
    print("-="*32)
    print("INÍCIO".center(64))
    print("-="*32)
    print('''[1] CADASTRAR JOGADOR
[2] LISTA DE JOGADORES
[3] GERAR TIME
[4] SAIR''')
    print("-="*32)


def indice():
    while True:
        try:
            inteiro = int(input('- Digíte o índice que deseja acessar: '))
            return inteiro
        except ValueError:
            print('Digíte um índice válido')
