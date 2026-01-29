# gestão de refeições
from src.db import conectar


def adicionar(nome, categoria, preco, quantidade_diaria):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO refeicao (nome, categoria, preco, quantidade_diaria) VALUES (%s, %s, %s, %s)",
        (nome, categoria, preco, quantidade_diaria)
    )
    conn.commit()

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM refeicao")
    return cursor.fetchall()

# teste rápido
if __name__ == "__main__":
    adicionar("Sopa do Dia", "Almoço", 200, 30)
    print(listar())
