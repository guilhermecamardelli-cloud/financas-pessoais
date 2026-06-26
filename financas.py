import json
import os
from datetime import datetime

ARQUIVO = "lancamentos.json"
ARQUIVO_TXT = "relatorio.txt"

def carregar ():
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(
                "Erro ao ler o arquivo de dados. Inicializando lista vazia."
            )
            return []
    return []

def salvar (lancamentos):
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
