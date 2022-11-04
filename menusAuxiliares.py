from processos import *

def menuBoasVindas():

    limpa(limpar)
    linha2(11)
    print(' <---TRABALHO DE TÉCNICAS DE PROGAMAÇÃO---> ')
    corVerde(''," <------SISTEMA DE CADASTRO DE JOGOS------> ",'')
    linha2(11)
    enterContinuar()

def menu():
    menuBoasVindas()
    limpa(limpar)
    linha1(10)
    print('Selecione uma opção:' )
    linha1(10)
    corVerde('1 - ','Cadastrar jogo','')
    corAmarelo('2 - ','Selecionar jogos','')
    corVermelha('3 - ','Deletar Jogo','')
    corAmarelo('4 - ','Selecionar por ID','')
    corAmarelo('5 - ','Alterar Jogo','')
    corVermelha('6 - ','Sair','')
    linha1(10)
    return validarOpcao()
    
def menuAlterarJG():
    limpa(limpar)
    linha1(15)
    print('Qual atributo deseja alterar:' )
    linha1(15)
    print('1 - Nome' )
    print('2 - Data de lançamento' )
    print('3 - Plataforma' )
    print('4 - Gênero' )
    print('5 - Estúdio' )
    print('6 - Cancelar' )
    linha1(15)
    return validarOpcao()