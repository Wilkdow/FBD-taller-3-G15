import os
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

COMENTARIOS_COLLECTION_NAME = "Comentarios"
EVENTOS_COLLECTION_NAME = "Eventos"

MONGO_URI = os.environ["MONGO_URI"]
MONGO_DB_NAME = os.environ["MONGO_DB_NAME"]

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

comentarios = db[COMENTARIOS_COLLECTION_NAME]
eventos = db[EVENTOS_COLLECTION_NAME]


def serializar_documento(doc):
    doc["_id"] = str(doc["_id"])
    return doc


@app.get("/")
def inicio():
    return {"estado": "API funcionando correctamente"}


@app.get("/bares/{bar_id}/comentarios")
def get_comentarios(bar_id: int):
    resultado = comentarios.find({"bar_id": bar_id})
    return [serializar_documento(c) for c in resultado]


@app.post("/bares/{bar_id}/comentarios")
def post_comentario(bar_id: int, datos: dict):
    documento = {
        "bar_id": bar_id,
        "texto": datos["texto"],
        "autor": datos.get("autor", "Anonimo"),
        "date": datetime.now().isoformat()
    }

    comentarios.insert_one(documento)
    return {"mensaje": "Comentario guardado"}


@app.get("/bares/{bar_id}/eventos")
def get_eventos(bar_id: int):
    resultado = eventos.find({"bar_id": bar_id})
    return [serializar_documento(e) for e in resultado]


@app.post("/bares/{bar_id}/eventos")
def post_evento(bar_id: int, datos: dict):
    documento = {
        "bar_id": bar_id,
        "nombre": datos["nombre"]
    }

    for campo, valor in datos.items():
        if campo not in documento:
            documento[campo] = valor

    eventos.insert_one(documento)
    return {"mensaje": "Evento guardado"}