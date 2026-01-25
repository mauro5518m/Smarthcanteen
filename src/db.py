import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="12345",  # se tu definiste senha, coloca aqui
        database="localhost"
    )

# teste de conexão
if __name__ == "__main__":
    conn = conectar()
    print("Conectado:", conn.is_connected())

