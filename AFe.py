# Disciplina: Linguagens Formais e Autômatos - 2024.2 - UFMA
# Alunas: Amanda Almeida Cardoso e Paloma Santos Ferreira
# Fevereiro 2025
# Implementação de um Automato Finito Não Determinístico com Movimentos Vazios (AFNe)


class AFe :
    def __init__(self, estados, alfabeto, estadoInicial, funPrograma, estadosFinais) :
        self.estados = estados
        self.alfabeto = alfabeto
        self.funPrograma = funPrograma  #dicionario de transições
        self.estadoInicial = estadoInicial
        self.estadosFinais = estadosFinais

    #Calcula o fecho vazio de um estado, retorna o fecho
    def fechoVazio(self, estado):

        fecho = {estado} #O próprio estado faz parte do fecho
        estadosPossiveis = [estado]

        while estadosPossiveis:
            atual = estadosPossiveis.pop()
            #Verificando transições vazias a partir do estudo atual
            if(atual,"&") in self.funPrograma:
                for prox_estado in self.funPrograma[(atual,"&")]:
                    if prox_estado not in fecho:
                        fecho.add(prox_estado)
                        estadosPossiveis.append(prox_estado)


        return fecho

    #Verifica se a palavra é aceita pelo AFNe
    def verificaPalavra(self, palavra):

        estadosPossiveis = set(self.fechoVazio(self.estadoInicial))

        #Verifica quais estados são acessíveis a partir do símbolo lido
        #Adiciona esses estados no conjunto estados possíveis.

        for letra in palavra:
            proximosEstados = set()
            for estado in estadosPossiveis:
                for estadoDestino in self.funPrograma.get((estado, letra), []):             #Buscar os estados de destino no dicionário
                    proximosEstados =  proximosEstados | self.fechoVazio(estadoDestino)     #Insere o fecho vazio do estado de destino no conjunto próximosEstados

            estadosPossiveis = proximosEstados                                              #Atualiza estados possíveis

        return not self.estadosFinais.isdisjoint(estadosPossiveis)                          #Retorna TRUE se existe um estado final no conjunto de estados possíveis


    #Verifica se o estado inicial também é final
    #Se for, ele adiciona a transição vazia para o próprio estado.
    #A palavra vazia "&" é aceita
    def verificaEstadoFinalEInicial(self):

        if(self.estadoInicial in self.estadosFinais):
            self.funPrograma[(int(self.estadoInicial), "&")] = {int(self.estadoInicial)}
            return True
        return False




def _entrar_com_estados_():

        estados = input("Digite até 5 estados separados por vírgula: ")
        mapEstados = list(map(int, estados.split(',')))

        if (len(mapEstados) <= 5) and len(mapEstados) > 0:
            return set(mapEstados)
        else:
            print("Valores inválidos, tente novamente")
            return _entrar_com_estados_()

def _entrar_com_alfabeto_():
    alfabeto = input("Digite até 3 símbolos do alfabeto separados por vírgula: ")
    setAlfabeto = set(alfabeto.split(','))
    if len(setAlfabeto) <= 3 and len(setAlfabeto) > 0:
        return setAlfabeto
    else:
        print("Alfabeto inválido. Tente novamente")
        return _entrar_com_alfabeto_()

def _entrar_com_estado_inicial_(setEstados):
    estadoInicial = int(input("Digite o estado inicial: "))
    if estadoInicial in setEstados:
        return estadoInicial
    else:
        print("Estado inical não existe no conjunto de estados. Tente novamente")
        return _entrar_com_estado_inicial_(setEstados)

def _entrar_com_transicao_(setEstados, setAlfabeto):

    aux = 0
    transicoes = {}
    while aux < 7 :
        transicao = input("Digite uma transição. Considere & como epsilon. Digite 'sair' para finalizar ")
        if transicao.lower() == 'sair':
            break

        primeiroEstado = int(transicao[0])
        simbolo = transicao[1]
        segundoEstado = int(transicao[2])

        if  len(transicao) != 3:
            print("Formato incorreto")
            continue
        if primeiroEstado not in setEstados or not isinstance(primeiroEstado,int):
            print("Estado inexistente")
            continue
        if simbolo != "&" and transicao[1] not in setAlfabeto or not isinstance(simbolo, str) :
            print("Símbolo é inválido")
            continue
        if segundoEstado not in setEstados or not isinstance(segundoEstado,int):
            print("Estado inexistente")
            continue

        if (int(primeiroEstado), simbolo) in transicoes:                        # Se o estado e simbolo já estão no dicionário  (0,"a") = {1, 2, 3}
            transicoes[int(primeiroEstado),simbolo].add(int(segundoEstado))     # Adiciona o estado final no set
        else:
            transicoes[(int(primeiroEstado), simbolo)] = {int(segundoEstado)}   # Cria o set

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

    print("\n\n### Criando AFNe ###\n")

    alfabeto = _entrar_com_alfabeto_()
    estados = _entrar_com_estados_()
    estadoInicial = _entrar_com_estado_inicial_(estados)
    funcaoPrograma = _entrar_com_transicao_(estados,alfabeto)
    estadosFinais = _entrar_com_estados_finais_(estados)

    automato = AFe(estados,alfabeto,estadoInicial, funcaoPrograma, estadosFinais)
    automato.verificaEstadoFinalEInicial()

    print("\n### AFNe criado ###")
    print(f"Σ (alfabeto): {automato.alfabeto}")
    print(f"Q (estados): {automato.estados}")
    print(f"δ: (função programa): {automato.funPrograma}")
    print(f"q0: (estado inicial): {automato.estadoInicial}")
    print(f"F: (estados finais): {automato.estadosFinais}")

    print("\n### Calculando Fecho Vazio ###")
    for estado in estados:
        fechoVazio = automato.fechoVazio(estado)
        print(f"O fecho vazio do estado {estado} é: {fechoVazio}")

    print("\n### Testes ### \n")
    sair = True
    print("Testando palavras. Digite 'sair' para finalizar:\n")
    while(sair):
        palavra = input(">>> ")
        if palavra.lower() == 'sair':
            break
        print(f"Palavra '{palavra}': {automato.verificaPalavra(palavra)}")

main()





