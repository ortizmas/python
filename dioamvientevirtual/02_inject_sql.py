import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row  # Melhor para impressão das entidades

id_client = input("Informe id do cliente: ")  # 1 0R 1=1
# cursor.execute(f"SELECT * FROM clients WHERE id={id_client}") # Errado
cursor.execute(f"SELECT * FROM clients WHERE id=?", (id_client,))  # Certo

clients = cursor.fetchall()

for client in clients:
    print(dict(client))
