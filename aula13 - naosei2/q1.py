class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == '':
            raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    
    def set_email(self, email):
        self.__email = email
    
    def set_fone(self, fone):
        self.__fone = fone
    
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"


class ContatoUI:
    contatos = []

    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            elif op == 2: ContatoUI.listar()
            elif op == 3: ContatoUI.atualizar()
            elif op == 4: ContatoUI.excluir()
            elif op == 5: ContatoUI.pesquisar()

    @staticmethod
    def menu():
        print("\n1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Pesquisar")
        print("6 - Sair")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")

        x = Contato(id, nome, email, fone)
        cls.contatos.append(x)
        print("Contato inserido com sucesso!")

    @classmethod
    def listar(cls):
        if len(cls.contatos) == 0:
            print("Nenhum contato na agenda")
        else:
            for x in cls.contatos:
                print(x)

    @classmethod
    def atualizar(cls):
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
    def excluir(cls):
        id = int(input("Informe o id do contato: "))
        for x in cls.contatos:
            if x.get_id() == id:
                cls.contatos.remove(x)
                print("Contato removido!")
                return
        
        print("Contato não encontrado")

    @classmethod
    def pesquisar(cls):
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

 
ContatoUI.main()