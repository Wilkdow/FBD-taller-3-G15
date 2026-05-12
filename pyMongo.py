import pymongo as pm
from pymongo.collection import Collection
from pymongo import MongoClient
from datetime import datetime

COMENTARIOS_COLLECTION_NAME = "Comentarios"
EVENTOS_COLLECTION_NAME = "Eventos"

def setup_db():
    client = MongoClient("mongodb://ISIS2304J10202610:x227wa7zbJ1v@157.253.236.88:8087/")
    db = client['ISIS2304J10202610']
    return db

def setup_mongo_constraints(db):
    validator_comments = {
        "$jsonSchema": {
            "required": ["bar_id", "date", "texto", "autor"],
            "properties": {
                "bar_id": {
                    "bsonType": "int"
                },
                "texto": {
                    "bsonType": "string",
                    "minLength": 1
                },
                "autor": {
                    "bsonType": "string",
                    "minLength": 1
                },
                "date": {
                    "bsonType": "date"
                }
            },
            "additionalProperties": False
        }
    }
    
    validator_eventos = {
        "$jsonSchema": {
            "required": ["bar_id", "nombre"],
            "properties": {
                "bar_id": {
                    "bsonType": "int"
                },
                "nombre": {
                    "bsonType": "string",
                    "minLength": 1
                }
            },
            "additionalProperties": True
        }
    }
    db.command("collMod", COMENTARIOS_COLLECTION_NAME, validator= validator_comments)
    db.command("collMod", EVENTOS_COLLECTION_NAME, validator= validator_eventos)

def print_documents(collection: Collection):
    print(f"Elementos de {collection.name}:\n")
    for document in collection.find({}):
        print(document)
        
def add_comment(bar_id: int, texto: str, date: datetime, autor: str = "Anonimo"):
    document = {
        "bar_id": bar_id,
        "texto": texto,
        "date": date,
        "autor": autor
    }
    comentarios.insert_one(document)
    
def add_evento(bar_id: int, nombre: str, **kargs):
    document = {
        "bar_id": bar_id,
        "nombre": nombre
    }
    document.update(kargs)
    
    eventos.insert_one(document)

db = setup_db()
comentarios = db[COMENTARIOS_COLLECTION_NAME]
eventos = db[EVENTOS_COLLECTION_NAME]

print_documents(comentarios)
print_documents(eventos)