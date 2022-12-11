from typing import Type
from leituraEscritaArq import *
from cores import *

def listaVazia(conteudo):
    if len(conteudo) == 0:
        limpa()
        cor.linha1(10)
        cor.corVermelha('','Lista vazia','')
        cor.linha1(10)
        enterContinuar()
        return 1     


def idNaoEncontrada(conteudo, id):
    for i in range(len(conteudo)):
        verificar=1
        if conteudo[i]['id'] == id:
            indiceID = i
            break               
        else:
            verificar=0.5
    if verificar==0.5:
        limpa()
        cor.linha1(10)
        cor.corVermelha('','ID não encontrada!','')
        cor.linha1(10)
        enterContinuar()
        return 0.5
    else:
        return indiceID


def selecionarID():
    cor.linha1(10)
    id = int(input("Digite a ID do jogo: "))
    cor.linha1(10)
    return id 

def gerarID():
    jogos = lerArquivo()
    if len(jogos) == 0:
        return 1
    return jogos[-1]["_Jogos__id"] + 1

def enterContinuar():
    input('Pressione ENTER para continuar...')

def auxiliarAltJogo(opcao, indice, conteudo):
    if opcao == 6:
        return
    limpa()
    for i , x in enumerate(conteudo[indice]):
        nomeAtributo = x
        if i == opcao:
            atributo = input(f"Digite o(a) novo(a) {nomeAtributo}: ")
            conteudo[indice][nomeAtributo] = atributo
            cor.corVerde('',f"\n{nomeAtributo} alterado(a) para {atributo}!",'')
            enterContinuar()

def selecionarOpcao():
    op = input('Escolha uma opção: ')
    return op
 
def validarOpcao():
    opcao = input('Digite uma opção: ')
    if opcao in ['1','2','3','4','5','6']:
        return int(opcao)
    else:
        cor.corVermelha('','Opção inválida!','')
        return validarOpcao()
    
       
     

