from utility.funcoes import menu, indice, cadastrar, carregar_json, salvar_json

elenco = carregar_json()

while True:
    menu()
    chave_menu = indice()

    if chave_menu == 1:
            jogador = cadastrar()
            elenco.append(jogador)
            salvar_json(elenco)
            print('Jogador cadastrado com sucesso.')
    elif chave_menu == 2:
        print(elenco)
    elif chave_menu == 3:
        print('EM BREVE')
    elif chave_menu == 4:
        break
    else:
        print("-="*32)
        print('Dígite um índice válido.')