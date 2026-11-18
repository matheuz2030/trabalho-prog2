import json
import os
import random

from cadastro import buscar_usuario
from controle_saldo import obter_saldo, atualizar_saldo

ARQUIVO_APOSTAS = "apostas.json"


def carregar_apostas():
   
    if not os.path.exists(ARQUIVO_APOSTAS):
        return []
    with open(ARQUIVO_APOSTAS, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_apostas(apostas):
  
    with open(ARQUIVO_APOSTAS, "w", encoding="utf-8") as f:
        json.dump(apostas, f, indent=4, ensure_ascii=False)


def apostar():
 
    cpf = input("Digite o CPF do usuário: ").strip()

   
    usuario = buscar_usuario(cpf)
    if usuario is None:
        print("Usuário não encontrado.")
        return

    saldo_atual = obter_saldo(cpf)

    try:
        valor = float(input(f"Saldo disponível: R$ {saldo_atual:.2f}\nDigite o valor da aposta: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    if valor <= 0:
        print("Erro: o valor da aposta deve ser maior que zero.")
        return

    if valor > saldo_atual:
        print("Erro: saldo insuficiente para a aposta.")
        return

    try:
        numero_apostado = int(input("Escolha um número entre 0 e 10: "))
    except ValueError:
        print("Número inválido.")
        return

    if numero_apostado < 0 or numero_apostado > 10:
        print("Erro: o número deve estar entre 0 e 10.")
        return

   
    numero_sorteado = random.randint(0, 10)

    print(f"\n🎰 Número sorteado: {numero_sorteado}")

   
    if numero_apostado == numero_sorteado:
        valor_obtido = valor * 10
        resultado = "ganhou"
        novo_saldo = saldo_atual - valor + valor_obtido
        print(f"🎉 Parabéns! Você GANHOU R$ {valor_obtido:.2f}!")
    else:
        valor_obtido = 0.0
        resultado = "perdeu"
        novo_saldo = saldo_atual - valor
        print(f"😞 Você perdeu R$ {valor:.2f}. Mais sorte na próxima!")

    
    atualizar_saldo(cpf, novo_saldo)
    print(f"Novo saldo: R$ {novo_saldo:.2f}")

    
    apostas = carregar_apostas()
    apostas.append({
        "cpf": cpf,
        "valor_apostado": valor,
        "numero_apostado": numero_apostado,
        "numero_sorteado": numero_sorteado,
        "resultado": resultado,
        "valor_obtido": valor_obtido
    })
    salvar_apostas(apostas)
