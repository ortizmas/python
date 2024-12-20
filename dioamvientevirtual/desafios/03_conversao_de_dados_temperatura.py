# Descrição
# Você está desenvolvendo um sistema de monitoramento de temperaturas para uma estação meteorológica.
# O seu script deve processar os dados brutos de temperaturas e converter esses dados de Celsius para Fahrenheit.

# Para converter uma temperatura de Celsius para Fahrenheit, utiliza-se a fórmula matemática:

# TF = (TC × 9/5) + 32

# Onde:

# TF representa a temperatura em graus Fahrenheit,
# TC representa a temperatura em graus Celsius.

# Entrada
# A entrada deve receber uma string com valores numéricos separados por “,” (vírgula) representando as temperaturas em graus Celsius.

# Saída
# Deverá retornar uma lista de valores numéricos representando as temperaturas convertidas para Fahrenheit.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
# Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# 0,10,20,30,40	[32.0, 50.0, 68.0, 86.0, 104.0]
# -5,-15,5,15,25	[23.0, 5.0, 41.0, 59.0, 77.0]
# 12,25,30,18,5	[53.6, 77.0, 86.0, 64.4, 41.0]

temperaturas_ceusius = input(
    "Informe as temperaturas em graus Celsius separadas por vírgula: "
)


def converter_clecisus_para_fahrenheit(temperaturas):
    temperaturas_lista = temperaturas.split(",")
    temperaturas_fahrenheit = []

    for temperatura in temperaturas_lista:
        fahrenheit = (float(temperatura) * 9 / 5) + 32
        temperaturas_fahrenheit.append(fahrenheit)

    return temperaturas_fahrenheit


print(converter_clecisus_para_fahrenheit(temperaturas_ceusius))
