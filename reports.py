import pandas as pd

def gerar_relatorio(vendas):
    if not vendas:
        print("Nao existem vendas registradas.")
        return
    
    df = pd.DataFrame(vendas)

    print("\n Relatporio completo das vendas")
    print(df)

    print("\n Total vendido por combustivel: ")
    print(df.groupby("combustivel")["valor"].sum())

    print(f"\n Total: R$ {df['valor'].sum():.2f}")

def exportar_csv(vendas):
    df = pd.DataFrame(vendas)
    df.to_csv("vendas_posto,csv", index=False)
    print("CSV gerado com sucesso")

