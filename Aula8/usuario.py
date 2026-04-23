class Usuario:
    def __init__(self, nome , email):
        self._nome = nome # o "_" indica que o atributo e privado
        self._email = email
    
    @property #esse é o getter
    def nome(self):
        return self._nome
    
    @nome.setter #esse e o setter
    def nome(self, valor):
        self._nome = valor
