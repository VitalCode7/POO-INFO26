class playlist:

    def __init__(self, id, nome, descricao):

        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    # SET
    def set_id(self, id):

        if id < 0:
            raise ValueError("O id deve ser positivo")

        self.__id = id

    def set_nome(self, nome):

        if nome == "":
            raise ValueError("Digite um nome")

        self.__nome = nome

    def set_descricao(self, descricao):

        if descricao == "":
            raise ValueError("Digite uma descrição")

        self.__descricao = descricao

    # GET
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    # STR
    def __str__(self):

        return (
            f"ID: {self.__id} "
            f"- Nome: {self.__nome} "
            f"- Descrição: {self.__descricao}"
        )


class musica:

    def __init__(self, id, titulo, artista, album):

        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)

    # SET
    def set_id(self, id):

        if id < 0:
            raise ValueError("O id deve ser positivo")

        self.__id = id

    def set_titulo(self, titulo):

        if titulo == "":
            raise ValueError("Digite um título")

        self.__titulo = titulo

    def set_artista(self, artista):

        if artista == "":
            raise ValueError("Digite o artista")

        self.__artista = artista

    def set_album(self, album):

        if album == "":
            raise ValueError("Digite o álbum")

        self.__album = album

    # GET
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_artista(self):
        return self.__artista

    def get_album(self):
        return self.__album

    # STR
    def __str__(self):

        return (
            f"ID: {self.__id} "
            f"- Título: {self.__titulo} "
            f"- Artista: {self.__artista} "
            f"- Álbum: {self.__album}"
        )


class playlistitem:

    def __init__(self, id, idplaylist, idmusica, sequencia):

        self.set_id(id)
        self.set_idplaylist(idplaylist)
        self.set_idmusica(idmusica)
        self.set_sequencia(sequencia)

    # SET
    def set_id(self, id):

        if id < 0:
            raise ValueError("O id deve ser positivo")

        self.__id = id

    def set_idplaylist(self, idplaylist):

        if idplaylist < 0:
            raise ValueError("O id da playlist deve ser positivo")

        self.__idplaylist = idplaylist

    def set_idmusica(self, idmusica):

        if idmusica < 0:
            raise ValueError("O id da música deve ser positivo")

        self.__idmusica = idmusica

    def set_sequencia(self, sequencia):

        if sequencia < 0:
            raise ValueError("A sequência deve ser positiva")

        self.__sequencia = sequencia

    # GET
    def get_id(self):
        return self.__id

    def get_idplaylist(self):
        return self.__idplaylist

    def get_idmusica(self):
        return self.__idmusica

    def get_sequencia(self):
        return self.__sequencia

    # STR
    def __str__(self):

        return (
            f"ID: {self.__id} "
            f"- Playlist: {self.__idplaylist} "
            f"- Música: {self.__idmusica} "
            f"- Sequência: {self.__sequencia}"
        )


