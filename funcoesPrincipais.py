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

def selecionarJogos():
    limpa()
    cor.linha1(10)
    jogos = lerArquivo()
    if listaVazia(jogos) != 1:
        for jogo in jogos:
            print(f'ID: {jogo["id"]}')
            print(f'Nome: {jogo["nome"]}')
            print(f'Data de lançamento: {jogo["data"]}')
            print(f'plataforma: {jogo["plataforma"]}')
            print(f'Gênero: {jogo["genero"]}')
            print(f'Estudio(s): {jogo["estudio"]}')
            cor.linha1(10)
        enterContinuar()

def deletarJogo():
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

def selecionarPorId():
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


def alterarJogo():
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