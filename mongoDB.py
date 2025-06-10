from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['meu_banco']
colecao = db['minha_colecao']

documento = {
    "nome": "Thomas Sievers",
    "idade": 18,
    "profissao": "Desenvolvedor"
}

resultado = colecao.insert_one(documento)
print("Documento inserido com o ID: ", resultado.inserted_id)

documentos = [
    {"nome": "Ana", "Idade": 25, "profissao": "Engenharia"},
    {"nome": "Carlos", "Idade": 40, "Profissao": "Arquiteto"}
]

resultado2 = colecao.insert_many(documentos)
print("IDs dos documentos inseridos: ", resultado2.inserted_ids)

documento_find_one = colecao.find_one({"nome": "Thomas Sievers"})
print("Documento encontrado:", documento_find_one)

documento_find = colecao.find({"idade": {"$gt": 18}})
for doc in documento_find:
    print(doc)

resultado_update = colecao.update_one(
    {"nome": "Thomas Sievers"}, #Filtro
    {"$set": {"idade": 31}}  #Atualização
)
print("Número de documentos modificados:", resultado_update.modified_count)

resultado_update_many = colecao.update_many(
    {"idade": {"$lt": 30}},
    {"$set": {"status": "jovem"}}
)
print("Número de documentos modificados:", resultado_update_many.modified_count)

resultado_delete = colecao.delete_one({"nome": "Thomas Sievers"})
print("Número de documentos deletados:", resultado_delete.deleted_count)

resultado_delete_many = colecao.delete_many({"Idade": {"$lt": 30}})
print("Número de documentos deleteados", resultado_delete_many.deleted_count)

projecao = {"_id": 0, "nome": 1, "idade": 1}
resultados_find = colecao.find({}, projection=projecao)
for doc in resultados_find:
    print(doc)