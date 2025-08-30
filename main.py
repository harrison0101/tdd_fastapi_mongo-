from fastapi import FastAPI, HTTPException
from models import Usuario
from database import usuarios_collection

app = FastAPI(title="API TDD FastAPI MongoDB", version="1.0")

# Endpoint para cadastrar usuário
@app.post("/usuarios")
async def criar_usuario(usuario: Usuario):
    if usuarios_collection.find_one({"email": usuario.email}):
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")
    usuarios_collection.insert_one(usuario.dict())
    return usuario

# Endpoint para listar todos os usuários
@app.get("/usuarios")
async def listar_usuarios():
    usuarios = list(usuarios_collection.find({}, {"_id": 0}))
    return usuarios
