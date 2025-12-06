import json

ARQUIVO = "elenco.json"

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


def cadastrar():
    print("-="*32)
    print("CADASTRO DE JOGADOR".center(64))
    print("-="*32)
    nome = input('Digíte o primeiro nome do jogador: ').upper().strip()
    sobrenome = input('Digíte o último nome do jogador: ').upper().strip()
    nome_completo = nome + ' ' + sobrenome
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
        "NOME" : nome_completo,
        "IDADE" : idade,
        "POSICAO" : posicao
        } 
    return jogador


def carregar_json():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as open_file:
            return json.load(open_file)
    except:
        return []


def salvar_json(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as write_file:
        json.dump(dados, write_file, indent=4, ensure_ascii=False)
    