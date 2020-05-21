import sqlalchemy


engine = sqlalchemy.create_engine("sqlite:///ac5-tecweb/banco.db")
connection = engine.connect()

result = connection.execute("SELECT EMAIL, PRESENCA FROM PRESENCA ORDER BY ID")

print("-----------------------")
presencas = []

for linha in result:
    presenca = linha.presenca
    presencas.append(presenca)

print(presencas)