from fastapi import FastAPI,HTTPException
from typing import List
from models import User, Role
from uuid import uuid4, UUID

app = FastAPI()

# criando um banco de dados para manipulação dos usuários
db: List[User] = [
    User(id=UUID('fd959933-c5a8-4ff6-a1bc-5d4290afd8de'),
         first_name="Juliana",
         last_name="Carvalho",
         email="ju@gmail.com",
         role=[Role.role_1]
         ),
    User(id=uuid4(),
         first_name="Kelly",
         last_name="Sylvia",
         email="manu@gmail.com",
         role=[Role.role_2, Role.role_3]
         )
]


@app.get("/")
async def root():
    return {"mensagem": "Olá, Womakers!"}


@app.get("/api/users")
async def get_users():
    return db


@app.get("/api/users/{id}")
async def get_users(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {'message': "Usuário não encontrado"}


@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/users/{id}")
async def remove_user(id:UUID):
    find_user = list(filter(lambda x: x.id == id, db))
    if find_user:
        db.remove(find_user[0])
        return
    raise HTTPException(
        status_code=404, #já trás o protocolo correto.
        detail=f"Usuário com o id {id} não encontrado!"
    )

