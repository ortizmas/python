# Descrição
# Os domínios de email são essenciais para categorizar e identificar a origem dos contatos,
# facilitando a segmentação e análise dos dados. Sabendo disso, sua função será receber uma string
# contendo múltiplos emails separados por ponto e vírgula e retornar uma lista contendo apenas os
# domínios de cada um desses emails.

# Entrada
# A entrada deve receber uma string contendo emails separados por ponto e vírgula: "email;email;email;...". Cada email é uma string.

# Saída
# Deverá retornar uma lista de strings com os domínios dos emails.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
# Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Retornar ['example.com', 'test.com']

# Recebe a entrada e armazena na variável 'entrada'
entrada = input("Ingrese os e-mails separados por punto y coma: ")


# Função responsável por extrair od dominiós dos e-mails
def extrair_dominios(emails):
    lista_emails = emails.split(";")

    dominios = []
    for email in lista_emails:
        dominio = email.split("@")
        dominios.append(dominio[1])

    return dominios


# imprime a lista de domínios
# entrada = (
#     "ana@example.com; bob@test.com; carlos@empresa.com; maria@web.com; pedro@mail.com"
# )
print(extrair_dominios(entrada))
