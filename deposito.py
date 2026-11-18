import json
import os

from cadastro import buscar_usuario
from controle_saldo import obter_saldo, atualizar_saldo

ARQUIVO_DEPOSITOS = "depositos.json"


def carregar_depositos():
  
    if not os.path.exists(ARQUIVO_DEPOSITOS):
        return []
    with open(ARQUIVO_DEPOSITOS, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_depositos(depositos):
    
    with open(ARQUIVO_DEPOSITOS, "w", encoding="utf-8") as f:
        json.dump(depositos, f, indent=4, ensure_ascii=False)


def depositar():
    
    cpf = input("Digite o CPF do usuário: ").strip()

   
    usuario = buscar_usuario(cpf)
    if usuario is None:
        print("Usuário não encontrado.")
        return

    try:
        valor = float(input("Digite o valor do depósito: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    if valor <= 0:
        print("Erro: o valor do depósito deve ser maior que zero.")
        return

  
    saldo_atual = obter_saldo(cpf)
    novo_saldo = saldo_atual + valor
    atualizar_saldo(cpf, novo_saldo)   
    depositos = carregar_depositos()
    depositos.append({
        "cpf": cpf,
        "valor_deposito": valor
    })
    salvar_depositos(depositos)

    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    print(f"Novo saldo: R$ {novo_saldo:.2f}")
