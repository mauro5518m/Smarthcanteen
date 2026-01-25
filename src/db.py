import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # se tu definiste senha, coloca aqui
        database="smartcanteen"
    )

# teste de conexão
if __name__ == "__main__":
    conn = conectar()
    print("Conectado:", conn.is_connected())

