from cadastro import carregar_cadastros, salvar_cadastros


def consultar_saldo(cpf):
    """Consulta e exibe o saldo de um usuário a partir do CPF."""
    cadastros = carregar_cadastros()
    for usuario in cadastros:
        if usuario["cpf"] == cpf:
            print(f"Saldo de {usuario['nome']}: R$ {usuario['saldo']:.2f}")
            return usuario["saldo"]
    print("Usuário não encontrado.")
    return None


def atualizar_saldo(cpf, novo_saldo):
    """Atualiza o saldo de um usuário identificado pelo CPF."""
    cadastros = carregar_cadastros()
    for usuario in cadastros:
        if usuario["cpf"] == cpf:
            usuario["saldo"] = novo_saldo
            salvar_cadastros(cadastros)
            return True
    return False


def obter_saldo(cpf):
    """Retorna o saldo do usuário sem exibir na tela. Retorna None se não encontrado."""
    cadastros = carregar_cadastros()
    for usuario in cadastros:
        if usuario["cpf"] == cpf:
            return usuario["saldo"]
    return None
