#Solução 01:
def tem_duplicados1(lista1):
    for i in range(len(lista1)):
        for j in range(i+1, len(lista1)):
            if lista1[i] == lista1[j]:
                return True
            return False

#Solução 2 
def tem_duplicados2(lista2):
    lista_ordenada = sorted(lista2)
    for i in range(len(lista_ordenada)-1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            return True
        return False

#Solução 3
def tem_duplicados3(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
        return False

'''
Saída Obtida: 

Resposta correta: 

Resposta que marquei: 
'''