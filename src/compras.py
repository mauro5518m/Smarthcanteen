# compras de refeições
from src.db import conectar

def comprar(id_estudante, id_refeicao, quantidade=1):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO compra (id_utilizador, id_refeicao, quantidade) VALUES (%s, %s, %s)",
        (id_estudante, id_refeicao, quantidade)
    )
    conn.commit()

# teste rápido
if __name__ == "__main__":
    comprar(1, 1)
    print("compra realisado com sucesso")

