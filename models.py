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
        sql = '''select email, presenca, resposta, comentario from presenca order by id desc'''
        cur = bd().execute(sql)
        presencas = []
        for email, presenca, resposta, comentario in cur.fetchall():
            presenca = Presenca(email, presenca, resposta, comentario)
            presencas.append(presenca)
        return presencas
