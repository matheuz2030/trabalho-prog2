import json
import os

ARQUIVO_CADASTRO = "cadastro.json"


def carregar_cadastros():
   
    if not os.path.exists(ARQUIVO_CADASTRO):
        return []
    with open(ARQUIVO_CADASTRO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_cadastros(cadastros):
    
    with open(ARQUIVO_CADASTRO, "w", encoding="utf-8") as f:
        json.dump(cadastros, f, indent=4, ensure_ascii=False)


def buscar_usuario(cpf):
    
    cadastros = carregar_cadastros()
    for usuario in cadastros:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def cadastrar_usuario():
   
    nome = input("Digite o nome do usuário: ").strip()
    cpf = input("Digite o CPF (somente números): ").strip()

    if not cpf:
        print("CPF não pode ser vazio.")
        return

   
    if buscar_usuario(cpf) is not None:
        print("Erro: CPF já cadastrado no sistema.")
        return

    cadastros = carregar_cadastros()
    novo_usuario = {
        "nome": nome,
        "cpf": cpf,
        "saldo": 0.0
    }
    cadastros.append(novo_usuario)
    salvar_cadastros(cadastros)
    print(f"Usuário {nome} cadastrado com sucesso!")
