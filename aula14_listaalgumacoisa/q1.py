class Contato:
    def __init__(self, id, nome, estado):
        self.set_id(id) #atributo de instância
        self.set_nome(nome)
        self.set_email(estado)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == '': raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    
    def set_email(self, email):
        if email == '': raise ValueError("Nome não pode ser vazio")
        self.__email = email
    
    def get_id(self): return self.__id

    def get_nome(self): return self.__nome

    def get_email(self): return self.__email

    def __str__(self):
        return f"id: {self.__id} - nome: {self.__nome} - email {self.__email}"

class Jogadores:
    def __init__(self, id, idTime, nome, camisa):
        self.set_id(id) #atributo de instância
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    
    def set_idTime(self, idTime):
        if idTime < 0: raise ValueError("Id do time deve ser positivo")
        self.__idTime = idTime

    def set_nome(self, nome):
        if nome == '': raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    
    def set_camisa(self, camisa):
        if camisa < 0: raise ValueError("O número da camisa deve ser positivo")
        self.__camisa = camisa
    
    def get_id(self): return self.__id

    def get_idTime(self): return self.__idTime

    def get_nome(self): return self.__nome

    def get_camisa(self): return self.__camisa

    def __str__(self):
        return f"id: {self.__id} - id do time {self.__idTime} - nome: {self.__nome} - número da camisa: {self.__camisa}"    
    
class UI:
    def main()