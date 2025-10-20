from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS roupas (
                    id SERIAL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    tamanho TEXT NOT NULL,
                    cor TEXT NOT NULL,
                    preco REAL NOT NULL,
                    estoque INTEGER NOT NULL
                )
            """)
            conexao.commit()
            print("Tabela 'roupas' criada com sucesso.")
        except Exception as erro:
            print(f"Erro ao criar a tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()