from data import combustiveis, vendas
from services import registrar_venda
from reports import gerar_relatorio, exportar_csv

def menu():
    print("\n=== POSTO DE GASOLINA ===")
    print("1 - Vender combustível")
    print("2 - Ver estoque")
    print("3 - Relatório de vendas")
    print("4 - Exportar vendas (CSV)")
    print("0 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            print("\nG - Gasolina | GD - Gasolina Grid | GD - Gasolina Podium | D - Diesel")
            tipo = input("Combustível: ").upper()

            if tipo not in combustiveis:
                print(" Combustível inválido")
                continue

            try:
                litros = float(input("Litros: "))
                valor = registrar_venda(combustiveis[tipo], litros)
                print(f" Venda realizada com sucesso! Valor: R$ {valor:.2f}")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            print("\n📦 ESTOQUE ATUAL")
            for c in combustiveis.values():
                print(f"{c.nome}: {c.estoque:.2f}L")

        elif opcao == "3":
            gerar_relatorio(vendas)

        elif opcao == "4":
            exportar_csv(vendas)

        elif opcao == "0":
            print(" Encerrando sistema")
            break

        else:
            print(" Opção inválida")

if __name__ == "__main__":
    main()


