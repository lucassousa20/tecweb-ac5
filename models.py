## models.py
from banco import bd


class Presenca:
    def __init__(self, email, presenca, resposta, comentario):
        self.email = email
        self.presenca = presenca
        self.resposta = resposta
        self.comentario = comentario

    def gravar_presenca(self):
        sql = '''insert into presenca (email, presenca, resposta, comentario) values (?, ?, ?, ?)'''
        primeiro_interrogacao = self.email
        segundo_interrogacao = self.presenca
        terceiro_interrogacao = self.resposta
        quarto_interrogacao = self.comentario
        bd().execute(sql, [primeiro_interrogacao, segundo_interrogacao, terceiro_interrogacao, quarto_interrogacao])
        bd().commit()


    @staticmethod
    def recupera_todas():
        ## Usamos o objeto retornado por bd() para realizar comandos sql
        sql = '''SELECT * FROM PRESENCA ORDER BY ID DESC'''
        cur = bd().execute(sql)
        ## Montamos dicionário dicionários com os resultados da consulta para passar para a view
        presencas = []
        for email, presenca in cur.fetchall(): # fetchall() gera uma lista com os resultados:
            presenca = Presenca(email, presenca)
            presencas.append(presenca)

        return presencas
