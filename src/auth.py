# autenticação de funcionários
from src.db import conectar

def login(email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM utilizador WHERE email=%s AND tipo='funcionario'",
        (email,)
    )
    return cursor.fetchone()

# teste rápido
if __name__ == "__main__":
    usuario = login("admin@um.edu.cv")
    if usuario:
        print("Login com sucesso:", usuario)
    else:
        print("Login falhou")
