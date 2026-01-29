# carregamento de saldo
from src.db import conectar


def carregar_saldo(id_estudante, valor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO carregamento (id_utilizador, valor) VALUES (%s, %s)",
        (id_estudante, valor)
    )
    cursor.execute(
        "UPDATE utilizador SET saldo = saldo + %s WHERE id = %s",
        (valor, id_estudante)
    )
    conn.commit()

# teste rápido
if __name__ == "__main__":
    carregar_saldo(1, 500)
    print("Saldo carregado com sucesso para o estudante ID 1")
