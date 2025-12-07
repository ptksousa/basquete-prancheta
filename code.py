import time

from utility.funcoes import menu, indice, cadastrar
from utility.json_funcoes import salvar_json, carregar_json

elenco = carregar_json()

while True:
    menu()
    chave_menu = indice()

    if chave_menu == 1:
            jogador = cadastrar()
            elenco.append(jogador)
            salvar_json(elenco)
            time.sleep(0.5)
            print('Jogador cadastrado com sucesso.')
            time.sleep(1)

    elif chave_menu == 2:
        print("-="*32)
        print("LISTA DE JOGADORES".center(64))
        print("-="*32)
        for i, jogador in enumerate(elenco):
             print(f'[{i}] NOME: {jogador['NOME']}')
             print(f'    IDADE: {jogador['IDADE']}')
             print(f'    POSICAO: {jogador['POSICAO']}')
             print("-"*64)
        input('Pressione ENTER para retornar.')

    elif chave_menu == 3:
        print('EM BREVE')

    elif chave_menu == 4:
        break

    else:
        print("-="*32)
        print('Dígite um índice válido.')