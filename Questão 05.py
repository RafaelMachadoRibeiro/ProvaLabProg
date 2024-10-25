#Solução 01:
def tem_duplicados1(lista1):
    for i in range(len(lista1)):
        for j in range(i+1, len(lista1)):
            if lista1[i] == lista1[j]:
                return True
            return False
# Complexidade de Tempo: 𝑂 ( 𝑛 2 ) O(n 2 ) — A função usa dois loops aninhados para comparar todos os pares de elementos na lista.
# Complexidade de Espaço: 𝑂 ( 1 ) O(1) — Não utiliza espaço adicional além de variáveis temporárias.

#Solução 2 
def tem_duplicados2(lista2):
    lista_ordenada = sorted(lista2)
    for i in range(len(lista_ordenada)-1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            return True
        return False
# Complexidade de Tempo: 𝑂 ( 𝑛 log ⁡ 𝑛 ) O(nlogn) — A ordenação da lista leva 𝑂 ( 𝑛 log ⁡ 𝑛 ) O(nlogn), e a passagem pela lista ordenada é 𝑂 ( 𝑛 ) O(n), mas o tempo dominante é a ordenação.
# Complexidade de Espaço: 𝑂 ( 𝑛 ) O(n) — A função cria uma nova lista ordenada.

#Solução 3
def tem_duplicados3(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
        return False
# Complexidade de Tempo: 𝑂 ( 𝑛 ) O(n) — A verificação da presença de um elemento em um conjunto e a adição de elementos ao conjunto são operações em média 𝑂 ( 1 ) O(1).
# Complexidade de Espaço: 𝑂 ( 𝑛 ) O(n) — Utiliza um conjunto para armazenar os elementos vistos, o que pode consumir até 𝑂 ( 𝑛 ) O(n) em espaço no pior caso.


'''
Saída Obtida: 
Mais Eficiente em Tempo: Solução 3 com 𝑂 ( 𝑛 ) O(n) é a mais eficiente em tempo.
Mais Eficiente em Espaço: Solução 1 é a mais eficiente em espaço, mas sua complexidade de tempo é muito pior.

Resposta correta: Alternativa C e D

Resposta que marquei: Alternativa B

Análise: Eu acabei me confundido na hora de marcar a questão, eu acabei marcando a incorreta achando que era a correta.
'''
