import mysql.connector

# Criando a conexão com o banco de dados
banco = mysql.connector.connect(
    host="xxxxxxxxxxx",
    user="xxxxxxxxxxx",
    passwd="xxxxxx",
    database="xxxxxxxxx"
)

codigo = input("Digite o código do produto: ")
descricao = input("Digite a descrição do produto: ")
preco = input("Digite o preço do produto: ")

categoria = ''
while categoria == '':
    tipo_categoria = input("Digite: [1] informática [2] Alimentos [3] eletrônicos:\n")

    if tipo_categoria == "1":
        categoria = "Informatica"
        break
    elif tipo_categoria == "2":
        categoria = "Alimentos"
        break
    elif tipo_categoria == "3":
        categoria = "Eletronicos"
        break

cursor = banco.cursor()
comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)"
dados = (str(codigo), str(descricao), str(preco), categoria)
cursor.execute(comando_SQL, dados)
banco.commit()
