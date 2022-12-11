from processos import *
from menusAuxiliares import *
class Jogos:
    __id: int
    __nome: str
    __data: str
    __plataforma: str
    __genero: str
    __estudio: str
    
    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getPlataforma(self):
        return self.__plataforma

    def setPlataforma(self, plataforma):
        self.__plataforma = plataforma
    
    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero
    
    def getEstudio(self):
        return self.__estudio

    def setEstudio(self, estudio):
        self.__estudio = estudio

    def cadastrarJogos(self) -> dict:
        limpa()
        cor.linha1(10)
        self.setId(gerarID())
        self.setNome(input('Nome do jogo: '))
        self.setData(input('Data de lançamento do jogo: '))
        self.setPlataforma(input('Plataforma do jogo: '))
        self.setGenero(input('Gênero do jogo: '))
        self.setEstudio(input('Estudio(s) do jogo: '))
        
        cor.linha1(10)
        enterContinuar()
            
        jogos = lerArquivo()
        jogos.append(self.__dict__)
        salvarArquivo(jogos)

    def selecionarJogos(self):
        limpa()
        cor.linha1(10)
        jogos = lerArquivo()
        if listaVazia(jogos) != 1:
            for jogo in jogos:
                print(f'ID: {jogo["_Jogos__id"]}')
                print(f'Nome: {jogo["_Jogos__nome"]}')
                print(f'Data de lançamento: {jogo["_Jogos__data"]}')
                print(f'Plataforma: {jogo["_Jogos__plataforma"]}')
                print(f'Gênero: {jogo["_Jogos__genero"]}')
                print(f'Estudio(s): {jogo["_Jogos__estudio"]}')
                cor.linha1(10)
            enterContinuar()

    def deletarJogo(self):
        limpa()
        conteudo = lerArquivo()
        if listaVazia(conteudo) != 1:          
            idjogo = selecionarID()
            indice = idNaoEncontrada(conteudo, idjogo)
            if indice != 0.5:                     
                del(conteudo[indice])
                limpa()
                cor.linha1(10)
                cor.corVerde('',f'ID {idjogo} Deletado com sucesso','')
                cor.linha1(10)
                salvarArquivo(conteudo)
                enterContinuar()           

    def selecionarPorId(self):
        limpa()
        conteudo = lerArquivo()

        if listaVazia(conteudo) != 1:
            id = selecionarID()
            indice = idNaoEncontrada(conteudo, id)
            if indice != 0.5:
                for n in conteudo[indice]:
                    print(f"{n}: {conteudo[indice][n]}")
                cor.linha1(10)                
                enterContinuar()


    def alterarJogo(self):
        limpa()
        conteudo = lerArquivo()   
        if listaVazia(conteudo) != 1:
            idjogo = selecionarID()
            indice = idNaoEncontrada(conteudo, idjogo)
            if indice != 0.5:
                opcao = menuAlterarJG()
                auxiliarAltJogo(opcao, indice, conteudo)
                salvarArquivo(conteudo)

jogo = Jogos()