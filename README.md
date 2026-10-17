# Tasks Flask CRUD

API REST simples de tarefas (CRUD) feita com Python e Flask, como estudo no curso "Desenvolvimento de APIs com Flask" da Rocketseat.

## Tecnologias

- Python
- Flask
- Pytest + Requests (testes)
- Postman (testes manuais)

## Como rodar

1. Clone o repositório:

```bash
https://github.com/LuigiT2703/tasks-flask-crud.git
cd tasks-flask-crud
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie a API:

```bash
python app.py
```

A API sobe em `http://127.0.0.1:5000`.

## Rotas

| Método | Rota           | Descrição                  |
|--------|----------------|----------------------------|
| POST   | `/tasks`       | Cria uma tarefa            |
| GET    | `/tasks`       | Lista todas as tarefas     |
| GET    | `/tasks/<id>`  | Busca uma tarefa pelo id   |
| PUT    | `/tasks/<id>`  | Atualiza uma tarefa        |
| DELETE | `/tasks/<id>`  | Remove uma tarefa          |

### Exemplo de body (POST e PUT)

```json
{
  "titulo": "Estudar Flask",
  "descricao": "Terminar o módulo 4",
  "completa": false
}
```

O `id` é gerado pelo servidor.

## Testes

Com a API rodando, em outro terminal:

```bash
pytest tests.py
```

## Observações

- Os dados ficam apenas na memória: ao reiniciar o Flask, a lista de tarefas é zerada.
- Projeto de estudo, sem banco de dados.