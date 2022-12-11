from funcoesPrincipais import *

while True:
    opcao = menu()
    if opcao == 1:
        jogo.cadastrarJogos()
    elif opcao == 2:
        jogo.selecionarJogos()
    elif opcao == 3:
        jogo.deletarJogo()
    elif opcao == 4:
        jogo.selecionarPorId()
    elif opcao == 5:
        jogo.alterarJogo()              
    elif opcao == 6:
        limpa()
        break