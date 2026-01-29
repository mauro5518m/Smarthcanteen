import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",  # tua senha do MySQL
        database="smartcanteen"
    )

# teste rápido
if __name__ == "__main__":
    conn = conectar()
    print("Conectado:", conn.is_connected())

