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


def atualizar_roupa(id_roupa, novo_preco):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE roupas SET preco = ? WHERE id = ?",
                (novo_preco, id_roupa)
            )
            conexao.commit()
            print("Preço da roupa atualizado com sucesso!")
        except Exception as erro:
            print(f"Erro ao atualizar o preço da roupa: {erro}")
        finally:
            cursor.close()
            conexao.close()


def deletar_roupa(id_roupa):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM roupas WHERE id = ?",
                (id_roupa,)
            )
            conexao.commit()
            print(f"Roupa com ID {id_roupa} deletada com sucesso.")
        except Exception as erro:
            print(f"Erro ao deletar a roupa: {erro}")
        finally:
            cursor.close()
            conexao.close()

def buscar_mroupa(id_roupa):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM movies WHERE id = %s", (id_roupa,)
            )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar:  {erro}")
        finally:
            cursor.close()
            conexao.close()