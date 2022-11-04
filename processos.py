from typing import Type
from leituraEscritaArq import *
from cores import *

def listaVazia(conteudo):
    if len(conteudo) == 0:
        limpa(limpar)
        linha1(10)
        corVermelha('','Lista vazia','')
        linha1(10)
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
        limpa(limpar)
        linha1(10)
        corVermelha('','ID não encontrada!','')
        linha1(10)
        enterContinuar()
        return 0.5
    else:
        return indiceID


def selecionarID():
    linha1(10)
    id = int(input("Digite a ID do jogo: "))
    linha1(10)
    return id 

def gerarID():
    id = lerArquivo()
    idList = []
    if len(id) == 0:
        return 0
    else:
        for i in range(len(id)):
            idList.append(id[i]['id'])
    return max(idList)

def enterContinuar():
    input('Pressione ENTER para continuar...')

def auxiliarAltJogo(opcao, indice, conteudo):
    if opcao == 6:
        return
    limpa(limpar)
    for i , x in enumerate(conteudo[indice]):
        nomeAtributo = x
        if i == opcao:
            atributo = input(f"Digite o(a) novo(a) {nomeAtributo}: ")
            conteudo[indice][nomeAtributo] = atributo
            corVerde('',f"\n{nomeAtributo} alterado(a) para {atributo}!",'')
            enterContinuar()

def selecionarOpcao():
    op = input('Escolha uma opção: ')
    return op
 
def validarOpcao():
    opcao = input('Digite uma opção: ')
    if opcao in ['1','2','3','4','5','6']:
        return int(opcao)
    else:
        corVermelha('','Opção inválida!','')
        return validarOpcao()
    
       
     

