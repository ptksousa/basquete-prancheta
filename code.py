from utility.funcoes import menu, indice, cadastrar

elenco = []

while True:
    menu()
    chave_menu = indice()

    if chave_menu == 1:
            jogador = cadastrar()
            elenco.append(jogador)
            json = "elenco.json"
            with open(json, mode="a") as open_file:
                 cadastrando = open_file.write(elenco)
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