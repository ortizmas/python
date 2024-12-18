import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row  # Melhor para impressão das entidades


def create_table(conn, cursor):
    cursor.execute(
        "CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), email VARCHAR(150))"
    )
    conn.commit()


def insert_register(conn, cursor, name, email):
    data = (name, email)
    cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", data)
    conn.commit()


def update_register(conn, cursor, name, email, id):
    data = (name, email, id)
    cursor.execute("UPDATE clients SET name = ?, email = ?  WHERE id = ?", data)
    conn.commit()


def delete_register(conn, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clients WHERE id = ?", data)
    conn.commit()


def insert_many_data(conn, cursor, data):
    cursor.executemany("INSERT INTO clients (name, email) VALUES (?, ?)", data)
    conn.commit()


def list_clients(cursor):
    cursor.execute("SELECT * FROM clients ORDER BY name DESC")
    return cursor.fetchall()


def list_client(cursor, id):
    cursor.execute("SELECT * FROM clients WHERE id=?", (id,))
    result = cursor.fetchone()
    return result


def list_client_row_factory(cursor, id):
    # cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clients WHERE id=?", (id,))
    result = cursor.fetchone()
    return result


# insert_register(conn, cursor, "Luis Ortiz Mas", "eberortizmas@gmail.com")
# update_register(conn, cursor, "Lola Ortiz Mas", "eberortizmas@gmail.com", 2)
# delete_register(conn, cursor, 5)

# data = [
#     ("Guillerme Lucano", "gui@gmail.com"),
#     ("Luis Lucano", "lu@gmail.com"),
#     ("Lara Lucano", "la@gmail.com"),
#     ("Luis Lucano", "luis@gmail.com"),
#     ("Marleny Lucano", "mar@gmail.com"),
# ]
# insert_many_data(conn, cursor, data)

client = list_client(cursor, 4)
print(dict(client))

clients = list_clients(cursor)
for client in clients:
    print(dict(client))

client_row_factory = list_client_row_factory(cursor, 4)
print(dict(client_row_factory))
print(client_row_factory["name"])


print("Operação realizada com sucesso com sucesso")
