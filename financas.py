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