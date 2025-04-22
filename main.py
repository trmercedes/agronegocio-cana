
import json
from modules.simulador import registrar_colheita, calcular_perda, simular_prejuizo
from modules.arquivos import salvar_json, salvar_txt, carregar_json

# Carrega colheitas anteriores, se existirem
dados = carregar_json('dados/colheitas.json')

print("\n--- SISTEMA DE GESTÃO DE PERDAS NA COLHEITA DE CANA ---")

while True:
    print("\n1. Registrar nova colheita")
    print("2. Exibir colheitas registradas")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        local = input("Local da colheita: ")
        safra = input("Safra (ex: 2024/25): ")
        metodo = input("Método de colheita (manual/mecanizada): ").lower()
        produtividade = float(input("Produtividade (toneladas/hectare): "))
        area = float(input("Área da fazenda (hectares): "))

        colheita = registrar_colheita(local, safra, metodo, produtividade, area)
        perda = calcular_perda(colheita)
        prejuizo = simular_prejuizo(perda, preco_tonelada=250)

        colheita['perda_toneladas'] = perda
        colheita['prejuizo_R$'] = prejuizo
        dados.append(colheita)

        salvar_json('dados/colheitas.json', dados)
        salvar_txt('dados/relatorio.txt', colheita)

        print(f"\n🔍 Perda estimada: {perda:.2f} toneladas")
        print(f"💸 Prejuízo estimado: R$ {prejuizo:.2f}")

    elif opcao == '2':
        print("\n--- COLHEITAS REGISTRADAS ---")
        for item in dados:
            print(f"\nLocal: {item['local']}, Safra: {item['safra']}, Método: {item['metodo']}, Perda: {item['perda_toneladas']:.2f}t, Prejuízo: R$ {item['prejuizo_R$']:.2f}")

    elif opcao == '3':
        print("\nEncerrando sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
