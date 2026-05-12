class Time:
    def __init__(self, id, nome, estado):
        self.__id = id
        self.__nome = nome
        self.__estado = estado

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_estado(self):
        return self.__estado

    def set_nome(self, nome):
        self.__nome = nome

    def set_estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Estado: {self.__estado}"


class Jogador:
    def __init__(self, id, nome, camisa, id_time):
        self.__id = id
        self.__nome = nome
        self.__camisa = camisa
        self.__id_time = id_time

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_camisa(self):
        return self.__camisa

    def get_id_time(self):
        return self.__id_time

    def set_nome(self, nome):
        self.__nome = nome

    def set_camisa(self, camisa):
        self.__camisa = camisa

    def set_id_time(self, id_time):
        self.__id_time = id_time

    def __str__(self):
        return (
            f"ID: {self.__id} | Nome: {self.__nome} | "
            f"Camisa: {self.__camisa} | Time: {self.__id_time}"
        )


class UI:
    times = []
    jogadores = []

    @staticmethod
    def menu():
        print("\n===== MENU =====")
        print("1 - Inserir Time")
        print("2 - Listar Times")
        print("3 - Atualizar Time")
        print("4 - Excluir Time")
        print("5 - Inserir Jogador")
        print("6 - Listar Jogadores")
        print("7 - Atualizar Jogador")
        print("8 - Excluir Jogador")
        print("9 - Listar Jogadores do Time")
        print("10 - Transferir Jogador")
        print("11 - Sair")

        return int(input("Escolha uma opção: "))

    # ================= TIMES =================

    @classmethod
    def inserir_time(cls):
        id = int(input("ID: "))

        for t in cls.times:
            if t.get_id() == id:
                print("Já existe um time com esse ID.")
                return

        nome = input("Nome: ")
        estado = input("Estado: ")

        t = Time(id, nome, estado)
        cls.times.append(t)

        print("Time cadastrado!")

    @classmethod
    def listar_times(cls):
        if len(cls.times) == 0:
            print("Nenhum time cadastrado.")
        else:
            for t in cls.times:
                print(t)

    @classmethod
    def atualizar_time(cls):
        id = int(input("ID do time: "))

        for t in cls.times:
            if t.get_id() == id:

                nome = input("Novo nome: ")
                estado = input("Novo estado: ")

                t.set_nome(nome)
                t.set_estado(estado)

                print("Time atualizado!")
                return

        print("Time não encontrado!")

    @classmethod
    def excluir_time(cls):
        id = int(input("ID do time: "))

        # verifica se há jogadores no time
        for j in cls.jogadores:
            if j.get_id_time() == id:
                print("Não é possível excluir um time com jogadores.")
                return

        for t in cls.times:
            if t.get_id() == id:

                cls.times.remove(t)

                print("Time removido!")
                return

        print("Time não encontrado!")

    # ================= JOGADORES =================

    @classmethod
    def inserir_jogador(cls):
        id = int(input("ID: "))

        for j in cls.jogadores:
            if j.get_id() == id:
                print("Já existe um jogador com esse ID.")
                return

        nome = input("Nome: ")
        camisa = int(input("Número da camisa: "))
        id_time = int(input("ID do time: "))

        # verifica se o time existe
        existe = False

        for t in cls.times:
            if t.get_id() == id_time:
                existe = True
                break

        if not existe:
            print("Time não encontrado.")
            return

        j = Jogador(id, nome, camisa, id_time)

        cls.jogadores.append(j)

        print("Jogador cadastrado!")

    @classmethod
    def listar_jogadores(cls):
        if len(cls.jogadores) == 0:
            print("Nenhum jogador cadastrado.")
        else:
            for j in cls.jogadores:
                print(j)

    @classmethod
    def atualizar_jogador(cls):
        id = int(input("ID do jogador: "))

        for j in cls.jogadores:
            if j.get_id() == id:

                nome = input("Novo nome: ")
                camisa = int(input("Nova camisa: "))

                j.set_nome(nome)
                j.set_camisa(camisa)

                print("Jogador atualizado!")
                return

        print("Jogador não encontrado!")

    @classmethod
    def excluir_jogador(cls):
        id = int(input("ID do jogador: "))

        for j in cls.jogadores:
            if j.get_id() == id:

                cls.jogadores.remove(j)

                print("Jogador removido!")
                return

        print("Jogador não encontrado!")

    @classmethod
    def listar_jogadores_do_time(cls):
        id_time = int(input("ID do time: "))

        encontrou = False

        for j in cls.jogadores:
            if j.get_id_time() == id_time:
                print(j)
                encontrou = True

        if not encontrou:
            print("Nenhum jogador encontrado para esse time.")

    @classmethod
    def transferir_jogador(cls):
        id_jogador = int(input("ID do jogador: "))
        novo_time = int(input("Novo ID do time: "))

        # verifica se o novo time existe
        existe = False

        for t in cls.times:
            if t.get_id() == novo_time:
                existe = True
                break

        if not existe:
            print("Time não encontrado.")
            return

        for j in cls.jogadores:
            if j.get_id() == id_jogador:

                j.set_id_time(novo_time)

                print("Jogador transferido!")
                return

        print("Jogador não encontrado!")

    @staticmethod
    def main():

        op = 0

        while op != 11:

            op = UI.menu()

            if op == 1:
                UI.inserir_time()

            elif op == 2:
                UI.listar_times()

            elif op == 3:
                UI.atualizar_time()

            elif op == 4:
                UI.excluir_time()

            elif op == 5:
                UI.inserir_jogador()

            elif op == 6:
                UI.listar_jogadores()

            elif op == 7:
                UI.atualizar_jogador()

            elif op == 8:
                UI.excluir_jogador()

            elif op == 9:
                UI.listar_jogadores_do_time()

            elif op == 10:
                UI.transferir_jogador()

            elif op == 11:
                print("Programa encerrado!")

            else:
                print("Opção inválida!")


UI.main()