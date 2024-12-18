import sqlite3
from pathlib import Path
from pycpfcnpj import cpfcnpj

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row  # Melhor para impressão das entidades


def create_client(conn, cursor, name, email, cpf, cnpj):
    data = (name, email, cpf, cnpj)
    cursor.execute(
        "INSERT INTO clients (name, email, cpf, cnpj) VALUES (?, ?, ?, ?)", data
    )
    conn.commit()


# Selecionar o tipo de Pessoa
tipo = int(input("Selecione o Tipo de Pessoa (PF = 1 ou PJ = 2): "))
name = input("Seu nome completo: ")
email = input("Seu e-mail: ")
cpf = None
cnpj = None

if tipo == 1:
    cpf = int(input("Seu CPF: "))
    if cpfcnpj.validate(cpf) != True:
        print("CPF não é valido, intente novamente")
        exit()
else:
    cnpj = int(input("Seu CNPJ: "))
    if cpfcnpj.validate(cnpj) != True:
        print("CNPJ não é valido, intente novamente")
        exit()

create_client(conn, cursor, name, email, cpf, cnpj)

print("Cadastro do cliente com sucesso!")
