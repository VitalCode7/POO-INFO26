class Time:
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
    contatos = []

    @staticmethod
    def main():
        op = 0
        while op != 12:
            op = UI.menu()
            if op == 1: UI.inserir_t()
            elif op == 2: UI.listar_t()
            elif op == 3: UI.atualizar_t()
            elif op == 4: UI.excluir_t()
            elif op == 5: UI.pesquisar_t()
            elif op == 6: UI.inserir_j()
            elif op == 7: UI.listar_j()
            elif op == 8: UI.atualizar_j()
            elif op == 9: UI.excluir_j()
            elif op == 10: UI.listar_j_de_t()
            elif op == 11: UI.transferir_j()

    @staticmethod
    def menu():
        print("\n1 - Inserir time")
        print("2 - Listar times")
        print("3 - Atualizar time")
        print("4 - Excluir time")
        print("5 - Pesquisar time")
        print("6 - Inserir jogador")
        print("7 - Listar jogadores")
        print("8 - Atualizar jogador")
        print("9 - Exluir jogador")
        print("10 - Listar jogadores de um time")
        print("11 - Transferir jogador")
        print("12 - Sair")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir_t(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome do time: ")
        estado = input("Informe o estado: ")

        x = Contato(id, nome, estado)
        cls.contatos.append(x)
        print("Time inserido com sucesso!")

    @classmethod
    def listar_t(cls):
        if len(cls.contatos) == 0:
            print("Nenhum contato na agenda")
        else:
            for x in cls.contatos:
                print(x)

    @classmethod
    def atualizar_t(cls):
        id = int(input("Informe o id do contato: "))
        for x in cls.contatos:
            if x.get_id() == id:
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                fone = input("Novo fone: ")

                x.set_nome(nome)
                x.set_email(email)
                x.set_fone(fone)

                print("Contato atualizado!")
                return
        
        print("Contato não encontrado")

    @classmethod
    def excluir_t(cls):
        id = int(input("Informe o id do contato: "))
        for x in cls.contatos:
            if x.get_id() == id:
                cls.contatos.remove(x)
                print("Contato removido!")
                return
        
        print("Contato não encontrado")

    @classmethod
    def pesquisar_t(cls):
        inicio = input("Digite as iniciais do nome: ").lower()
        encontrados = []

        for x in cls.contatos:
            if x.get_nome().lower().startswith(inicio):
                encontrados.append(x)

        if len(encontrados) == 0:
            print("Nenhum contato encontrado")
        else:
            for x in encontrados:
                print(x)

    @classmethod
    def inserir_j(idTime):

    def listar_j(cls):
    
    def atualizar_j(cls):

    def excluir_j(cls):

    def listar_j_de_t(cls):

    def transferir_j(cls):
 
UI.main()