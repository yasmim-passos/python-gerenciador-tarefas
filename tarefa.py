class Tarefa:
    def __init__(self, id, titulo, concluida=False):
        self.id = id
        self.titulo = titulo
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "concluida": self.concluida
        }

    @staticmethod
    def from_dict(dados):
        return Tarefa(
            dados["id"],
            dados["titulo"],
            dados["concluida"]
        )
