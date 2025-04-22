def registrar_colheita(local, safra, metodo, produtividade, area):
    return {
        "local": local,
        "safra": safra,
        "metodo": metodo,
        "produtividade": produtividade,
        "area": area
    }

def calcular_perda(colheita):
    fator_perda = 0.05 if colheita['metodo'] == 'manual' else 0.15
    perda = colheita['produtividade'] * colheita['area'] * fator_perda
    return perda

def simular_prejuizo(perda_toneladas, preco_tonelada):
    return perda_toneladas * preco_tonelada
