class bcolors:
        verde = '\033[92m'
        vermelho = '\033[91m'
        azul = '\033[34m'
        amarelo = '\033[93m'
        reset = '\033[0m'

def corVerde(antecessor,string,sucessor):
    print(antecessor + bcolors.verde + string + bcolors.reset + sucessor)

def corVermelha(antecessor,string,sucessor):
    print(antecessor + bcolors.vermelho + string + bcolors.reset + sucessor)

def corAzul(antecessor,string,sucessor):
    print(antecessor + bcolors.azul + string + bcolors.reset + sucessor) 

def corAmarelo(antecessor,string,sucessor):
    print(antecessor + bcolors.amarelo + string + bcolors.reset + sucessor)

def linha1(tamanho):
    corAzul('',tamanho *'-=-','')

def linha2(tamanho):
    corAzul('',tamanho *'⇌⇌⇌⇌','')

linha1(10)
pika
