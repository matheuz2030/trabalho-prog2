from cadastro import cadastrar_usuario
from deposito import depositar
from aposta import apostar
from resgata import resgatar
from controle_saldo import consultar_saldo


def exibir_menu():
  
    print("     🎰  ROLETA UNIRPIX  🎰")

    print("1. Cadastrar usuário")
    print("2. Depositar dinheiro")
    print("3. Realizar aposta")
    print("4. Resgatar saldo")
    print("5. Consultar saldo")
    print("6. Sair")
 


def main():
    """Função principal que controla o fluxo do programa."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- Cadastro de Usuário ---")
            cadastrar_usuario()

        elif opcao == "2":
            print("\n--- Depósito ---")
            depositar()

        elif opcao == "3":
            print("\n--- Aposta ---")
            apostar()

        elif opcao == "4":
            print("\n--- Resgate de Saldo ---")
            resgatar()

        elif opcao == "5":
            print("\n--- Consulta de Saldo ---")
            cpf = input("Digite o CPF do usuário: ").strip()
            consultar_saldo(cpf)

        elif opcao == "6":
            print("\nObrigado por usar a Roleta UNIRPIX! Até mais! 👋")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
