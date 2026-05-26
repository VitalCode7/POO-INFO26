from datetime import datetime
from datetime import timedelta

class Treino:
    def __init__(self, id, dt, dis, t):
        self.set_id(id)
        self.set_data(dt)
        self.set_distancia(dis)
        self.set_tempo(t)
    
    def set_id(self, id):
        if id < 0: raise ValueError("id não pode ser negativo")
        self.__id = id
    
    def set_data(self, dt):
        if dt > datetime.now(): raise ValueError("Exterminador do futuro?")
        self.__data = dt

    def set_distancia(self, dis):
        if dis < 0: raise ValueError("Distância não pode ser negativa")
        self.__distancia = dis

    def set_tempo(self, t):
        if t < timedelta(0): raise ValueError("tempo não pode ser negativo")
        self.__tempo = t

    def get_id(self):
        return self.__id
    
    def get_data(self):
        return self.__data
    
    def get_distancia(self):
        return self.__distancia
    
    def get_tempo(self):
        return self.__tempo
    
    def __str__(self):
        # Formatando a data e o tempo para ficarem mais visíveis no print
        data_str = self.__data.strftime("%d/%m/%Y")
        return f"ID: {self.__id} | Data: {data_str} | Distância: {self.__distancia}km | Tempo: {self.__tempo}"
    
    def pace(self):
        # Transforma o tempo total em minutos e divide pela distância
        tempo_em_minutos = self.__tempo.total_seconds() / 60
        return tempo_em_minutos / self.__distancia
    
class TreinoUI:
    __treinos = []

    @staticmethod
    def menu():
        print("\n--- MENU ---")
        print("1 - Inserir treino")
        print("2 - Listar treinos")
        print("3 - Listar por ID")
        print("4 - Atualizar treino")
        print("5 - Excluir treino")
        print("6 - Treino mais rápido")
        print("7 - Sair")
        x = int(input("Escolha uma das seguintes opções: "))
        return x
    
    @staticmethod
    def main():
        op = TreinoUI.menu()
        while op != 7:    
            if op == 1: TreinoUI.inserir()
            elif op == 2: TreinoUI.listar()
            elif op == 3: TreinoUI.listar_id()
            elif op == 4: TreinoUI.atualizar()
            elif op == 5: TreinoUI.excluir()
            elif op == 6: TreinoUI.MaisRapido()
            op = TreinoUI.menu()

    @classmethod
    def inserir(cls):
        try:
            id = int(input("Digite o ID: "))
            data = datetime.strptime(input("Digite a data (dd/mm/aaaa): "), "%d/%m/%Y")
            distancia = float(input("Digite a distância (em km): "))
            intervalo = input("Digite o tempo no formato minutos:segundos : ")
            m, s = map(int, intervalo.split(":"))
            tempo = timedelta(minutes=m, seconds=s)
            
            x = Treino(id, data, distancia, tempo)
            cls.__treinos.append(x)
            print("Treino inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir: {e}")
    
    @classmethod
    def listar(cls):
        if not cls.__treinos:
            print("Nenhum treino cadastrado.")
            return
        for x in cls.__treinos:
            print(x)
    
    @classmethod
    def listar_id(cls):
        i = int(input("Digite o ID do treino desejado: "))
        for x in cls.__treinos:
            if x.get_id() == i:
                print(x)
                return
        print("Treino não encontrado.")

    @classmethod
    def atualizar(cls):
        id = int(input("Digite o ID do treino que você deseja atualizar: "))
        for x in cls.__treinos:
            if x.get_id() == id:
                try:
                    data = datetime.strptime(input("Digite a nova data (dd/mm/aaaa): "), "%d/%m/%Y")
                    distancia = float(input("Digite a nova distância (em km): "))
                    intervalo = input("Digite o novo tempo no formato minutos:segundos : ")
                    m, s = map(int, intervalo.split(":"))
                    tempo = timedelta(minutes=m, seconds=s)

                    x.set_data(data)
                    x.set_distancia(distancia)
                    x.set_tempo(tempo)
                    print("Treino atualizado com sucesso!")
                    return
                except Exception as e:
                    print(f"Erro ao atualizar: {e}")
                    return
        print("Treino não encontrado.")
    
    @classmethod
    def excluir(cls):
        id = int(input("Digite o ID do treino que você deseja remover: "))
        for x in cls.__treinos:
            if x.get_id() == id:
                cls.__treinos.remove(x)
                print("Treino removido.")
                return
        print("Treino não encontrado.")
    
    @classmethod 
    def MaisRapido(cls):
        if not cls.__treinos:
            print("Nenhum treino cadastrado.")
            return
        
        # Encontra o treino com o menor pace (mais rápido)
        treino_mais_rapido = min(cls.__treinos, key=lambda t: t.pace())
        
        print("\n--- Treino Mais Rápido ---")
        print(treino_mais_rapido)
        print(f"Pace: {treino_mais_rapido.pace():.2f} min/km")

TreinoUI.main()