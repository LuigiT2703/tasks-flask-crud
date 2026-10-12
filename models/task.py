class Task:
  def __init__(self, id, titulo, descricao, completa=False):
    self.id = id
    self.titulo = titulo
    self.descricao = descricao
    self.completa = completa

  def info_dicionario(self):
    return {
      "id": self.id,
      "titulo": self.titulo,
      "descricao": self.descricao,
      "completa": self.completa
    }