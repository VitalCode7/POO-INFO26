from datetime import datetime

class Paciente:
    def __init__(self, id, n, c, t, nasc):
        self.set_id(id)
        self.set_nome(n)
        self.set_cpf(c)
        self.set_telefone(t)
        self.set_nasc(nasc)
    
    def set_id(self, id):
        if id < 0: raise ValueError("id não pode ser negativo")
        self.__id = id
    
    def set_nome(self, n):
        if n == "": raise ValueError("nome não pode ser vazio")
        self.__nome = n

    def set_cpf(self, cpf):
        if cpf == "": raise ValueError("CPF não pode ser vazio")
        self.__cpf = cpf

    def set_telefone(self, t):
        if t == "": raise ValueError("telefone não pode ser vazio")
        self.__telefone = t

    def set_nasc(self, nasc):
        if nasc > datetime.now(): raise ValueError("Exterminador do futuro?")
        self.__nascimento = nasc

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_telefone(self):
        return self.__telefone
    
    def get_nascimento(self):
        return self.__nascimento
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento.strftime('%d/%m/%Y')}"
    
    def idade(self):
        tempo = datetime.now() - self.__nascimento
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30
        dias = tempo.days % 365 % 30
        return f"{anos} anos, {meses} meses, {dias} dias"
    
class PacienteUI:
    __pacientes = []

    @staticmethod
    def menu():
        print("1 - inserir")
        print("2 - listar")
        print("3 - atualizar")
        print("4 - excluir")
        print("5 - pesquisar")
        print("6 - aniversariantes")
        print("7 - sair")
        x = int(input("Escolha uma das seguintes opções: "))
        return x
    
    @staticmethod
    def main():
        op = PacienteUI.menu()
        while op != 7:    
            if op == 1: PacienteUI.inserir()
            elif op == 2: PacienteUI.listar()
            elif op == 3: PacienteUI.atualizar()
            elif op == 4: PacienteUI.excluir()
            elif op == 5: PacienteUI.pesquisar()
            elif op == 6: PacienteUI.aniversariantes()
            op = PacienteUI.menu()

    @classmethod
    def inserir(cls):
        id = int(input("digite o id: "))
        nome = input("digite o nome: ")
        cpf = input("digite o cpf: ")
        telefone = input("digite o telefone: ")
        nascimento = datetime.strptime(input("Informe a data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
        x = Paciente(id, nome, cpf, telefone, nascimento)
        cls.__pacientes.append(x)
    
    @classmethod
    def listar(cls):
        if not cls.__pacientes:
            print("Nenhum paciente cadastrado.")
        for x in cls.__pacientes:
            print(x)
    
    @classmethod
    def atualizar(cls):
        id = int(input("digite o id do paciente que você deseja atualizar: "))
        for x in cls.__pacientes:
            if x.get_id() == id:
                nome = input("digite o novo nome: ")
                cpf = input("digite o novo cpf: ")
                telefone = input("digite o novo telefone: ")
                nasc_str = input("Informe a nova data de nascimento (dd/mm/aaaa): ")
                nascimento = datetime.strptime(nasc_str, "%d/%m/%Y")
                
                x.set_nome(nome)
                x.set_cpf(cpf)
                x.set_telefone(telefone)
                x.set_nasc(nascimento)
                print("Paciente atualizado com sucesso!")
                return
        print("Paciente não encontrado.")
    
    @classmethod
    def excluir(cls):
        id = int(input("digite o id do paciente que você deseja remover: "))
        for x in cls.__pacientes:
            if x.get_id() == id:
                cls.__pacientes.remove(x)
                print("Paciente removido.")
                return
        print("Paciente não encontrado.")

    @classmethod
    def pesquisar(cls):
        encontrados = []
        inicio = input("Digite as primeiras letras do nome: ").lower()
        for x in cls.__pacientes:
            if x.get_nome().lower().startswith(inicio):
                encontrados.append(x)
        if len(encontrados) == 0:
            print("Nenhum paciente com esse nome foi encontrado")
        else:
            for t in encontrados:
                print(t)
    
    @classmethod 
    def aniversariantes(cls):
        i = int(input("escolha um mês de 1 a 12: "))

        print(f"\nAniversariantes do mês {i}:")
        for x in cls.__pacientes:
            if x.get_nascimento().month == i:
                print(f"Nome: {x.get_nome()} - Aniversário: {x.get_nascimento().day}/{x.get_nascimento().month}")

PacienteUI.main()