class UI:

    playlists = []
    musicas = []
    itens = []

    @staticmethod
    def menu():

        print("\n===== MENU =====")
        print("1 - Inserir música")
        print("2 - Listar músicas")
        print("3 - Atualizar música")
        print("4 - Excluir música")
        print("5 - Inserir playlist")
        print("6 - Listar playlists")
        print("7 - Atualizar playlist")
        print("8 - Excluir playlist")
        print("9 - Inserir item na playlist")
        print("10 - Listar itens da playlist")
        print("11 - Sair")

        return int(input("Escolha uma opção: "))

    @staticmethod
    def main():

        op = 0

        while op != 11:

            op = UI.menu()

            if op == 1:
                UI.inserir_musica()

            elif op == 2:
                UI.listar_musicas()

            elif op == 3:
                UI.atualizar_musica()

            elif op == 4:
                UI.excluir_musica()

            elif op == 5:
                UI.inserir_playlist()

            elif op == 6:
                UI.listar_playlists()

            elif op == 7:
                UI.atualizar_playlist()

            elif op == 8:
                UI.excluir_playlist()

            elif op == 9:
                UI.inserir_item_playlist()

            elif op == 10:
                UI.listar_itens_playlist()

            elif op == 11:
                print("Programa encerrado!")

            else:
                print("Opção inválida!")

    # PLAYLIST
    @classmethod
    def inserir_playlist(cls):

        id = int(input("ID da playlist: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")

        p = playlist(id, nome, descricao)

        cls.playlists.append(p)

        print("Playlist cadastrada!")

    @classmethod
    def listar_playlists(cls):

        if len(cls.playlists) == 0:
            print("Nenhuma playlist cadastrada.")

        else:

            print("\n--- PLAYLISTS ---")

            for p in cls.playlists:
                print(p)

    @classmethod
    def atualizar_playlist(cls):

        id = int(input("ID da playlist: "))

        for p in cls.playlists:

            if p.get_id() == id:

                nome = input("Novo nome: ")
                descricao = input("Nova descrição: ")

                p.set_nome(nome)
                p.set_descricao(descricao)

                print("Playlist atualizada!")

                return

        print("Playlist não encontrada!")

    @classmethod
    def excluir_playlist(cls):

        id = int(input("ID da playlist: "))

        for p in cls.playlists:

            if p.get_id() == id:

                cls.playlists.remove(p)

                nova_lista = []

                for i in cls.itens:

                    if i.get_idplaylist() != id:
                        nova_lista.append(i)

                cls.itens = nova_lista

                print("Playlist removida!")

                return

        print("Playlist não encontrada!")

    # MÚSICA
    @classmethod
    def inserir_musica(cls):

        id = int(input("ID da música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")

        m = musica(id, titulo, artista, album)

        cls.musicas.append(m)

        print("Música cadastrada!")

    @classmethod
    def listar_musicas(cls):

        if len(cls.musicas) == 0:
            print("Nenhuma música cadastrada.")

        else:

            print("\n--- MÚSICAS ---")

            for m in cls.musicas:
                print(m)

    @classmethod
    def atualizar_musica(cls):

        id = int(input("ID da música: "))

        for m in cls.musicas:

            if m.get_id() == id:

                titulo = input("Novo título: ")
                artista = input("Novo artista: ")
                album = input("Novo álbum: ")

                m.set_titulo(titulo)
                m.set_artista(artista)
                m.set_album(album)

                print("Música atualizada!")

                return

        print("Música não encontrada!")

    @classmethod
    def excluir_musica(cls):

        id = int(input("ID da música: "))

        for m in cls.musicas:

            if m.get_id() == id:

                cls.musicas.remove(m)

                nova_lista = []

                for i in cls.itens:

                    if i.get_idmusica() != id:
                        nova_lista.append(i)

                cls.itens = nova_lista

                print("Música removida!")

                return

        print("Música não encontrada!")

    # ITENS
    @classmethod
    def inserir_item_playlist(cls):

        id = int(input("ID do item: "))
        id_playlist = int(input("ID da playlist: "))
        id_musica = int(input("ID da música: "))
        sequencia = int(input("Sequência: "))

        item = playlistitem(
            id,
            id_playlist,
            id_musica,
            sequencia
        )

        cls.itens.append(item)

        print("Item inserido!")

    @classmethod
    def listar_itens_playlist(cls):

        id_playlist = int(input("ID da playlist: "))

        encontrou = False

        print("\n--- ITENS DA PLAYLIST ---")

        for i in cls.itens:

            if i.get_idplaylist() == id_playlist:

                for m in cls.musicas:

                    if m.get_id() == i.get_idmusica():

                        print(
                            f"Sequência: {i.get_sequencia()} "
                            f"- Música: {m.get_titulo()}"
                        )

                        encontrou = True

        if encontrou == False:
            print("Nenhum item encontrado.")


UI.main()