from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)
app.json.sort_keys = False
#CRUD
#Create, Read, Update e delete = Criar, Ler, Atualizar e deletar
#Tabela: Tarefa

tasks = []
task_id_control = 1

@app.route("/tasks", methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control, titulo=data["titulo"], descricao=data.get("descricao", ""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({'message': "Tarefa concluida com sucesso!"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
  #task_list = [task.info_dicionario() for task in tasks]
  task_list = []
  for task in tasks:
    task_list.append(task.info_dicionario())

  resposta = {                        
    "tasks": task_list,
    "total_tasks": len(task_list)
  }
  return jsonify(resposta)

@app.route("/tasks/<int:id>", methods=['GET'])
def get_task(id):
  for t in tasks:
    if t.id == id:
      return jsonify(t.info_dicionario())
    
  return jsonify({"message": "Nao encontramos a atividade"}), 404

@app.route("/tasks/<int:id>", methods=['PUT'])
def update_task(id):
  task = None
  for tarefa in tasks:
    if tarefa.id == id:
      task = tarefa
  print(task)
  if task == None:
    return jsonify({"message": "Tarefa nao encontrada"}), 404

  data = request.get_json()
  task.titulo = data['titulo']
  task.descricao = data['descricao']
  task.completa = data['completa']
  print(task)
  return jsonify({"message": "Tarefa atualizada com sucesso!"})

@app.route("/tasks/<int:id>", methods=['DELETE'])
def delete_tasks(id):
  task = None
  for tarefa in tasks:
    if tarefa.id == id:
      task = tarefa
      break

  if not task:
    return jsonify({"message": "Tarefa nao encontrada"}), 404
  
  tasks.remove(task)
  return jsonify({"message": "Tarefa deletada com sucesso!"})

if __name__ == "__main__":
  app.run(debug=True)