import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.sqlite")

cursor = conn.cursor()

# cursor.execute(
#     "CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), email VARCHAR(150))"
# )

data = ("Eber Ortiz Mas", "eberortizmas@gmail.com")
# cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", data)
cursor.execute("UPDATE clients SET name = ?, email = ?  WHERE id = 2", data)
conn.commit()

print("Operação realizada com sucesso com sucesso")
