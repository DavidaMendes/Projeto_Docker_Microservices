from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Usuario(BaseModel):
    id: int
    name: str
    email: str

usuarios_db = [
    {"id": 1, "name": "Davi Silva", "email": "davi@example.com"},
    {"id": 2, "name": "Maria Santos", "email": "maria@example.com"},
    {"id": 3, "name": "João Oliveira", "email": "joao@example.com"},
]

@app.get("/health")
def healthCheck():
    return {"status": "healthy", "component": "service_users"}

@app.get("/usuarios")
def getAllUsuarios() -> List[Usuario]:
    return usuarios_db

@app.get("/usuarios/{usuario_id}")
def getUsuario(usuario_id: int) -> Usuario:
    for usuario in usuarios_db:
        if usuario["id"] == usuario_id:
            return usuario
    return {"error": "Usuário não encontrado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)