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


def criar_roupa(nome, categoria, tamanho, cor, preco, estoque):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                INSERT INTO roupas (nome, categoria, tamanho, cor, preco, estoque)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (nome, categoria, tamanho, cor, preco, estoque))
            conexao.commit()
            print("Roupa adicionada com sucesso!")
        except Exception as erro:
            print(f"Erro ao adicionar roupa: {erro}")
        finally:
            cursor.close()
            conexao.close()