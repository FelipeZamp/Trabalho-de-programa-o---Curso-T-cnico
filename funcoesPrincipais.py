from processos import *
from menusAuxiliares import *

def cadastrarJogos() -> dict:
    limpa(limpar)
    linha1(10)
    jogo = {}
    jogo['id'] = gerarID()+1
    jogo['nome'] = str(input('Nome do jogo: '))
    jogo['data'] = str(input('Data de lançamento do jogo: '))
    jogo['plataforma'] = str(input('Plataforma do jogo: '))
    jogo['genero'] = str(input('Gênero do jogo: '))
    jogo['estudio'] = str(input('Estudio(s) do jogo: '))
    linha1(10)
    enterContinuar()
        
    jogos = lerArquivo()
    jogos.append(jogo)
    salvarArquivo(jogos)

def selecionarJogos():
    limpa(limpar)
    linha1(10)
    jogos = lerArquivo()
    if listaVazia(jogos) != 1:
        for jogo in jogos:
            print(f'ID: {jogo["id"]}')
            print(f'Nome: {jogo["nome"]}')
            print(f'Data de lançamento: {jogo["data"]}')
            print(f'plataforma: {jogo["plataforma"]}')
            print(f'Gênero: {jogo["genero"]}')
            print(f'Estudio(s): {jogo["estudio"]}')
            linha1(10)
        enterContinuar()

def deletarJogo():
    limpa(limpar)
    conteudo = lerArquivo()
    if listaVazia(conteudo) != 1:          
        idjogo = selecionarID()
        indice = idNaoEncontrada(conteudo, idjogo)
        if indice != 0.5:                     
            del(conteudo[indice])
            limpa(limpar)
            linha1(10)
            corVerde('',f'ID {idjogo} Deletado com sucesso','')
            linha1(10)
            salvarArquivo(conteudo)
            enterContinuar()           

def selecionarPorId():
    limpa(limpar)
    conteudo = lerArquivo()

    if listaVazia(conteudo) != 1:
        id = selecionarID()
        indice = idNaoEncontrada(conteudo, id)
        if indice != 0.5:
            for n in conteudo[indice]:
                print(f"{n}: {conteudo[indice][n]}")
            linha1(10)                
            enterContinuar()


def alterarJogo():
    limpa(limpar)
    conteudo = lerArquivo()   
    if listaVazia(conteudo) != 1:
        idjogo = selecionarID()
        indice = idNaoEncontrada(conteudo, idjogo)
        if indice != 0.5:
            opcao = menuAlterarJG()
            auxiliarAltJogo(opcao, indice, conteudo)
            salvarArquivo(conteudo)