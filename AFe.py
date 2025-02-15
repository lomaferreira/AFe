

class AFe :
    def __init__(self, estados, alfabeto, estadoInicial, funPrograma, estadosFinais) :
        self.estados = estados
        self.alfabeto = alfabeto
        self.funPrograma = funPrograma  #dicionario de transições
        self.estadoInicial = estadoInicial
        self.estadosFinais = estadosFinais
    def getEstados(self):
        return self.estados
    def getAlfabeto(self):
        return self.alfabeto
    def getFunPrograma(self):
        return self.funPrograma
    def getEstadoInicial(self):
        return self.estadoInicial
    def getEstadosFinais(self):
        return self.estadosFinais

    def fechoVazio(self, estado):

        fecho = {estado} #o próprio estado faz parte do fecho
        estadosPossiveis = [estado]

        while estadosPossiveis:
            atual = estadosPossiveis.pop()
            #verificando transições vazias a partir do estudo atual
            if(atual,"&") in self.funPrograma:
                for prox_estado in self.funPrograma[(atual,"&")]:
                    if prox_estado not in fecho:
                        fecho.add(prox_estado)
                        estadosPossiveis.append(prox_estado)


        return fecho

    def verificaPalavra(self, palavra):

        estadosPossiveis = set(self.fechoVazio(self.estadoInicial))

        for letra in palavra:
            proximosEstados = set()
            for estado in estadosPossiveis:
                for estadoDestino in self.funPrograma.get((estado, letra), []):
                    proximosEstados =  proximosEstados | self.fechoVazio(estadoDestino)

            estadosPossiveis = proximosEstados

        return not self.estadosFinais.isdisjoint(estadosPossiveis)


#o AFNe quer dizer que vc pode estar em dois estados ao mesmo tempo
# Isso pq a transição não custa nada
# Então para ver se uma palavra é aceita, preciso calcular o fecho vazio de cada estado que irei passar e guardar num conjunto de estados possíveis
# Assim, vou tentando consumir a palavra e recalculando os fechos a cada estado e adicionando ao conjunto de estados possiveis
# Caso a palavra tenha terminado, verifico se um dos estados possiveis é final





def _entrar_com_estados_():

        estados = input("Digite até 5 estados separados por vírgula: ")
        mapEstados = list(map(int, estados.split(',')))

        if (len(mapEstados) <= 5) and len(mapEstados) > 0:
            return set(mapEstados)
        else:
            print("Valores inválidos, tente novamente")
            _entrar_com_estados_()

def _entrar_com_alfabeto_():
    alfabeto = input("Digite até 3 símbolos do alfabeto separados por vírgula: ")
    setAlfabeto = set(alfabeto.split(','))
    if len(setAlfabeto) <= 3 and len(setAlfabeto) > 0:
        return setAlfabeto
    else:
        print("Alfabeto inválido. Tente novamente")
        _entrar_com_alfabeto_()

def _entrar_com_estado_inicial_(setEstados):
    estadoInicial = int(input("Digite o estado inicial: "))
    if estadoInicial in setEstados:
        return estadoInicial
    else:
        print("Estado inical não existe no conjunto de estados. Tente novamente")
        _entrar_com_estado_inicial_(setEstados)

def _entrar_com_transicao_(setEstados, setAlfabeto):

    aux = 0
    transicoes = {}
    while aux <= 7 :
        transicao = input("Digite uma transição. Considere & como epsilon. Digite 'sair' para finalizar ")
        if transicao.lower() == 'sair':
            break
        primeiroEstado = int(transicao[0])
        simbolo = transicao[1]
        segundoEstado = int(transicao[2])

        if  len(transicao) != 3:
            print("Formato incorreto")
            continue
        if primeiroEstado not in setEstados and not isinstance(primeiroEstado,int):
            print("Estado inexistente")
            continue
        if simbolo != "&" and transicao[1] not in setAlfabeto and not isinstance(simbolo, str) :
            print("Símbolo é inválido")
            continue
        if segundoEstado not in setEstados and not isinstance(segundoEstado,int):
            print("Estado inexistente")
            continue

        if (int(primeiroEstado), simbolo) in transicoes:
            transicoes[int(primeiroEstado),simbolo].add(int(segundoEstado))
        else:
            transicoes[(int(primeiroEstado), simbolo)] = {int(segundoEstado)}

        aux+=1

    return transicoes


def _entrar_com_estados_finais_(setEstados):
    estadosFinais = input("Digite os estados finais separados por vírgula: ")
    mapEstadosFinais = set(map(int, estadosFinais.split(',')))

    for i in mapEstadosFinais:
        if i not in setEstados:
            print("Estado final não existe no conjunto de estados. Tente novamente")
            return _entrar_com_estados_finais_(setEstados)  # Chama novamente e retorna o valor correto

    return mapEstadosFinais



def main():

    print("Criando AFe \n")

    alfabeto = _entrar_com_alfabeto_()
    estados = _entrar_com_estados_()
    estadoInicial = _entrar_com_estado_inicial_(estados)
    funcaoPrograma = _entrar_com_transicao_(estados,alfabeto)
    estadosFinais = _entrar_com_estados_finais_(estados)

    automato = AFe(estados,alfabeto,estadoInicial, funcaoPrograma, estadosFinais)

    print("AFe criado: ")
    print(f"Σ (alfabeto): {automato.getAlfabeto()}")
    print(f"Q (estados): {automato.getEstados()}")
    print(f"δ: (função programa): {automato.getFunPrograma()}")
    print(f"q0: (estado inicial): {automato.getEstadoInicial()}")
    print(f"F: (estados finais): {automato.getEstadosFinais()}")

    for estado in estados:
        fechoVazio = automato.fechoVazio(estado)
        print(f"O fecho vazio do estado {estado} é: {fechoVazio}")

    print(f"Palavra 'aabb': {automato.verificaPalavra('aabb')}")
    print(f"Palavra 'a': {automato.verificaPalavra('a')}")
    print(f"Palavra 'b': {automato.verificaPalavra('b')}")
    print(f"Palavra '&': {automato.verificaPalavra('&')}")
    print(f"Palavra 'aba': {automato.verificaPalavra('aba')}")
    print(f"Palavra 'bbab': {automato.verificaPalavra('bbab')}")
    print(f"Palavra 'ba': {automato.verificaPalavra('ba')}")


main()





