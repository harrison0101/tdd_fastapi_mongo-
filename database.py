from pymongo import MongoClient

# Conexão simples com MongoDB local
client = MongoClient("mongodb://localhost:27017")
db = client["tdd_fastapi_db"]
usuarios_collection = db["usuarios"]
