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

@app.post("/roupas")
def adicionar_roupa(nome: str, categoria: str, tamanho: str, cor: str, preco: float, estoque: int):
    funcao.criar_roupa(nome, categoria, tamanho, cor, preco, estoque)
    return {"Mensagem": "Roupa adicionada com sucesso!"}

@app.put("/roupas/{id_roupa}")
def atualizar_roupa(id_roupa: int, novo_preco: float):
    roupa = funcao.buscar_roupa(id_roupa)
    if roupa:
        funcao.atualizar_roupa(id_roupa, novo_preco)
        return {"Mensagem": "Roupa atualizada com sucesso!"}
    else:
        return {"Erro": "Roupa não encontrada."}