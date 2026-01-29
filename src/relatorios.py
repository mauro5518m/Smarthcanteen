from src.db import conectar


def refeicoes_mais_vendidas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.nome, COUNT(*) 
        FROM compra c JOIN refeicao r ON c.id_refeicao = r.id
        GROUP BY r.nome
        ORDER BY COUNT(*) DESC
    """)
    return cursor.fetchall()

# teste rápido
if __name__ == "__main__":
    print(refeicoes_mais_vendidas())


