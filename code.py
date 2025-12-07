import time

from utility.funcoes import menu, indice, cadastrar, lista_jogadores
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
        lista_jogadores(elenco)

    elif chave_menu == 3:
        print("-="*32)
        print('EM BREVE')
        time.sleep(1)

    elif chave_menu == 4:
        break

    else:
        print("-="*32)
        print('Dígite um índice válido.')