import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row  # Melhor para impressão das entidades

try:
    data = ("Somala Lula", "lu@gmail.com")
    cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", data)
    cursor.execute(
        "INSERT INTO clients (id, name, email) VALUES (?, ?, ?)",
        (2, "Teste 2", "test@tes.com"),
    )
    conn.commit()
except Exception as e:
    print(f"Ocurreu um erro: {e}")
    conn.rollback()
