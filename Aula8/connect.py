import sqlite3

class Connect:
    def __init__(self):
        ###Criar conexão e a tabela##
        self.banco = sqlite3.connect("aula.db")
        self.cursor = self.banco.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS user (id integer primary key , nome text, email text )")
    
    def inserir(self, u):
        self.cursor.execute("INSERT INTO user (nome, email ) values (? , ?)",(u.nome, u._email))
        self.banco.commit()

    def alterar(self, id, novo_nome):
        self.cursor.execute("update user Set nome = ? where id = ?", (novo_nome, id))
        self.banco.commit()

    def listar(self):
        return self.cursor.execute("SELECT * FROM User").fetchall()