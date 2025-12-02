from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    content: str

@app.post("/message")
def receive(msg: Msg):
    print(f"Mensagem recebida: {msg.content}")
    return {"ok": True, "received": msg.content}
