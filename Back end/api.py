from fastapi import FastAPI
import funcao

app = FastAPI(title="Loja de Roupas")

@app.get("/")
def home():
    return {"Mensagem": "Bem-vindo à Loja!"}

@app.get("/roupas")
def catalogo():
    roupas = funcao.listar_roupas()
    lista = []
    for roupa in roupas:
        lista.append({
            "id": roupa[0],
            "nome": roupa[1],
            "categoria": roupa[2],
            "tamanho": roupa[3],
            "cor": roupa[4],
            "preco": roupa[5],
            "estoque": roupa[6]
        })
