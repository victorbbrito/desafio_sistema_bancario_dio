class Cliente():
    def __init__(self, nome, cpf):
      self.nome = nome
      self.cpf = cpf

    def __str__(self) -> str:
       return f"Nome: {self.nome}\nCPF: {self.cpf}"

    def __repr__(self) -> str:
       return f"Cliente <{self.nome}>"


    