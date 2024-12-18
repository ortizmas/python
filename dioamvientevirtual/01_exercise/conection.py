import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row  # Melhor para impressão das entidades


def create_table(conn, cursor):
    cursor.execute(
        "CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), email VARCHAR(150), cpf INTEGER(11), cnpj INTEGER(14))"
    )
    conn.commit()


create_table(conn, cursor)
