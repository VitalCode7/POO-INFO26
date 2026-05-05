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
        return: f"id: {id} - nome: {nome} - email {email}"

class Jogadores:
    def __init__(self, id, idTime nome, camisa):
        self.set_id(id) #atributo de instância
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == '': raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    
    def set_(self, email):
         if email == '': raise ValueError("Nome não pode ser vazio")
        self.__email = email
    
    def get_id(self): return self.__id

    def get_nome(self): return self.__nome

    def get_email(self): return self.__email

    def __str__(self):
        return: f"id: {id} - nome: {nome} - email {email}"    