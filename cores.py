class Cores:

    def __init__(self,verde='\033[92m',vermelho = '\033[91m',azul = '\033[34m',amarelo = '\033[93m',reset = '\033[0m'):
        self.verde = verde
        self.vermelho = vermelho
        self.azul = azul
        self.amarelo = amarelo
        self.reset = reset

    def corVerde(self,antecessor,string,sucessor):
        print(antecessor + self.verde + string + self.reset + sucessor)

    def corVermelha(self,antecessor,string,sucessor):
        print(antecessor + self.vermelho + string + self.reset + sucessor)

    def corAzul(self,antecessor,string,sucessor):
        print(antecessor + self.azul + string + self.reset + sucessor) 

    def corAmarelo(self,antecessor,string,sucessor):
        print(antecessor + self.amarelo + string + self.reset + sucessor)

    def linha1(self,tamanho):
        self.corAzul('',tamanho *'-=-','')

    def linha2(self,tamanho):
        self.corAzul('',tamanho *'⇌⇌⇌⇌','')

cor = Cores()