from fastapi.testclient import TestClient
from gerenciador_tarefas.gerenciador import app, TAREFAS


cliente = TestClient(app)

def test_quando_listar_tarefas_retorna_cod_status_200():
    response = cliente.get("/tarefas")
    assert response.status_code == 200

def test_quando_listar_tarefas_retorna_json():
    cliente = TestClient(app)
    response = cliente.get("/tarefas")
    assert response.headers["Content-Type"] == "application/json"

def test_quando_listar_tarefas_retorna_lista():
    cliente = TestClient(app)
    response = cliente.get("/tarefas")
    assert isinstance(response.json(), list)

def test_quando_listar_tarefas_retorno_deve_possuir_id():
    TAREFAS.append({"id":1})
    cliente = TestClient(app)
    response = cliente.get("/tarefas")
    assert "id" in response.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_titulo():
    TAREFAS.append({"titulo": "titulo 1"})
    cliente = TestClient(app)
    response = cliente.get("/tarefas")
    assert "titulo" in response.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_descricao():
    TAREFAS.append({"descricao": "descricao 1"})
    cliente = TestClient(app)
    response = cliente.get("/tarefas")
    assert "descricao" in response.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_estado():
    TAREFAS.append({"estado": "finalizado"})
    cliente = TestClient(app)
    response = cliente.get("/tarefas")
    assert "estado" in response.json().pop()
    TAREFAS.clear()

def test_para_quando_adicionar_nova_tarefa_retorna_status_200():
    cliente = TestClient(app)
    response = cliente.post(
        "/tarefas",
        json={"id": "4", "titulo": "fazer jantar", "descricao": "cozinhar para 4 adultos", "estado": "não finalizado"}
        )
    assert response.status_code == 200
    TAREFAS.clear()
   