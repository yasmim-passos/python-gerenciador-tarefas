import json
import os
from tarefa import Tarefa

ARQUIVO = "data/tarefas.json"


def garantir_pasta():
    os.makedirs("data", exist_ok=True)


def salvar(tarefas):
    garantir_pasta()
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tarefas], f, indent=4, ensure_ascii=False)


def carregar():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)
        return [Tarefa.from_dict(d) for d in dados]
