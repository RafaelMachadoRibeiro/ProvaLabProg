#Alternativa A
def soma_diagonal_principalA(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    print(soma)
    return soma

#Alternativa B
def soma_diagonal_principalB(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][-i]
    print(soma)
    return soma

#Alternativa C
def soma_diagonal_principalC(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    print(soma)
    return soma

#Alternativa D
def soma_diagonal_principalD(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][len(matriz)-i-1]
    print(soma)
    return soma

#Alternativa E
def soma_diagonal_principalE(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[len(matriz)-i-1[i]]
    print(soma)
    return soma

'''
Saída Obtida: 

Resposta correta: 

Resposta que marquei: 
'''