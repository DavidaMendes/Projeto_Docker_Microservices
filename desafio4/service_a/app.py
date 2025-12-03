from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Usuario(BaseModel):
    id: int
    name: str
    active: bool
    start_date: str

usuarios_db = [
    {"id": 1, "name": "Davi", "active": True, "start_date": "2024-01-15"},
    {"id": 2, "name": "Maria", "active": True, "start_date": "2024-02-10"},
    {"id": 3, "name": "João", "active": False, "start_date": "2023-11-20"},
]

@app.get("/usuarios")
def getAll() -> List[Usuario]:
    return usuarios_db

@app.get("/usuarios/{usuario_id}")
def findById(usuario_id: int) -> Usuario:
    for usuario in usuarios_db:
        if usuario["id"] == usuario_id:
            return usuario
    return {"error": "Usuário não encontrado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)