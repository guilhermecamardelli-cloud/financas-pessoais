import json
import os
from datetime import datetime

ARQUIVO_JSON = "lancamentos.json"
ARQUIVO_TXT = "relatorio.txt"

def carregar():
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de dados. Inicializando lista vazia.")
            return []
    return []

def salvar(lancamentos):
    try:
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(lancamentos, f, indent=4, ensure_ascii=False)
    except IOError:
        print("Erro ao salvar os dados no arquivo.")

def registrar_lancamento(lancamentos):
    print("\n--- REGISTRAR NOVA MOVIMENTAÇÃO ---")
    while True:
        tipo = input("Digite o tipo (receita/despesa): ").strip().lower()
        if tipo in ["receita", "despesa"]:
            break
        print("Entrada inválida! Digite 'receita' ou 'despesa'.")
    while True:
        try:
            valor = float(input("Digite o valor (Ex: 150.50): "))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
    while True:
        categoria = input("Digite a categoria: ").strip().capitalize()
        if categoria:
            break
        print("A categoria não pode estar vazia.")
    
    descricao = input("Digite uma descrição curta: ").strip()
    if not descricao:
        descricao = "Sem descrição"

    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

    novo_lancamento = {
        "data": data_atual,
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
    }

    lancamentos.append(novo_lancamento)
    salvar(lancamentos)
    print("\nMovimentação registrada e salva com sucesso!")

def exibir_extrato(lancamentos):
    print("\n--- EXTRATO DETALHADO ---")
    if not lancamentos:
        print("Nenhum lançamento registrado até o momento.")
        return

    print(f"{'Data':<18} | {'Tipo':<8} | {'Categoria':<15} | {'Valor':<12} | Descrição")
    print("-" * 70)
    for l in lancamentos:
        sinal = "+" if l["tipo"] == "receita" else "-"
        valor_formatado = f"{sinal} R$ {l['valor']:.2f}"
        print(f"{l['data']:<18} | {l['tipo'].capitalize():<8} | {l['categoria']:<15} | {valor_formatado:<12} | {l['descricao']}")

def calcular_saldo(lancamentos):
    total_receitas = sum(l["valor"] for l in lancamentos if l["tipo"] == "receita")
    total_despesas = sum(l["valor"] for l in lancamentos if l["tipo"] == "despesa")
    saldo_total = total_receitas - total_despesas
    return total_receitas, total_despesas, saldo_total

def gerar_relatorio(lancamentos, apenas_retornar_string=False):
    total_receitas, total_despesas, saldo_total = calcular_saldo(lancamentos)

    categorias_resumo = {}
    for l in lancamentos:
        cat = l["categoria"]
        tipo = l["tipo"]
        if cat not in categorias_resumo:
            categorias_resumo[cat] = {"receita": 0.0, "despesa": 0.0}
        categorias_resumo[cat][tipo] += l["valor"]

    linhas = []
    linhas.append("\n=========================================")
    linhas.append("           RESUMO FINANCEIRO             ")
    linhas.append("=========================================")
    linhas.append(f"Total de Receitas: R$ {total_receitas:.2f}")
    linhas.append(f"Total de Despesas: R$ {total_despesas:.2f}")
    linhas.append(f"Saldo Total Atual: R$ {saldo_total:.2f}")
    linhas.append("-----------------------------------------")
    linhas.append("DETALHAMENTO POR CATEGORIA:")

    if not categorias_resumo:
        linhas.append("Nenhuma categoria registrada.")
    else:
        for cat, valores in categorias_resumo.items():
            linhas.append(f"\nCategoria: {cat}")
            if valores["receita"] > 0:
                linhas.append(f"  (+) Receitas: R$ {valores['receita']:.2f}")
            if valores["despesa"] > 0:
                linhas.append(f"  (-) Despesas: R$ {valores['despesa']:.2f}")

    linhas.append("=========================================\n")

    texto_relatorio = "\n".join(linhas)

    if apenas_retornar_string:
        return texto_relatorio
    else:
        print(texto_relatorio)

def exportar_relatorio(lancamentos):
    texto = gerar_relatorio(lancamentos, apenas_retornar_string=True)
    try:
        with open(ARQUIVO_TXT, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"Relatório exportado com sucesso para o arquivo '{ARQUIVO_TXT}'!")
    except IOError:
        print("Erro ao tentar exportar o arquivo de texto.")

def menu():
    print("\n=== APP DE FINANÇAS PESSOAIS ===")
    print("1 - REGISTRAR")
    print("2 - VER EXTRATO")
    print("3 - RELATÓRIO")
    print("4 - EXPORTAR")
    print("5 - SAIR")
    return input("Escolha uma opção (1-5): ").strip()

def main():
    lancamentos = carregar()

    while True:
        opcao = menu()

        if opcao == "1":
            registrar_lancamento(lancamentos)
        elif opcao == "2":
            exibir_extrato(lancamentos)
        elif opcao == "3":
            gerar_relatorio(lancamentos)
        elif opcao == "4":
            exportar_relatorio(lancamentos)
        elif opcao == "5":
            print("\nEncerrando o programa com segurança. Até mais!")
            break
        else:
            print("\nOpção inválida! Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()