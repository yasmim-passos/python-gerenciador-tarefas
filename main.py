from tarefa import Tarefa
import storage


def menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")


def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for t in tarefas:
        status = "✔" if t.concluida else "✖"
        print(f"{t.id} - {t.titulo} [{status}]")


def proximo_id(tarefas):
    return max((t.id for t in tarefas), default=0) + 1


def main():
    tarefas = storage.carregar()
    opcao = -1

    while opcao != 0:
        menu()
        opcao = int(input("Opção: "))

        if opcao == 1:
            titulo = input("Título da tarefa: ")
            tarefa = Tarefa(proximo_id(tarefas), titulo)
            tarefas.append(tarefa)
            storage.salvar(tarefas)
            print("Tarefa criada!")

        elif opcao == 2:
            listar(tarefas)

        elif opcao == 3:
            listar(tarefas)
            id_tarefa = int(input("ID da tarefa: "))
            for t in tarefas:
                if t.id == id_tarefa:
                    t.concluir()
                    storage.salvar(tarefas)
                    print("Tarefa concluída!")
                    break

        elif opcao == 4:
            listar(tarefas)
            id_tarefa = int(input("ID da tarefa: "))
            tarefas[:] = [t for t in tarefas if t.id != id_tarefa]
            storage.salvar(tarefas)
            print("Tarefa removida!")

    print("Programa encerrado.")


if __name__ == "__main__":
    main()
