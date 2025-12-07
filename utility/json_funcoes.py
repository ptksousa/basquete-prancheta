import json

ARQUIVO = "elenco.json"

def carregar_json():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as open_file:
            return json.load(open_file)
    except:
        return []


def salvar_json(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as write_file:
        json.dump(dados, write_file, indent=4, ensure_ascii=False)
    