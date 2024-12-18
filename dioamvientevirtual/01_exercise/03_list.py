import sqlite3
from pathlib import Path
from pycpfcnpj import cpfcnpj

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row  # Melhor para impressão das entidades


def list_pfs(cursor):
    cursor.execute("SELECT * FROM clients WHERE cnpj IS NULL AND cpf IS NOT NULL")
    return cursor.fetchall()


def list_pjs(cursor):
    cursor.execute("SELECT * FROM clients WHERE cpf IS NULL AND cnpj IS NOT NULL")
    return cursor.fetchall()


# Lista de PFs
print("Lista de Pessoas Fisicas")
pfs = list_pfs(cursor)
for pf in pfs:
    print(dict(pf))

print("\n")
print("Lista de Pessoas Juridicas")
pjs = list_pjs(cursor)
for pj in pjs:
    print(dict(pj))
