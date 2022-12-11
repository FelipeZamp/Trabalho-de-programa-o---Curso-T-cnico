from processos import *

def menuBoasVindas():
    limpa()
    cor.linha2(11)
    print(' <---TRABALHO DE TÉCNICAS DE PROGAMAÇÃO---> ')
    cor.corVerde(''," <------SISTEMA DE CADASTRO DE JOGOS------> ",'')
    cor.linha2(11)
    enterContinuar()

def menu():
    menuBoasVindas()
    limpa()
    cor.linha1(10)
    print('Selecione uma opção:' )
    cor.linha1(10)
    cor.corVerde('1 - ','Cadastrar jogo','')
    cor.corAmarelo('2 - ','Selecionar jogos','')
    cor.corVermelha('3 - ','Deletar Jogo','')
    cor.corAmarelo('4 - ','Selecionar por ID','')
    cor.corAmarelo('5 - ','Alterar Jogo','')
    cor.corVermelha('6 - ','Sair','')
    cor.linha1(10)
    return validarOpcao()
    
def menuAlterarJG():
    limpa()
    cor.linha1(15)
    print('Qual atributo deseja alterar:' )
    cor.linha1(15)
    print('1 - Nome' )
    print('2 - Data de lançamento' )
    print('3 - Plataforma' )
    print('4 - Gênero' )
    print('5 - Estúdio' )
    print('6 - Cancelar' )
    cor.linha1(15)
    return validarOpcao()