import json
import os

def salvar_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_json(caminho):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_txt(caminho, colheita):
    with open(caminho, 'a', encoding='utf-8') as f:
        f.write(f"Local: {colheita['local']}, Safra: {colheita['safra']}, Método: {colheita['metodo']}, ")
        f.write(f"Produtividade: {colheita['produtividade']} t/ha, Área: {colheita['area']} ha, ")
        f.write(f"Perda: {colheita['perda_toneladas']:.2f} t, Prejuízo: R$ {colheita['prejuizo_R$']:.2f}\n")
