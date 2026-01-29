# gestão de estudantes
from src.db import conectar

def adicionar(nome, numero, curso, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO utilizador (tipo, nome, numero, curso_departamento, email, saldo) "
        "VALUES ('estudante', %s, %s, %s, %s, 0)",
        (nome, numero, curso, email)
    )
    conn.commit()

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utilizador WHERE tipo='estudante'")
    return cursor.fetchall()

# teste rápido
if __name__ == "__main__":
    adicionar("João Silva", "E001", "Engenharia", "joao@um.edu.cv")
    print(listar())
