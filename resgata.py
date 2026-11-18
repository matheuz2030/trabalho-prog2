import json
import os

from cadastro import buscar_usuario
from controle_saldo import obter_saldo, atualizar_saldo

ARQUIVO_SAQUES = "saques.json"


def carregar_saques():
   
    if not os.path.exists(ARQUIVO_SAQUES):
        return []
    with open(ARQUIVO_SAQUES, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_saques(saques):
    
    with open(ARQUIVO_SAQUES, "w", encoding="utf-8") as f:
        json.dump(saques, f, indent=4, ensure_ascii=False)


def resgatar():
   
    cpf = input("Digite o CPF do usuário: ").strip()

    usuario = buscar_usuario(cpf)
    if usuario is None:
        print("Usuário não encontrado.")
        return

    saldo_atual = obter_saldo(cpf)

    try:
        valor = float(input(f"Saldo disponível: R$ {saldo_atual:.2f}\nDigite o valor do resgate: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    if valor <= 0:
        print("Erro: o valor do resgate deve ser maior que zero.")
        return

    if valor > saldo_atual:
        print("Erro: saldo insuficiente para o resgate.")
        return

    novo_saldo = saldo_atual - valor
    atualizar_saldo(cpf, novo_saldo)


    saques = carregar_saques()
    saques.append({
        "cpf": cpf,
        "valor_saque": valor
    })
    salvar_saques(saques)

    print(f"Resgate de R$ {valor:.2f} realizado com sucesso!")
    print(f"Novo saldo: R$ {novo_saldo:.2f}")
