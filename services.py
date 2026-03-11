from data import vendas

def registrar_venda(combustivel, litros):
    valor = combustivel.vendas(litros)

    vendas.append({
        "combustivel": combustivel.nome,
        "litros": litros,
        "valor": valor
    })

    return valor