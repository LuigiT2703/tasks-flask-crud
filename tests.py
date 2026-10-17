import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
task_list = []

def test_create_task():
  nova_task = {
    "titulo": "Miranha",
    "descricao": "joga bola"
  }
  response = requests.post(f"{BASE_URL}/tasks", json=nova_task)
  assert response.status_code == 200
  response_json = response.json()
  assert "message" in response_json
  assert "id" in response_json
  task_list.append(response_json["id"])

def test_get_tasks():
  response = requests.get(f"{BASE_URL}/tasks")
  assert response.status_code == 200
  response_json = response.json()
  assert "tasks" in response_json
  assert "total_tasks" in response_json

def test_get_task():
  if task_list:
    task_id = task_list[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json['id']

def test_update_task():
  if task_list:
    task_id = task_list[0]
    payload = {
    "titulo": "cagar com a tropa",
    "descricao": "oi",
    "completa": True
}
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
    response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

    #Nova requisicao para tarefas especificas
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['titulo'] == payload["titulo"]
    assert response_json['descricao'] == payload["descricao"]
    assert response_json['completa'] == payload["completa"]

def test_delete_task():
  if task_list:
    task_id = task_list[0]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200

    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 404
