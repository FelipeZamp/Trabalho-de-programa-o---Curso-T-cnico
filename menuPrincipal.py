from funcoesPrincipais import *

while True:
    opcao = menu()
    if opcao == 1:
        cadastrarJogos()
    elif opcao == 2:
        selecionarJogos()
    elif opcao == 3:
        deletarJogo()
    elif opcao == 4:
        selecionarPorId()
    elif opcao == 5:
        alterarJogo()              
    elif opcao == 6:
        limpa(limpar)
        break